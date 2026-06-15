
'''

Simple Calculator project

Operators:

1. + Addition
2. - Subtraction
3. * Multiplication
4. / Division

'''

# Qo'shish amali funksiyasi
def add(number_1, number_2):
    return number_1 + number_2

# Ayirish amali funksiyasi
def subtract(number_1, number_2):
    return number_1 - number_2

# Ko'paytirish amali funksiyasi
def multiply(number_1, number_2):
    return number_1 * number_2

# Bo'lish amali funksiyasi
def divide(number_1, number_2):
    if number_2 == 0:
        return None

    return round(number_1 / number_2, 2)


# Asosiy funksiyasi
def main():

    number_1 = float(input("Birinchi son: "))

    while True:

        print(f"Hozirgi natija: {number_1}")
        operator = input("Operator (+, -, *, /) yoki chiqish (q, stop): ")

        if operator == "q" or operator == "stop":
            break

        number_2 = float(input("Ikkinchi son: "))

        if operator == "+": # Qo'shish amali uchun
            result = add(number_1, number_2)
        elif operator == "-": # Ayirish amali uchun
            result = subtract(number_1, number_2)
        elif operator == "*": # Ko'paytirish amali uchun
            result = multiply(number_1, number_2)
        elif operator == "/": # Bo'lish amali uchun
            result = divide(number_1, number_2)

            if result is None:
                print("Sonni 0 ga bo'lib bo'lmaydi!")
                continue

        else:
            print("Bunday operator mavjud emas!")
            continue

        print(f"{number_1} {operator} {number_2} = {result}")

        number_1 = result

main()