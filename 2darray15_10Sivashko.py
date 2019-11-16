import random
b = []
def matrix():
    a = []
    for _ in range(10):
        a.append(random.randint(0, 100))
    return a
s = 0
for i in range(10):
    b.append(matrix())
for i in range(10):
    s += b[i][i]
print("Матрица",b)    
print("Сумма чисел по диагонали",s)     