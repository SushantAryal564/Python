import math
# Assignment
# width = 17
# height = 12.0
# delimiter = '.'

# print(width, "is of type ", type(width))
# print(height, "is of type ", type(height))
# print(delimiter, "is of type ", type(delimiter))

# print(width/2)
# print(width/2.0)
# print(height/3)
# print(1+2*5)
# print(delimiter*5)

# r = float(input("Enter a value of radius"))
# volume = (4/3)*math.pi*r**3
# print(volume)

copies = int(input("Enter a number of copies of book"))
price = 24.95 - (40/100)*24.95
shipping_cost = 0
if(copies == 1):
    shipping_cost = 0
if(copies > 1):
    shipping_cost = 3 + (copies-1)*0.75
total_price = copies*price + shipping_cost
print(total_price)
