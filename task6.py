print("введите слово палиндром")
slovo = str(input())
a = slovo[::-1]
if slovo == a:
  print("палиндром")
else:
  print("НЕпалиндром")