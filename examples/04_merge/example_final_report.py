"""
Вы работаете аналитиком в международной торговой компании.
От руководства поступила задача: составить отчет по крупным продажам (транзакции на сумму строго больше 3000$).
В итоговом отчете босс хочет видеть общую выручку и количество таких сделок по каждой стране,
а также имя конкретного регионального менеджера, который за эту страну отвечает.
Результат должен быть отсортирован по убыванию выручки.
"""

import pandas as pd

# 0. Исходные данные (создаем датафреймы из словарей)
sales_data = {
    "order_id": [1001, 1002, 1003, 1004, 1005, 1006],
    "country": ["USA", "China", "Korea", "UK", "China", "Japan"],
    "price": [1200, 45000, 8200, 2900, 39000, 11900]
}
df = pd.DataFrame(sales_data)

df_managers = pd.DataFrame({
    "country": ["USA", "China", "Korea", "Germany"],
    "manager": ["Alice", "Bob", "Charlie", "Hans"]
})

# 2. Быстрая фильтрация крупного опта (цена > 3000)
filtered_df = df.query("price > 3000")

# 3. Группировка: считаем общую выручку по странам
country_report = filtered_df.groupby("country").agg(
    total_revenue=("price", "sum"),
    orders_count=("order_id", "count")
).reset_index()

# 4. Обогащение данных информацией о менеджерах
# Для Japan менеджера нет, поэтому подставится None
final_report = pd.merge(country_report, df_managers, on="country", how="left")

# 5. Сортировка по выручке
final_report = final_report.sort_values(by="total_revenue", ascending=False)

print(final_report)