# Repetation of a task is called iteration. There are two type of loops called for loop and while loop.
# i = 1
# while i <= 10:
#     print(i)
#     if i == 5:
#         break
#     i = i+1


# def square_root(a):
#     x = 0
#     y = a
#     while True:
#         x = y
#         y = (x+a/x)/2
#         if x == y:
#             break
#     return x
# print(square_root(4))

def multiplication_table(number):
    i = 1
    while i <= 10:
        first_Number = i-1
        second_Number = number-i
        print(first_Number, second_Number, sep="")
        i = i+1
multiplication_table(10)

# Python for iterate over the items of any sequence in order that they appear in the sequence.

# aboutMe = "Hello my name is sushant Aryal. I am worst at what i do best"
# for word in aboutMe:
#     print(word)

# fruits = ['banana', 'apple', 'mango', 'orange']
# # for fruit in fruits:
# #     print('current fruit', fruit)
# for fruit in range(len(fruits)):
#     print(fruits[fruit])

# range function
# for i in range(10):
#     print(i)
# print("******************")
# for i in range(6, 10):
#     print(i)
# print("************")
# for i in range(5, 10, 2):
#     print(i)

# Our own range generator with float value
# def my_range(start, end, gap):
#     while(start < end):
#         yield start
#         start = start + gap


# for z in my_range(1, 5, 0.5):
#     print(z)