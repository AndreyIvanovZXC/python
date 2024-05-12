# ПЕРВАЯ ФУНКЦИЯ
# print("Введите двухзначное число")
# number = input()
# def reverse_number (number):
#     revers = number[::-1]
#     print(revers)
# reverse_number(number)

# ВТОРАЯ ФУНКЦИЯ
# print("введите число")
# number = str(input())
# a = number[::-1]
# def is_palindrome(number):
#     if number == a:
#         print("ПАЛИНДРОМ")
#     else:
#         print("НЕпалиндром")
# is_palindrome(number)


# ТРЕТЬЯ ФУНКЦИЯ
# def is_palindrome(number):
#     return str(number) == str(number)[::-1]

# print("Введите несколько чисел:")
# numbers = input().split()

# for number in numbers:
#     if is_palindrome(number):
#         print(number, "палиндром")
#     else:
#         print(number, "не палиндром")



# ВСЕ ФУНКЦИИ ВМЕСТЕ 
print("введите число")
number = input()
a = number[::-1]
def reverse_number (number):
    revers = number[::-1]
    print("перевернутое число", revers)
reverse_number(number)
def is_palindrome(number):
    if number == a:
        print("ПАЛИНДРОМ")
    else:
        print("НЕпалиндром")
def is_palindrome(number):
    return str(number) == str(number)[::-1]
print("Повторите ввод чисел")
numbers = input().split()
for number in numbers:
    if is_palindrome(number):
        print(number, "палиндром")
    else:
        print(number, "не палиндром")
is_palindrome(number)
