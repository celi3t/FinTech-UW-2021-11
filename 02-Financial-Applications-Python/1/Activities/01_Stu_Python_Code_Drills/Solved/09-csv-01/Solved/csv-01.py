# Import the necessary libraries for reading csv files
import csv
from pathlib import Path

# Set the path for the csv file
csvpath = Path("../Resources/pokemon.csv")

# Create new lists to store data for heaviest and tallest Pokemon
heaviest = []
tallest = []

# Open the csv
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Iterate through the data and search for the number the user inputted. Remember to skip the header of the CSV.
    csv_header = next(csvreader)

    for row in csvreader:
        # Print the name of the Pokemon(identifier) and Pokedex number(species id) at that number. For example, "Pokemon No. 25 - Pikachu".
        print(f"Pokemon No. {row[0]} - {row[1]}")

        # Iterate through the data and search for Pokemon whose weight is greater than 3000. Append only the Pokemon's name and weight to the 'heaviest' list.
        if int(row[4]) > 3000:
            heaviest.append(row[1])

        # Iterate through the data and search for Pokemon whose height is greater than 50. Append only the Pokemon's name and height to the 'tallest' list.
        if int(row[3]) > 50:
            tallest.append(row[1])

# Print the list of heaviest and tallest pokemon
print(f"Heaviest Pokemon: {heaviest}")
print(f"Tallest Pokemon: {tallest}")
