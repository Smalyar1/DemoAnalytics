import pandas as pd

# Загружаем файл
df = pd.read_csv("sales.csv", dtype={"country": "string"})

print("--- Исходный тип ---")
print(df["country"].dtype)  # Выведет: string
print(f"Память: {df['country'].memory_usage(deep=True)} байт")

# Переводим в категорию
df["country"] = df["country"].astype("category")

print("\n--- Категориальный тип ---")
print(df["country"].dtype)  # Выведет: category
print(f"Память: {df['country'].memory_usage(deep=True)} байт")