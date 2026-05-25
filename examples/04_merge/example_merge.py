import pandas as pd

# 1. Левая таблица: данные о продажах
sales_data = {
    "order_id": [101, 102, 103, 104],
    "country": ["USA", "China", "Korea", "UK"],
    "price": [1200, 45000, 8200, 3100]
}
df_sales = pd.DataFrame(sales_data)

# 2. Правая таблица: справочник менеджеров
managers_data = {
    "country": ["USA", "China", "Korea", "Germany"],
    "manager": ["Alice", "Bob", "Charlie", "Hans"]
}
df_managers = pd.DataFrame(managers_data)

# 3. Демонстрация Inner Join (пересечение)
# UK и Germany пропадут, так как их нет в обеих таблицах одновременно
inner_res = pd.merge(df_sales, df_managers, on="country", how="inner")
print("--- Результат INNER JOIN ---")
print(inner_res)

# 4. Демонстрация Left Join (сохранение левой таблицы)
# UK останется, а в поле manager запишется None/NaN
left_res = pd.merge(df_sales, df_managers, on="country", how="left")
print("\n--- Результат LEFT JOIN ---")
print(left_res)