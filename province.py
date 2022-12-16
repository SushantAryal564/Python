# def gcd(a,b):
#   if(a>b):
#     maximum = a;
#     minimum = b
#   else:
#     maximum = b
#     minimum = a
#   if(minimum==0):
#     return maximum
#   else:
#      return gcd(minimum,maximum%minimum)
# def lcm(a,b):
#   return (a*b)/(gcd(a,b))
# print(lcm(24,36))

# my_info = {
#   "name": "sushant",
#   "age":12,
#   "nationality":"Nepalese"
# }
# print(my_info.keys())
# print(my_info.values())

# f1 = open("./notes.txt","r")
# f2 = open("./test1.txt","w")
# text = f1.read().upper()
# f2.write(text);
# f1.close()
# f2.close()

# txt = ",,,,,rrttgg.....banana....rrr"

# x = txt.strip(",.grt")

# print(x)

# lists = [1,2,4,5,6]
# lists.extend([2,3,4,5,6])
# print(lists)
# factDict ={7:5040}
# def recur_function(n):
#   if n == 1:
#     return n
#   else:
#     return n*recur_function(n-1);
  
# num = 7;
# if(num<0):
#   print("sorry")
# elif(num==1):
#   print(1)
# else:
#   if(num in factDict.keys()):
#     print(factDict[num])
#   else:
#     print(recur_function(num))
#     factDict[num] = recur_function(num)

# fiboDict={5:'01123'}
# def fibonacci(n):
#   if(n <= 1):
#     return n
#   else:
#     return (fibonacci(n-1)+fibonacci(n-2))

# n  = int (input("Enter an umber of terms"))
# if(n in fiboDict.keys()):
#   print(fiboDict[n])
# else:
#   fibo = "";
#   for i in range(n):
#     fibo = fibo+str(fibonacci(i))
#   print(fibo);
#   fiboDict[n] = fibo

def decToHex(n):
  if(n>8):
    decToHex(int(n/8))
  print(n%8,end="")

decToHex(2567)
  