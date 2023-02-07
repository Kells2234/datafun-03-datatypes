"""
These five list show tthe finishing order and related data front the top ten finishers respective to the driver in this past weekends Clash.

"""

# imports first

# reusable functions next

# call functions and execute code
# use if __name__ == "__main__":

import random

# Define a string list of driver last names
list_driver_names = ["Truex_Jr", "Dillon", "Busch", "Bowman", "Larson", "Redick", "Preece", "Chastain", "Hamlin", "Byron"]

# Define a strint list of car numbers
list_car_numbers = ["19", "3", "8", "48", "5", "45", "41", "1", "11", "24"]

# Define a list of outcomes
list_outcomes = ["1st place", "2nd place", "3rd place", "4th place", "5th place", "6th place", "7th place", "8th place", "9th place", "10th place"]

# Define a list of medals received
list_medals = ["gold", "silver", "bronze"]

# Define a list showing if driver won their heat race
list_heat_race_results = ["1st", "2nd", "3rd", "4th", "5th", "LCQ"]

# Drivers names, car numbers and race outcomes
race_results = list(zip(list_driver_names, list_car_numbers, list_outcomes))
race_results = tuple(race_results)
print(race_results)

#Random value chosen from a race results
random_value = random.choice(race_results)
print("randomly picked value:", random_value)

# Create a random sentence
sentence = (
    f"{random.choice(list_driver_names)} {random.choice(list_car_numbers)} "
    f"{random.choice(list_outcomes)} {random.choice(list_heat_race_results)}."
)
print()
print(sentence)
print()

# read in Julius Caesar
from io import open
with open("text_juliuscaesar.txt", "r") as fileObject:
    text = fileObject.read()
    list_words = text.split()  # split on whitespace
    unique_words = set(list_words)  # remove duplicates

# Print the count and list of words
word_ct = len(list_words)

# Print the count and list of unique words
unique_word_ct = len(unique_words)
print(unique_words)



