a = 50
while a > 0:
    print("Нужная сумма:",a)
    n = int(input("Вставьте монету:"))
    if n == 50:
        a = a - n
    elif n == 20:
        a = a - n
    elif n == 10:
        a = a - n
    elif n == 5:
        a = a - n
    else:
        continue

print(" Ваша сдача:", a*(-1))