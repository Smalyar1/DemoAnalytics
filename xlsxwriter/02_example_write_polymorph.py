import datetime
import xlsxwriter

# Создаем книгу и лист
with xlsxwriter.Workbook("write_methods_demo.xlsx") as workbook:
    worksheet = workbook.add_worksheet("Специфика write")

    # Подготовим форматы для наглядности
    header_fmt = workbook.add_format({'bold': True, 'bg_color': '#D3D3D3', 'border': 1})
    date_fmt = workbook.add_format({'num_format': 'yyyy-mm-dd'})
    url_fmt = workbook.add_format({'font_color': 'blue', 'underline': True})

    # Настраиваем ширину колонок для читаемости
    worksheet.set_column("A:D", 25)

    # Шапка таблицы
    headers = ["Что пишем", "Через универсальный write()", "Через явный write_*()", "В чем разница / Особенность"]
    for col_idx, header in enumerate(headers):
        worksheet.write(0, col_idx, header, header_fmt)

    # --- КЕЙС 1: Число как текст (Проблема "Зеленых треугольников" в Excel) ---
    row = 1
    worksheet.write(row, 0, "Числовой код (ID или ИНН)")

    # Универсальный write() видит строку и запишет её как ТЕКСТ. В Excel появится предупреждение.
    worksheet.write(row, 1, "004523")

    # Явный write_number() принудительно превратит строку в число (ведущие нули пропадут, зато можно считать сумму)
    try:
        worksheet.write_number(row, 2, "004523")  # Передаем строку, но пишем как число
    except TypeError:
        worksheet.write(row, 2, int("004523"))

    worksheet.write(row, 3, "write() сохраняет строку. write_number() конвертирует в число.")

    # --- КЕЙС 2: Даты ---
    row = 2
    worksheet.write(row, 0, "Дата (datetime)")
    dt = datetime.date(2026, 5, 29)

    # Универсальный write() распознает объект даты, но запишет его без формата (Excel покажет число вроде 46171)
    worksheet.write(row, 1, dt)

    # Явный write_datetime() позволяет сразу применить маску отображения даты
    worksheet.write_datetime(row, 2, dt, date_fmt)
    worksheet.write(row, 3, "write() выведет сырое число Excel. write_datetime() + формат дадут красивую дату.")

    # --- КЕЙС 3: Ссылки (URLs) ---
    row = 3
    worksheet.write(row, 0, "Гиперссылка")
    url = "https://python.org"

    # Универсальный write() распознает регулярное выражение URL и сделает его кликабельным автоматически
    worksheet.write(row, 1, url)

    # Явный write_url() позволяет изменить отображаемый текст ссылки (экранный текст вместо сырого URL)
    worksheet.write_url(row, 2, url, string="Официальный сайт Python", cell_format=url_fmt)
    worksheet.write(row, 3, "write() пишет сырой URL. write_url() позволяет задать красивый текст (anchor text).")

    # --- КЕЙС 4: Формулы ---
    row = 4
    worksheet.write(row, 0, "Формула")

    # Запишем пару чисел для теста формулы ниже
    worksheet.write("B6", 10)
    worksheet.write("C6", 20)

    # Универсальный write() проверяет, начинается ли строка с '='. Если да — пишет как формулу.
    worksheet.write(row, 1, "=B6*2")
    # официальный хак от автора XlsxWriter специально для LibreOffice, который не всегда корректно обрабатывает формулы, начинающиеся с '='
    # TODO: worksheet.write(row, 1, "=B6*2", None, "")

    # Явный write_formula() полезен, когда формула собирается динамически и нужно гарантировать её тип
    worksheet.write_formula(row, 2, "=C6*2")
    # TODO: worksheet.write(row, 2, "=C6*2", None, "")
    worksheet.write(row, 3, "write() делает проверку на знак '='. write_formula() работает быстрее в циклах.")

    # --- КЕЙС 5: Пустые ячейки (Бланки) ---
    row = 6
    worksheet.write(row, 0, "Пустая ячейка со стилем")

    # Передача None в универсальный write() просто ничего не запишет (стиль проигнорируется)
    worksheet.write(row, 1, None, header_fmt)

    # write_blank() создает пустую ячейку, но применяет к ней стиль (например, серый фон или границы)
    worksheet.write_blank(row, 2, None, header_fmt)
    worksheet.write(row, 3, "write(None) пропускает ячейку. write_blank() красит её, оставляя пустой.")

print("Демонстрационный файл 'write_methods_demo.xlsx' успешно создан!")