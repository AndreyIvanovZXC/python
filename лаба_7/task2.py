print("введите три числа")
a = int(input())
b = int(input())
c = int(input())
max_num = a
if b > max_num:
    max_num = b
    print (b,"максимальное число")
elif c > max_num:
    max_num = c
    print(max_num,"максимальное число")
