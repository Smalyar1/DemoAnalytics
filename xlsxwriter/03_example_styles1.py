import xlsxwriter

with xlsxwriter.Workbook("styling_demo.xlsx") as workbook:
    ws = workbook.add_worksheet("Выручка")

    # 1. ОПРЕДЕЛЯЕМ СТИЛИ (Глобально для книги)

    # Стиль для шапки таблицы
    header_fmt = workbook.add_format({
        'bold': True,
        'font_color': '#FFFFFF',
        'bg_color': '#366092',
        'border': 1,
        'align': 'center',
        'valign': 'vcenter'
    })

    # Стиль для текстовых данных
    text_fmt = workbook.add_format({
        'font_name': 'Arial',
        'border': 1,
        'align': 'left'
    })

    # Стиль для финансовых показателей (переиспользует сетку + добавляет маску валюты)
    money_fmt = workbook.add_format({
        'font_name': 'Arial',
        'border': 1,
        'num_format': '#,##0.00 ₽',
        'align': 'right'
    })

    # Стиль для финальной строки "Итого"
    total_fmt = workbook.add_format({
        'bold': True,
        'bg_color': '#D9E1F2',
        'border': 6,  # Двойная рамка снизу (классика бухгалтерии)
        'num_format': '#,##0.00 ₽',
        'align': 'right'
    })

    # 2. НАСТРОЙКА СЕТКИ (Устанавливаем высоту строк и ширину колонок)
    ws.set_row(0, 25)  # Делаем шапку повыше
    ws.set_column('A:A', 20)  # Широкая колонка под название товара
    ws.set_column('B:B', 15)  # Под суммы

    # 3. ЗАПИСЬ ДАННЫХ
    ws.write(0, 0, "Товар", header_fmt)
    ws.write(0, 1, "Продажи", header_fmt)

    data = [("Ноутбук", 125000.50), ("Смартфон", 89000.00), ("Монитор", 34500.20)]

    for row_idx, (item, price) in enumerate(data, start=1):
        ws.write(row_idx, 0, item, text_fmt)
        ws.write(row_idx, 1, price, money_fmt)

    # 4. СТРОКА ИТОГО
    total_row = len(data) + 1
    ws.write(total_row, 0, "Всего:", text_fmt)  # Можно применить bold отдельно
    ws.write_formula(total_row, 1, f"=SUM(B2:B{total_row})", total_fmt, "")

print("Красивый отчет создан!")