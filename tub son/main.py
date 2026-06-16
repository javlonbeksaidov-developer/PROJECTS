
'''
Prime Number Checker

1. Kiritgan sonni tub son ekanligini aniqlaydi.
2. Kiritilgan sonni bo'luvchilarini aniqlaydi.
'''

def tub(son):
    count = 0
    for i in range(2, son + 1):
        if son % i == 0:
            count += 1
    
    if count == 0 or count == 1:
        return f"{son} tub son"
    return f"{son} tub son emas"

def buluvchi(son):
    count = 1
    buluvchi = "1"
    for i in range(2, son + 1):
        if son % i == 0:
            count += 1
            buluvchi = buluvchi + ", " + str(i)
    return f"{son} son bo'luvchilari ({buluvchi}).\n Jami bo'luvchilar soni {count}ta"


def main():
    print("Butun son kiriting (1 - ...). Tark etish uchun (0).")
    while True:
        son = int(input("Son: "))

        if son == 0:
            break

        if son < 0:
            print("Butun son kiriting (1 - ...). Tark etish uchun (0).")
            continue

        result_1 = tub(son)
        result_2 = buluvchi(son)

        print(result_1)
        print(result_2)

main()