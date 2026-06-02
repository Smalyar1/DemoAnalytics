import pyexcel as pe

matrix = [
    ["Категория", "Товар", "Цена"],
    ["Электроника", "Наушники", 7000],
    ["Электроника", "Мышь", 2500],
]

# Просто передаем массив и имя целевого файла
pe.save_as(array=matrix, dest_file_name="simple_report.xlsx")