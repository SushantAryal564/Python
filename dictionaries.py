phonebook = {}
phonebook["sushant"] = 9828560584
phonebook["Prashant"] = 9840033089
phonebook["Gita Aryal"] = 9849693684
phonebook["Hem Aryal"] = 9851151183
phonebook["Rashmi Dhungana"] = 9864380086
# print(phonebook)

# A key can be a number, string, list, not tuples.
# keys = phonebook.keys()
# value = phonebook.values()
# entries = phonebook.items()


matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
def getValue(matrix,key):
    if key in matrix.keys():
        return matrix[key]
    else:
        return 0
print(getValue(matrix,(0,3)));
print(matrix.get((22,1),"Not found"))
# print((0, 1) in matrix.keys())
# print(matrix.has_key((0, 3)))


# def getValue(matrix, key):
#     if key in matrix.keys():
#         value = matrix[key]
#     else:
#         value = 0
#     return value


# print(getValue(phonebook, "sushant"))