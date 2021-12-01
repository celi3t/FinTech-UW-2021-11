# Use the `from` keyword to import the `shows` dictionary from the `show_data.py` file
from show_data import shows


# QUESTION 1: Is the Walking Dead still running?
print(shows['genre']['drama']['the_walking_dead']['still_running'])

# QUESTION 2: Who hosts the Daily Show (talk)?
print(shows['genre']['talk']['the_daily_show']['host'])

# QUESTION 3: Who does Will Arnett play in Arrested Development (comedy)
print(shows['genre']['comedy']['arrested_development']['cast'][2]['character'])

# QUESTION 4: Who does Peter Dinklage play in Game of Thrones (drama)?
print(shows['genre']['drama']['game_of_thrones']['cast'][1]['character'])

# QUESTION 5: Who plays Dexter in Dexter (drama) and who plays Dexter in Dexter's Lab (kids)?
# HINT: You can print multiple items at once by using a comma like this: print(thing1, thing2)
print(shows['genre']['drama']['dexter']['cast'][0]['actor'], shows['genre']['kids']['dexters_lab']['cast'][0]['actor'])

# QUESTION 6: Who are the main characters of the Office (comedy) (not the actors, but the actual character names)?
for character in shows['genre']['comedy']['the_office']['cast']:
    print(character['character'])

# QUESTION 7: List the main cast of Dexter (drama) (the actors, not the characters)
for character in shows['genre']['drama']['dexter']['cast']:
    print(character['actor'])


# QUESTION : List the American Idol Judges
for judge in shows['genre']['reality']['american_idol']['judges']:
    print(judge)

# QUESTION 9: What are the show names of the Impractical Jokers (comedy)
# Hint: You will need to use a loop for this one. You may not simply log the entire list, but must log each name individually
for character in shows['genre']['comedy']['impractical_jokers']['cast']:
    print(character['showName'])
