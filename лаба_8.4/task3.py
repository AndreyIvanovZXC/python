# подключите библиотеку datetime под именем dt
import datetime as dt

start_moment = dt.datetime(2024, 5, 1, 11, 0, 0)  # Напишите код здесь
current_moment = dt.datetime(2024,5,21,9,17,0)  # и здесь

total_time = current_moment - start_moment  # и здесь

print(total_time)