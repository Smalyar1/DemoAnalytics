import xlsxwriter

# 1. Создаем книгу (Workbook). Файл создастся в текущей папке.
with xlsxwriter.Workbook("hello_world.xlsx") as workbook:
    # 2. Добавляем лист (Worksheet). По умолчанию имя будет "Sheet1", но мы зададим свое.
    worksheet = workbook.add_worksheet("Тестовый лист")

    # 3. Пишем данные в ячейку A1 (строка 0, колонка 0)
    worksheet.write("A1", "Привет, XlsxWriter!")

    # 4. Пишем данные, используя индексы (строка 1, колонка 0 -> это ячейка A2)
    worksheet.write(1, 0, "Работает на Python 3.12+")