a = input("Введите строку:")
count = 0
vowels = set("aeiou")
for letter in a:
    if letter in vowels:
        count += 1
print("Количество гласных равно:")
print(count)