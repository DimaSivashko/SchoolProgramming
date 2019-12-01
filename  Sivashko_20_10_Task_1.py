import random
m = int(input("enter M: "))
n = int(input("enter N: "))
k = int(input("enter K: "))
output_array = []
for item in range(m):
    stroke = []
    for item_2 in range(n):
        stroke.append(random.randint(0, 100))
    output_array.append(stroke)

s = 0
p = 1
for i in range(m):
    s += output_array[i][k]
    p *= output_array[i][k]

print(output_array)
print(s)
print(p)