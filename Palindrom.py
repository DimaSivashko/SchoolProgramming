s = input("Введите число: ")
l = len(s)

for i in range(l//2):
  if s[i] != s[-1-i]:
    print("Не палиндром")
    break
  else:
    print("Палиндром")
    break
