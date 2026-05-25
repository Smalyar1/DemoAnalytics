import pandas as pd

# Создаем датафрейм на 1 миллион строк с повторяющимися странами
countries = ["Россия", "Китай", "Корея"] * 333333
df = pd.DataFrame({"country": countries})

# Замеряем память до оптимизации
mem_before = df["country"].memory_usage(deep=True)

# Переводим в категориальный тип
df["country"] = df["country"].astype("category")

# Замеряем память после
mem_after = df["country"].memory_usage(deep=True)

print(f"Память ДО:   {mem_before / 1024 / 1024:.2f} Мб")
print(f"Память ПОСЛЕ: {mem_after / 1024 / 1024:.2f} Мб")