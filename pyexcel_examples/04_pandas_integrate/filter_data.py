import pyexcel as pe

# Читаем только первые 3 товара, пропуская шапку (если start_row=1)
# Или берем конкретный кусок данных:
sampled_data = pe.get_array(
    file_name="prices.xlsx",
    start_row=1,  # Пропускаем строку заголовков (индекс 0)
    row_limit=3,  # Берем только 3 строки данных
    start_column=0,
    column_limit=2,  # Берем только первые две колонки (Наименование и Цена)
)

print(sampled_data)