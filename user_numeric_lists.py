"""
Modify this docstring.

"""

# import some modules first - how many can you make use of?

import math


# define some functions





# -------------------------------------------------------------
# Call some functions and execute code!

# This is very standard Python - it means
# "If this module is the one being executed, i.e., the main module"
# (as opposed to being imported by another module)
# Literally: "if this module name == the name of the main module"
if __name__ == "__main__":

    # call your functions here (see instructions)
    print("your code here")

"""

Examples of numeric lists

VS Code Menu / View / Command Palette / Python Interpretor
Must be 3.10 or greater to get the correlation and linear regression.


Uses only Python Standard Library module

"""

import statistics
import math

# define a variable with some univariant data
# (one varabile, many readings)
list1 = [
    23,
    45,
    8,
    24,
    22,
    54,
    42,
    43,
    84,
    88,
    3,
    1,
    99,
    38,
    34,
    48,
    9,
    5,
    6,
    14,
    2,
    4,
    78,
    10,
    43,
    2,
    44,
    54,
    23,
    23,   
]
print(list1)

# univariant time series data (one varabile over time)
# typically, x (or time) is independent and
# y is dependent on x (e.g. temperature vs hour of day)
print("Time series data")
xtimes_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print(xtimes_list)
yvalues_list = [3, 6, 9, 21, 22, 24, 25, 28, 31, 32, 33, 34]    
print(yvalues_list)
# Descriptive: Averages and measures of central tendency
# Use statisttics module to get mean, median, mode
# for a values list
print("Mean, Median, Mode")
mean = statistics.mean(list1)
print("mean:", mean)
median = statistics.median(list1)
print("Median:", median)
mode = statistics.mode(list1)
print("Mode:", mode)

# Descriptive: Measures of spread
# Get standard deviation and variance for a values list
print("Deviation and Variance data")
stdev = statistics.stdev(list1)
print("Standard Deviation:", stdev)
variance = statistics.variance(list1)
print("Variance:", variance)

# Descriptive: Measures of correlation
# Use two numerical lists of the same size
# Use statisttics module to get correlation between list1 and list2
print("Correlation data")
correlationxy = statistics.correlation(xtimes_list, yvalues_list)
print("Correlation:", correlationxy)

# Predictive: Machine Learning - Linear Regression
# If the corrlation is close to 1.0, then the data is linearly related
# If so, use statistics module to get linear regression for list1 and list2
# This is a form of supervised machine learning - it uses all known data
# Use the slope and intercept and an unknown (future) x to predict a y value
# Python functions can return multiple values
print("slope and Intercept Data")
slope, intercept = statistics.linear_regression(xtimes_list, yvalues_list)
print("Slope:", slope)
# Once we have learned the slope and intercept
# of the best-fit straight line through the data,
# we can use it to make predictions

# Predict the y value for a given x value outside the range of the data

x_max = max(xtimes_list)
newx = x_max * 15.  # predict for a future x value


# Use the slope and intercept to predict a y value for the future x value
# y = mx + b

newy = slope * newx + intercept
print("Intercept:", intercept)
print("New x:", newx)
print("New y:", newy)


# BUILT-IN FUNCTIONS ......................................
# Many built-in functions work on lists
# try min(), max(), len(), sum(), sorted(), reversed()

# Using the score list provided above, do the following:
# Calcuate the max and min scores
print("Max and Min Scores")
max = max(list1)
min = min(list1)
print("Max:", max)
print("Min:", min)
# Calculate the length of the list
print("List1 Length")
len = len(list1)
print("Length:", len)

# Calculate the sum of the list
print("Sum of List1")
sum = sum(list1)
print("Sum:", sum)

# Calculate the average of the list
print("Average of the List")
avg = sum / len
print("Average:", avg)

# Return a new list soreted in ascending order
print("Ascending Scores")
asc_scores = sorted(list1)
print("Ascending scores:", asc_scores)

# Return a new list soreted in descending order
print("Descending Scores")
desc_scores = sorted(list1, reverse=True)
print("Descending scores:", desc_scores)


"""

LIST METHODS ............................................... 

Here are some common methods that operate on an instance of a list.

append(x): Add an item to the end of the list.
extend(iterable): Add all the items from an iterable (such as another list)
     to the end of the list.
insert(i, x): Insert an item at a given position.
remove(x): Remove the first occurrence of an item.
pop([i]): Remove the item at the given position in the list, 
    and return it. If no index is specified, 
    removes and returns the last item in the list.
clear(): Remove all items from the list.
index(x[, start[, end]]): Return the index of the first occurrence of
     an item.
count(x): Return the number of occurrences of an item.
sort(key=None, reverse=False): Sort the items in the list 
     in ascending order.
reverse(): Reverse the order of the items in the list.
copy(): Return a shallow copy of the list.

"""

