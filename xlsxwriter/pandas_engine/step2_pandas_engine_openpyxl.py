import pandas as pd

# 1. Исходные данные
data = {
    "Сотрудник": ["Александр Иванов", "Мария Сидорова", "Дмитрий Петров"],
    "Дата найма": ["2024-01-15", "2023-05-20", "2025-11-01"],
    "Выручка, ₽": [1550000.75, 980000.00, 2300000.50],
    "Выполнение плана": [0.92, 1.05, 0.88]
}
df = pd.DataFrame(data)
df["Дата найма"] = pd.to_datetime(df["Дата найма"])

# Форматируем дату в строку (как в вашем примере)
df_ready = df.copy()
df_ready["Дата найма"] = df_ready["Дата найма"].dt.strftime("%Y-%m-%d")

# ==========================================
# 2. ЗАПИСЬ ЧЕРЕЗ EXCELWRITER БЕЗ TO_EXCEL
# ==========================================
with pd.ExcelWriter("pandas_to_excel.xlsx", engine="openpyxl") as writer:
    # Создаем пустой лист в книге силами openpyxl
    workbook = writer.book
    worksheet = workbook.create_sheet(title="KPI_Продажи")

    # Так как мы создали лист вручную, удаляем дефолтный пустой лист ExcelWriter'а,
    # чтобы в итоговом файле не плодились лишние вкладки
    if "Sheet" in workbook.sheetnames:
        workbook.remove(workbook["Sheet"])

    # А) Записываем заголовки (названия колонок DataFrame)
    # Помним, что в openpyxl координаты начинаются с 1
    for col_idx, col_name in enumerate(df_ready.columns, start=1):
        worksheet.cell(row=1, column=col_idx, value=col_name)

    # Б) Построчно переносим данные из DataFrame
    # iterrows() возвращает (индекс, строка_данных)
    for row_idx, (index, row_data) in enumerate(df_ready.iterrows(), start=2):
        for col_idx, value in enumerate(row_data, start=1):
            worksheet.cell(row=row_idx, column=col_idx, value=value)

print("Файл успешно собран вручную и сохранен!")