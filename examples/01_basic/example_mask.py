import pandas as pd

df = pd.DataFrame({
    "city": ["Москва", "Краснодар", "Новосибирск"],
    "price": [1500, 450, 12300]
})

mask = df["price"] > 1000
print(mask)

# Этап 2: Передаем маску в DataFrame. Он оставляет только строки, где было True
expensive_orders = df[mask]
print(expensive_orders)