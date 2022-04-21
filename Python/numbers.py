import math
a = float(input("Длина первого катета: "))
b = float(input("Длина второго катета: "))
c = math.sqrt(a**2+b**2)
p = a + b + c
P = round(p,2)
print("Периметр равен:",P)