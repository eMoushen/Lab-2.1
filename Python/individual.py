import math
a = float(input("Длина первого катета: "))
b = float(input("Длина второго катета: "))
c = math.sqrt(a**2+b**2)
C = round(c,2)
print("Гипотенуза равна:",C)