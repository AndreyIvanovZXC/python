print("Введите начальную сумму вклада")
money = float(input())
print("Введите процент вклада")
procent = float(input())
print("Введите колличество лет вклада")
srok = int(input())
def vklad (money, procent, srok):
    dohod = money * (1 + procent)**srok
    return dohod
vklad (money, procent, srok)
