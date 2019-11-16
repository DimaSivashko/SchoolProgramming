import random
array = []
for _ in range(10):
    array.append(int(random.randint(0,100)))
print("Сгенерированный массив", array)
print("Максимальный элемент", max(array))
b = sum(array)
print("Сумма элементов", b)
even = 0  # четные числа
odd = 0  # нечетные числа
d = 0
for i in range(len(array)):
    if array[i] % 2 == 0:
        even += 1
    else: 
        odd += 1
        if i % 2 != 0: d += 1
print("Количество четных чисел", even)
print("Количество нечетных чисел", odd)
print("Количество нечетных чисел, стоящих на нечетных местах",d)