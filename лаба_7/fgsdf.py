# Подсчет гласных и согласных: Попросите пользователя ввести строку. Посчитайте количество гласных и согласных букв в этой строке.



var_str = str(input("введите строку: ")).lower()
glasn = ['a','e','o','i','y','u']
sogl = ['b','c','d','e','f','j','k','l','m','o','p','q','r','s','t','u','v','w','x','y','z']
count_glasn = 0
count_sogl = 0
for char in var_str:
    if char in glasn:
        count_glasn += 1
    elif char in sogl:
        count_sogl += 1
print(f'гласных, {count_glasn}, согласных {count_sogl}')


        