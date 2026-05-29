# 0. Запустите текущий код

# 1.Удалим библиотеки openpyxl и xlsxwriter, оставим только pandas
# uv remove xlsxwriter
# uv remove openpyxl

# 2. Пробуем запустить текущий код
import pandas as pd
from pandas.compat._optional import import_optional_dependency

data = {
    "Сотрудник": ["Александр Иванов", "Мария Сидорова", "Дмитрий Петров"],
    "Дата найма": ["2024-01-15", "2023-05-20", "2025-11-01"],
    "Выручка, ₽": [1550000.75, 980000.00, 2300000.50],
    "Выполнение плана": [0.92, 1.05, 0.88]
}
df = pd.DataFrame(data)
df["Дата найма"] = pd.to_datetime(df["Дата найма"])

df_ready = df.copy()
df_ready["Дата найма"] = df_ready["Дата найма"].dt.strftime("%Y-%m-%d")

# Сохраняем обычный DataFrame
df_ready.to_excel("pandas_native_clean.xlsx", sheet_name="KPI_Продажи", index=False)

# 3.Вернем библиотеки openpyxl и xlsxwriter
# uv add xlsxwriter
# uv add openpyxl
