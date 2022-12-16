# def is_even(x):
#     return x % 2 == 0
# print(is_even(20))

# num = int(input("Enter a num"))
# print("Final digit of a num is ", num % 10)

# def last_digit(num, lastDigits):
#     return num % 10**lastDigits
# print(last_digit(9849693684, 4))

# def count_down(num):
#     if(num >= 0):
#         print(num)
#         count_down(num-1)
# print(count_down(10))

# convert a number to binary from decimal
# def convertToBinary(n):
#     if(n > 1):
#         convertToBinary(int(n/2))
#     print(n % 2, end='')
# convertToBinary(34)

# convert a number to octal from decimal
# def convertToOctal(n):
#     if(n > 0):
#         convertToOctal(int(n/8))
#     print(n % 8, end="")
# convertToOctal(8)

# Generalizing the base conversion
# def ConvertToBase(number, base):
#     if(number > 0):
#         ConvertToBase(int(number/base), base)
#     print(number % base, end="")
# ConvertToBase(8, 8)

# Conversin to Hexadeciaml
# conversion_table = ['0', '1', '2', '3', '4', '5',
#                     '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
# def conversionToHexa(number):
#     if(number > 16):
#         conversionToHexa(int(number/16))
#     print(conversion_table[number % 16], end="")
# conversionToHexa(44)
# conversion to decimal to hexa:
# def my_str(d):
#   if(d<10):
#     return d
#   else:
#     return chr(ord('A')+d-10)
  
# def bc(n,b):
#   if(n<b):
#     return my_str(n)
#   else:
#     return bc(n/b,b) + my_str(n%b)
# def bc(n,b):
#   if(n>b):
#     return bc(n/b,b)
#   print(my_str(n%b),end="")

# bc(44,16)
# To calculate the GCD
# def gcd(a, b):
#     if(a > b):
#         maximum = a
#         minimum = b
#     else:
#         maximum = b
#         minimum = a
#     if(minimum == 0):
#         return maximum
#     else:
#         return gcd(minimum, maximum % minimum)
# print(gcd(63780, 21340))
