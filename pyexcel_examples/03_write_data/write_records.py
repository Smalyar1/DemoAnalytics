import pyexcel as pe

records = [
    {"Товар": "Клавиатура", "Цена": 5000},
    {"Товар": "Коврик", "Цена": 1200},
]

# Указываем аргумент records вместо array
pe.save_as(records=records, dest_file_name="hardware.ods")

