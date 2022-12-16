import math
import random
def newtonsqrt(a):
  x = 0
  y = a
  while x != y:
    x =y
    y = (x+a/x)/2
  return x

print(newtonsqrt(100))
print(math.sqrt(100))

print(random.random());
print(random.randint(3,5));

print(59/60);
