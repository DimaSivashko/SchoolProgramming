import math
a = int(input("Введите a: "))
b = int(input("Введите b: "))
c = int(input("Введите c: "))
d = b**2 - 4*a*c
if d < 0:
    print("Нет решений")
elif d > 0:
    x1 =  -b+math.sqrt(d)/2*a
    x2 =  -b-math.sqrt(d)/2*a
    print("2 решения уравнения", int(x1), int(x2))
elif d == 0:
    x3 = -b/2*a
    print("1 решение уравнения", int(x3))

else:
    pass