# append an item to the end of the list
lst = [1, 2, 3]
lst.append(4)

# extend the list with another list
lst.extend([4, 5, 6])

# insert an item at a given position (3 = first item)
i = 3
newvalue = 41
lst.insert(i, newvalue)

# remove an item
item_to_remove = 5
lst.remove(item_to_remove)
lst.insert(i,14)

# Count how many times 2 appears in the list
ct_of_23 = list1.count(2)

# Sort the list in ascending order using the sort() method
asc_scores2 = list1.sort()

# Sort the list in descending order using the sort() method
desc_scores2 = list1.sort(reverse=True)

# Copy the list to a new list
new_scores = list1.copy()

# Remove the first item from the new list
# The first item in a list is at index 0
# Think of it as an offset from the beginning of the list
first = new_scores.pop(0)

# Remove the last item from the new list
# The last item in a list is at index -1
last = new_scores.pop(-1)

# Remove the item at index 3 from the new list
print("New List after item removed at index 3 from the new list ")
fourth = new_scores.pop(3)
print(new_scores)
print(fourth)
print(new_scores)


# TRANFORMATIONS ............................

# FILTER and MAP are critical in big data applications

# Use the built-in function filter() anywhere you need to filter a list
# Filter the new list to only include scores greater than 10
# You could pass in a named function, but honestly this is easier
# Say "keep x such that x > 100 is True" given new_scores
# Cast the result using square brackets to get a list
print("Filter and Map Data")
print("Scores greater than 10")
scores_over_10 = [filter(lambda x: x > 10, new_scores)]

# Use the built-in function map() anywhere you need to transfrom

# Map each element to its square
# Say "map x to x squared" given new_scores
# Cast the result using square brackets to get a list
print("Cube Scores")
cubrt_scores = [map(lambda x: x * 3, new_scores)]

# Map each element to its Cube root
# Say "map x to the cube root of x" and cast to a list
cubrt_scores = map(lambda x: math.cubrt(x), new_scores)

# Map each element (radius) to its area
print("Radious List")
radius_list = [1, 2, 3, 4, 5]
# Say "map r to pi r squared" and cast to a list
print("Area List")
area_list = [map(lambda r: math.pi * r * r, radius_list)]
print(cubrt_scores)
print(area_list)


# TRANFORMATIONS - Using List Comprehensions
# List comprehensions are a concise way to create lists
# They work like map and filter, but are more concise
# They are the preferred "pythonic" way to do transformations

# With comprehensions, we start with what we WANT
# Filter the new list to only include scores greater than 10
# Say "keep x (for each x in new_scores) IF  x > 10"
print("List Comprehension Data")
print("Scores greater than 10")
scores_over_10 = [x for x in new_scores if x > 10]
print(scores_over_10)

# Try again "keep x (for each x in new_scores) IF  x < 42"
print(" Scores Less than 42")
scores_under_42 = [x for x in new_scores if x < 42]
print(scores_under_42)

# Map each element to its square
# Say "give me x squared (for each x in new_scores)"
print("Mapping the Elements")
cubrt_scores = [x * 3 for x in new_scores]
print(cubrt_scores)

# Map each element to its square root
# Say "give me the square root of x (for each x in new_scores)"
# and cast it to a list using square brackets
cubrt_scores = [math.sqrt(x) for x in new_scores]
print(cubrt_scores)

# Map each element (radius) to its area
# Say "give me pi r squared (for each r in radius_list)"
# and cast it to a list using square brackets
area_list = [math.pi * r * r for r in radius_list]
print(area_list)

# Map each element (radius) to its circumference
# Say "give me 2 pi r (for each r in radius_list)"
# and cast it to a list using square brackets
circumference_list = [2 * math.pi * r for r in radius_list]
print(circumference_list)

# Mastering comprehesions is a key skill for data scientists
numbers = [1, 2, 3, 4]
cubes = [x ** 3 for x in numbers]
print(cubes)

print()

# Why? Why only print if this the module called?
# Because when you write good functions, you may want to
# import this module into another script - just like you did
# math or statistics.
# Build a library of resuable functions to support your domain.

# For example, if your domain:
# Is sports, create functions to provide a list of teams.
# Is pets, create functions to calculate adoption prices.
# Is music, create functions to return a list of your favorite artists.


# When you write reusable functions for your domain, you can
# import the module with your utility functions into other modules
# and use them there.  This is a very common practice.
# Anything you write can be imported into later projects.

