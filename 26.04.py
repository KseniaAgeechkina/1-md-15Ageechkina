import random
count = 0
mistake = 0
while mistake < 3:
    a = (random.randint(1, 11))
    b = (random.randint(1, 11))
    res = a + b
    print(a, "+", b)
    ot = int(input("Ответ"))
    if ot == res:
        print("класс")
        count += 1
    else:
        mistake += 1
        print("Ответе не верный")
print("Игра окончена. Правильных ответов", count)


