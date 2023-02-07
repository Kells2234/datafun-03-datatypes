"""
Modify this docstring.

"""
print("Tuples")
# Create some tuples
tupleA = (2, 4, 6, 8, 10)
tupleB = (8, 10, 12, 14, 16)

# tuple concatenation
tupleCat = tupleA + tupleB

# tuple repetition
tupleAThrice = tupleA * 3

# TODO: Start using this f-string "syntactic sugar" for quick ouptut
# just add space = space inside the curly braces
# it will print the name of the variable and the value
print(f"tupleA = {tupleA}")
print(f"tupleB = {tupleB}")
print(f"tupleAThrice = {tupleAThrice}")

# tuple membership testing

tupleD = (1, 2, 3)
hasOne = 1 in tupleD  # True
hasFour = 4 in tupleD  # False


# tuple indexing (0 is first, -1 is last, or 1 less than the length)

my_tuple = (1, 2, 3)
print(my_tuple)
first = my_tuple[0]
print(first)
second = my_tuple[1]
print(second)
third = my_tuple[2]
print(third)
last = my_tuple[-1]
print(last)


# Use tuples to return multiple values from a function


def divide_and_remainder(dividend, divisor):
    quotient = dividend // divisor
    remainder = dividend % divisor
    return quotient, remainder


q, r = divide_and_remainder(10, 3)
print(f"Quotient: {q}, Remainder: {r}")


"""


SETS .......................................................    


A set is an unordered collection of unique elements.
A set is created using curly braces.
Sets can use the same methods as lists and tuples.
Sets support the following operations:

Membership testing (using the in and not in operators)
Element addition (using the add method)
Element removal (using the remove and discard methods)
Set union (using the union method or the | operator)
Set intersection (using the intersection method or the & operator)
Set difference (using the difference method or the - operator)
Set symmetric difference (using the symmetric_difference method or ^ operator)


"""
print("Sets")


setA = {10, 20, 30, 40, 50}
setB = {1, 3, 5, 7, 9}
print(setA)
print(setB)

# set union
setC = setA | setB
print(setC)

# set intersection
setD = setA & setB
print(setD)

# set difference
setE = setA - setB

# sets are often used to remove duplicates from a list
# after gettin the set, convert it back to a list with list() or []
listWords = ["apple", "banana", "apple", "pear", "banana", "orange"]
setWords = set(listWords)
listWordsNoDuplicates = list(setWords)
listWordsNoDuplicates = [setWords]  # same as above


"""


DICTIONARIES .......................................................    

A dictionary is an unordered collection of key-value pairs.
A dictionary is created using curly braces.
A dictionary is accessed using keys, not indexes.
A dictionary is mutable, so you can add, remove, and change values.
A dictionary is iterable, so you can use it in a for loop.
A dictionary is not ordered, so you can't slice to access a range of values.

Dictionaries support the following operations:

Indexing: access the value associated with a key in the dictionary. 
For example: dogA['name'].

Membership testing: use 'in' and 'not in' operators 
to test whether a key is in the dictionary. 
For example: 'name' in dogA.

Adding and updating items: use indexing to add a new key-value pair,
or to update the value associated with an existing key. 
For example: dogA['age'] = 2.

Removing items: Use the del statement to remove a key-value pair. 
For example: del dogA['weight_kg'].

Iteration: You can use a for loop to iterate over the 
keys, values, or key-value pairs in a dictionary. 
For example: for key in dogA: print(key)

Dictionaries are a lot like 
JSON objects - a common data format used in web development.

"""
print("Dictionaries")

driverA_dict = {"name": "Truex_Jr", "car number": 19, "Position": 1.0}
driverB_dict = {"name": "K_Bush", "car number": 8, "Position": 2.0}
print(driverA_dict)
print(driverB_dict)

assessment_dict = {"low": 0, "medium": 1, "high": 2}

data_dict = {
    "name": ["Truex_jr", "K_Bush", "Larson", "Dillon"],
    "car number": [19, 8, 5, 3],
    "position": [1.0, 2.0, 3.0, 4.0],
}


