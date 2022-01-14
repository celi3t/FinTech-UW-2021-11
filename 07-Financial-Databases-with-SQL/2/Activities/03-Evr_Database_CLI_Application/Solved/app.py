# A Database CLI Application

# Import modules
import pandas as pd
import sqlalchemy as sql
import os
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv
import questionary

# Load .env file
load_dotenv()

# Set the variables for the Alpaca API and secret keys
alpaca_api_key = os.getenv("ALPACA_API_KEY")
alpaca_secret_key = os.getenv("ALPACA_SECRET_KEY")

# Create a function called `sector_report` that will be the application report.
# This function will be called from the `__main__` loop.
def sector_report(sectors, engine):

    # Print a welcome message for the application
    print("\n......Welcome to the Sector Analyzer Report.....\n")
    print("This report will calculate the yearly return of a financial sector based on the top five\n")
    print("companies in that sector based on their market capitalization.\n")

    # Using questionary, give the user a list of sectors to run the report on.
    sector = questionary.select("Which sector do you wish to report on?", choices=sectors).ask()

    print("Running report ...")

    # Write a sql statement that selects all stocks from that sector.
    # Return the values in descending order by MarketCap.
    sql_sector = f"""
        SELECT * FROM NYSE
        WHERE sector = '{sector}'
        ORDER BY MarketCap DESC
    """

    # Query the database using the sql statement written above.
    # Save the returned values in a DataFrame called `sector_df`
    sector_df = pd.read_sql_query(sql_sector, engine)

    # Create a list called `symbols`
    # to hold the "Symbol" of the top 5 stocks from the `sector_df` DataFrame
    symbols = sector_df["Symbol"][0:5]

    # The Alpaca Parameters for timeframe and daterange
    # `today` is a timestamp using Pandas Timestamp
    # `a_year_ago` is calculated using Pandas Timestamp and Timedelta
    timeframe = '1D'
    today = pd.Timestamp.now(tz="America/New_York")
    a_year_ago = pd.Timestamp(today - pd.Timedelta(days=365)).isoformat()

    # The Alpaca tradeapi.REST object
    alpaca = tradeapi.REST(
        alpaca_api_key,
        alpaca_secret_key,
        api_version="v2")

    # Use the Alpaca get_barset function to get the closing prices for the stocks.
    sector_prices_df = alpaca.get_barset(
        symbols,
        timeframe,
        start=a_year_ago,
        limit=1000
    ).df

    # An empty dictionary that will hold the daily pct change for each stock from the sector.
    symbol_pct_changes = {}

    # Calculate the daily percent change for each symbol in the sector.
    # Create a loop that selects each symbol in the symbols list.
    # Using the `sector_prices_df` DataFrame returned from the Alpaca API call,
    # call the `pct_change` function on the DataFrame's "close" column.
    for symbol in symbols:
        symbol_pct_changes[symbol] = sector_prices_df[symbol]['close'].pct_change()

    # Create a dataframe from the dictionary of daily pct changes.
    sector_pct_changes = pd.DataFrame.from_dict(symbol_pct_changes)

    # Calculate the average daily pct change for each day of the five stocks.
    sector_pct_changes['sector_pct_change'] = sector_pct_changes.mean(axis=1)

    # Sum the daily percent changes for the sector over the past year to find the sector yearly return.
    sector_yearly_rtn = sector_pct_changes['sector_pct_change'].sum()

    # Create a statement that displays the `results` of your sector_yearly_return calculation.
    # On a separate line (\n) ask the use if they would like to continue running the report.
    results = f"The cumulative return for the {sector} sector for the past year is {sector_yearly_rtn * 100}%.\nWould you like to choose another sector to analyze?"

    # Using the `results` statement created above,
    # prompt the user to run the report again (`y`) or exit the program (`n`).
    continue_running = questionary.select(results, choices=['y', 'n']).ask()

    # Return the `continue_running` variable from the `sector_report` function
    return continue_running


# The `__main__` loop of the application.
# It is the entry point for the program.
if __name__ == "__main__":

    # Database connection string to the clean NYSE database
    database_connection_string = 'sqlite:///../Resources/nyse.db'

    # Create an engine to interact with the database
    engine = sql.create_engine(database_connection_string)

    # Read the NYSE table into a dataframe called `nyse_df`
    nyse_df = pd.read_sql_table('NYSE', engine)

    # Get a list of the sector names from the `nyse_df` DataFrame
    # Be sure to drop n/a values and capture only unique values.
    # You will use this list of `sector` names for the user options in the report.
    sectors = nyse_df['Sector']
    sectors = sectors.dropna()
    sectors = sectors.unique()

    # Create a variable named running and set it to True
    running = True

    # While running is `True` call the `sector_report` function.
    # Pass the `nyse_df` DataFrame `sectors` and the database `engine` as parameters.
    while running:
        continue_running = sector_report(sectors, engine)
        if continue_running == 'y':
            running = True
        else:
            running = False
