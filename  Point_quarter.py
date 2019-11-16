x = int(input("Введите X: "))
y = int(input("Введите Y: "))
if x > 0 and y > 0:
    print("Точка лежит в 1-ой четверти")
elif x < 0 and y > 0:
    print("Точка лежит во 2-ой четверти")
elif x < 0 and y < 0:
        print("Точка лежит в 3-ей четверти")
elif x > 0 and y < 0:
        print("Точка лежит во 4-ой четверти")
else:
    pass
