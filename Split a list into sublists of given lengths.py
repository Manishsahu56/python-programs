# Python code to split a list
# into sublists of given length.

from itertools import islice

# Input list initialization
Input = [1, 2, 3, 4, 5, 6, 7]

# list of length in which we have to split
length_to_split = [2, 1, 3, 1]

# Using islice
Inputt = iter(Input)
Output = [list(islice(Inputt, elem))
		for elem in length_to_split]

# Printing Output
print("Initial list is:", Input)
print("Split length list: ", length_to_split)
print("List after splitting", Output)
