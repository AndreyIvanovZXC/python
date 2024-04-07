print ("введите целое не отрицательное число")
a=int(input())
fac = 1
for i in range (2, a+1):
    fac *= i
    print(fac)