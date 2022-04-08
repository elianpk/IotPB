
import csv
 
import random
from datetime import date, timedelta, datetime

start_date = datetime(2015, 1, 1, 0, 0, 0, 0)
end_date = datetime(2020, 12, 30, 0, 0, 0, 0)
delta = timedelta(days=1)

with open('csv_file.csv', 'w', encoding='utf-8') as file:
    file.write("Timestamp,Temperature_Celsius\n")

    old_temperature = random.randrange(16, 33)
    while start_date <= end_date:
        start_date += delta
        
        min = old_temperature
        max = old_temperature

        if min - 3 < 16:
            min = 16
        else:
            min = min - 3

        if max + 3 > 33:
            max = 33
        else:
            max = max + 3

        temperature = random.randrange(min, max)
        a = f"{start_date},{temperature}\n"

        print(a)
        file.write(a)

        old_temperature = temperature