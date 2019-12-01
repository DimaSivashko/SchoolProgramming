import random
m = int(input("enter M: "))
n = int(input("enter N: "))
output_array = []
for item in range(m):
    stroke = []
    for item_2 in range(n):
        stroke.append(random.randint(0, 100))
    output_array.append(stroke)

print(output_array)

for stroke in range(m):
    min = 101
    for item in output_array[stroke]:
        if item < min:
            min = item
    print(f" min for {stroke} stroke is {min}")
