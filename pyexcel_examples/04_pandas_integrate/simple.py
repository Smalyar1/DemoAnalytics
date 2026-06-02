import pandas as pd
import pyexcel as pe

# 1. Быстро и безболезненно читаем любой формат в список словарей
raw_records = pe.get_records(file_name="prices.xlsx")

# 2. Передаем в pandas одной строчкой
df = pd.DataFrame(raw_records)

# 3. Дальше работаем в привычном pandas
print("Тип объекта:", type(df))
print(df.describe())