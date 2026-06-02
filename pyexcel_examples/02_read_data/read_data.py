import pyexcel as pe

# Читаем файл в виде списка списков
data: list[list[str | int]] = pe.get_array(file_name="prices.xlsx")

print(data)

# Читаем таблицу как словарь колонок
data_dict: dict[str, list[str | int]] = pe.get_dict(
    file_name="prices.xlsx", name_columns_by_row=0
)
print(data_dict)


# Получаем список строк-записей
records: list[dict[str, str | int]] = pe.get_records(file_name="prices.xlsx")

print(records)

