### Required Libraries ###
from datetime import datetime
from dateutil.relativedelta import relativedelta
from botocore.vendored import requests

### Functionality Helper Functions ###
def parse_float(n):
    """
    Securely converts a non-numeric value to float.
    """
    try:
        return float(n)
    except ValueError:
        return float("nan")


def get_btcprice():
    """
    Retrieves the current price of bitcoin in dollars from the alternative.me Crypto API.
    """
    bitcoin_api_url = "https://api.alternative.me/v2/ticker/bitcoin/?convert=USD"
    response = requests.get(bitcoin_api_url)
    response_json = response.json()
    price_dollars = parse_float(response_json["data"]["1"]["quotes"]["USD"]["price"])
    return price_dollars


def get_fg_index():
    """
    Retrieves the current Bitcoin Fear & Greed Index from the alternative.me Crypto API.
    """
    fgi_url = "https://api.alternative.me/fng/"
    response = requests.get(fgi_url)
    response_json = response.json()
    fg_index = parse_float(response_json["data"][0]["value"])
    return fg_index


def get_recommendation():
    """
    Returns a buying recommendation based on the current value of the Bitcoin Fear & Greed Index.
    """
    fg_index = get_fg_index()
    recommendation = ""
    if fg_index >= 0 and fg_index <=25:
        recommendation = "Be cautious on buying bitcoin today since the market feels 'Extreme Fear'."
    elif fg_index > 25 and fg_index < 50:
        recommendation = "Be cautious on buying bitcoin today since the market feels 'Fear'."
    elif fg_index == 50:
        recommendation = "You may buy bitcoin today since the market feels 'Neutral'."
    elif fg_index > 50 and fg_index <= 75:
        recommendation = "You may buy bitcoin today, the market feels 'Greed'"
    else:
        recommendation = "You may buy bitcoin today, the market feels 'Extreme Greed'"
    return recommendation


def build_validation_result(is_valid, violated_slot, message_content):
    """
    Defines an internal validation message structured as a python dictionary.
    """
    if message_content is None:
        return {"isValid": is_valid, "violatedSlot": violated_slot}

    return {
        "isValid": is_valid,
        "violatedSlot": violated_slot,
        "message": {"contentType": "PlainText", "content": message_content},
    }


def validate_data(dollars, intent_request):
    """
    Validates the data provided by the user.
    """

    # Validate the amount, it should be > 0
    if dollars is not None:
        dollars = parse_float(
            dollars
        )  # Since parameters are strings it's important to cast values
        if dollars <= 0:
            return build_validation_result(
                False,
                "amount",
                "The amount should be greater than zero, "
                "please provide a correct amount in dollars.",
            )

    # A True results is returned if age or amount are valid
    return build_validation_result(True, None, None)


### Dialog Actions Helper Functions ###
def get_slots(intent_request):
    """
    Fetch all the slots and their values from the current intent.
    """
    return intent_request["currentIntent"]["slots"]


def elicit_slot(session_attributes, intent_name, slots, slot_to_elicit, message):
    """
    Defines an elicit slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "ElicitSlot",
            "intentName": intent_name,
            "slots": slots,
            "slotToElicit": slot_to_elicit,
            "message": message,
        },
    }


def delegate(session_attributes, slots):
    """
    Defines a delegate slot type response.
    """

    return {
        "sessionAttributes": session_attributes,
        "dialogAction": {"type": "Delegate", "slots": slots},
    }


def close(session_attributes, fulfillment_state, message):
    """
    Defines a close slot type response.
    """

    response = {
        "sessionAttributes": session_attributes,
        "dialogAction": {
            "type": "Close",
            "fulfillmentState": fulfillment_state,
            "message": message,
        },
    }

    return response


### Intents Handlers ###
def convert_dollars(intent_request):
    """
    Performs dialog management and fulfillment for converting from dollars to bitcoin.
    """

    # Gets slots' values
    dollars = get_slots(intent_request)["amount"]

    # Gets the invocation source, for Lex dialogs "DialogCodeHook" is expected.
    source = intent_request["invocationSource"]

    if source == "DialogCodeHook":
        # This code performs basic validation on the supplied input slots.

        # Gets all the slots
        slots = get_slots(intent_request)

        # Validates user's input using the validate_data function
        validation_result = validate_data(dollars, intent_request)

        # If the data provided by the user is not valid,
        # the elicitSlot dialog action is used to re-prompt for the first violation detected.
        if not validation_result["isValid"]:
            slots[validation_result["violatedSlot"]] = None  # Cleans invalid slot

            # Returns an elicitSlot dialog to request new data for the invalid slot
            return elicit_slot(
                intent_request["sessionAttributes"],
                intent_request["currentIntent"]["name"],
                slots,
                validation_result["violatedSlot"],
                validation_result["message"],
            )

        # Fetch current session attributes
        output_session_attributes = intent_request["sessionAttributes"]

        # Once all slots are valid, a delegate dialog is returned to Lex to choose the next course of action.
        return delegate(output_session_attributes, get_slots(intent_request))

    # Get the current price of bitcoin in dolars and make the conversion from dollars to bitcoin.
    btc_value = parse_float(dollars) / get_btcprice()
    btc_value = round(btc_value, 4)

    # Return a message with conversion's result.
    return close(
        intent_request["sessionAttributes"],
        "Fulfilled",
        {
            "contentType": "PlainText",
            "content": """Thank you for your information;
            you can get {} Bitcoins for your ${} dollars.
            {}
            """.format(
                btc_value, dollars, get_recommendation()
            ),
        },
    )


### Intents Dispatcher ###
def dispatch(intent_request):
    """
    Called when the user specifies an intent for this bot.
    """

    # Get the name of the current intent
    intent_name = intent_request["currentIntent"]["name"]

    # Dispatch to bot's intent handlers
    if intent_name == "getFGIndex":
        return convert_dollars(intent_request)

    raise Exception("Intent with name " + intent_name + " not supported")


### Main Handler ###
def lambda_handler(event, context):
    """
    Route the incoming request based on intent.
    The JSON body of the request is provided in the event slot.
    """

    return dispatch(event)
