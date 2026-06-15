
'''
BMI calculator

height (kg)
weight (m)
'''

def bmi(kg, m):
    bmi = kg / (m * m)
    bmi = round(bmi, 2)
    return bmi

def bmi_check(bmi):
    if 0 < bmi <= 18.5:
        return "Vazn yetishmovchiligi"
    elif 18.5 < bmi <= 25:
        return "Sog'lom / Me'yoriy vazn"
    elif 25 < bmi <= 30:
        return "Ortiqcha vazn"
    elif bmi > 30.0:
        return "Semizlik"
    else:
        return  None


def main():
    kg = float(input("Mass (kg): "))
    m = float(input("Uzunlik (m): "))

    result = bmi(kg, m)

    print(f"BMI: {result}")
    print(f"Holat: {bmi_check(result)}")

main()
