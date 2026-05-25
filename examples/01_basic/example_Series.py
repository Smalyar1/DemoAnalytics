import pandas as pd

# 1. Создаем минимальный DataFrame
df = pd.DataFrame({
    "city": ["Москва", "Краснодар"],
    "price": [1500, 450]
})

# 2. Вырезаем КОЛОНКУ и проверяем тип
column_data = df["city"]
print(f"Тип колонки: {type(column_data)}")  # <class 'pandas.core.series.Series'>

# 3. Вырезаем СТРОКУ (индекс 0) и проверяем тип
row_data = df.loc[0]
print(f"Тип строки:  {type(row_data)}")   # <class 'pandas.core.series.Series'>

# Задаем кастомные индексы (имена строк)
weather: pd.Series = pd.Series(
    [22, 25, 19],
    index=["Москва", "Краснодар", "Новосибирск"]
)

# Доступ к элементу по его "имени"
print(weather["Краснодар"])  # Выведет: 25

prices = [100, 200, 300, 400]

# Медленный цикл
discounted_prices = []
for price in prices:
    discounted_prices.append(price * 0.9)

import pandas as pd

prices_series = pd.Series([100, 200, 300, 400])

# Векторизованная операция — без циклов!
discounted_series = prices_series * 0.9

print(discounted_series)

