# tuples are immutable where as list are mutable.
# A tuple is the sequence of value which can be of any type and are indexed by an integer and are immutable.

# t1 = ('a',)  # For tuples with single value it has to include comma.
# print(t1)
# t = tuple()
# print(t)
# t2 = tuple('sushnat Aryal')
# print(t2)
# print(t2[0:7])
# # Tuples are immutable if we try to replace one tuple it will generate an error.
# tup = ('A',)+t2[0:7]  # we can concatenate two tuples with +.
# print(tup)

# swap place
# x = (5,)
# y = (10,)
# x, y = y, x
# print(x, y)

# split() method
addr = "aryalsushant564@gmail.com"
print(addr.split("@"))
username,domain = addr.split("@")
print(username,domain)

# tuples as return values
# A function can only return one value if it can return tuples it is same as returning multiple values.
# twovalue = divmod(7, 3)
# print(twovalue)
# quote, rem = divmod(7, 3)
# print(quote, rem)

# # function returning tuples
# def min_max(t):
#     return min(t), max(t)


# print(min_max([10, 20, 30, 40]))

# # variable length argument tuples
# #gather argument
# def printall(*args):
#     print(args)
# printall(10, 201, 'adslfkjsd', "asdklf", 'alsdkfj', 23)

# scatter argument
# The complement of gather is scatter.If we have a sequence of value and we want ot pass it to a function as an multiple argument we can use * operator.
# t = (7, 3)
# a = divmod(*t)
# print(a)


# def sum_all(*args):
#     return sum(args)


# value = sum_all(10, 20, 30, 40, 50, 60, 60, 70)
# print(value)

# Zip is a built in function that takes two or more sequence and zips them into lists of tuples
# s = 'abc'
# t = [0, 1, 2]
# print(zip(s, t))

# print(zip('Ann', 'Elk'))
# t = [('a', 0), ('b', 1), ('c', 2), ('d', 3)]
# for letter, number in t:
#     print(letter, number)

# # dictionaries and tuples
# d = {'a': 0, 'b': 1, 'c': 2}
# t = d.items()
# print(t)
# # we can also create a new dictionary from the list of tuples
# dictonary = dict(t)
# print(dictonary)

# # dictionary and tuples
# d = dict(zip('abc', range(3)))
# print(d)

# comparing tuples: the comparision operator work with tuples and other sequence. Python starts by comparing the first element from each sequence. If they are equal it goes on to the next element,and so on until it finds element that differ.

t = divmod(7,3);
print(t)

def summation(*args):
  print(args)
  return max(args);

print(summation(4,5,6,7,8));
t = [("a",1),("b",2),("c",3),("d",4),("e",5)]
d = dict(t)
print(d)
