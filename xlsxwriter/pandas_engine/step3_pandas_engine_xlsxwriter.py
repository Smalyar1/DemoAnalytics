import pandas as pd

# 1. Готовим данные
data = {
    "Сотрудник": ["Александр Иванов", "Мария Сидорова", "Дмитрий Петров", "Елена Кузнецова", "Игорь Федоров"],
    "Дата найма": ["2024-01-15", "2023-05-20", "2025-11-01", "2022-08-12", "2026-02-10"],
    "Выручка, ₽": [1550000.75, 980000.00, 2300000.50, 4120000.00, 850000.25],
    "Выполнение плана": [0.92, 1.05, 0.88, 1.12, 0.75]
}
df = pd.DataFrame(data)
df["Дата найма"] = pd.to_datetime(df["Дата найма"])

# 2. Запись через контекстный менеджер (Движок XlsxWriter)
with pd.ExcelWriter("pandas_styled_pro.xlsx", engine="xlsxwriter") as writer:
    sheet_name = "KPI_Продажи"

    # Выгружаем данные БЕЗ стандартной шапки Pandas (header=False),
    # чтобы полностью нарисовать свои красивые заголовки с нуля в XlsxWriter.
    # Данные сдвигаем на одну строку вниз (startrow=1)
    df.to_excel(writer, sheet_name=sheet_name, index=False, header=False, startrow=1)

    workbook = writer.book
    worksheet = writer.sheets[sheet_name]

    # ==========================================
    # 3. СОЗДАНИЕ СТИЛЬНОЙ ПАЛИТРЫ (ТЕМНО-СИНИЙ АКЦЕНТ)
    # ==========================================

    # Новая стильная шапка: темно-синий фон, белый текст, без унылых черных рамок
    header_fmt = workbook.add_format({
        'bold': True,
        'font_name': 'Segoe UI',
        'font_size': 11,
        'font_color': '#FFFFFF',
        'bg_color': '#1F497D',
        'align': 'center',
        'valign': 'vcenter',
        'bottom': 2,  # Толстая линия снизу шапки
        'bottom_color': '#163356'
    })

    # Обычная строка (белый фон)
    row_fmt = workbook.add_format({
        'font_name': 'Segoe UI',
        'font_size': 10,
        'bottom': 1,
        'bottom_color': '#E0E0E0'  # Легкая серая линия-разделитель вместо черной сетки
    })

    # Чередующаяся строка (светло-серый фон для "зебры")
    zebra_fmt = workbook.add_format({
        'font_name': 'Segoe UI',
        'font_size': 10,
        'bg_color': '#F9FBFD',
        'bottom': 1,
        'bottom_color': '#E0E0E0'
    })

    # Специализированные маски отображения данных
    # Обратите внимание: мы создаем их ДВАЖДЫ — для обычных строк и для строк-зебр
    formats = {
        'date': {
            'plain': workbook.add_format({'num_format': 'yyyy-mm-dd', 'align': 'center'}),
            'zebra': workbook.add_format({'num_format': 'yyyy-mm-dd', 'align': 'center', 'bg_color': '#F9FBFD'})
        },
        'money': {
            'plain': workbook.add_format({'num_format': '#,##0.00 ₽', 'align': 'right'}),
            'zebra': workbook.add_format({'num_format': '#,##0.00 ₽', 'align': 'right', 'bg_color': '#F9FBFD'})
        },
        'percent': {
            'plain': workbook.add_format({'num_format': '0.0%', 'align': 'right'}),
            'zebra': workbook.add_format({'num_format': '0.0%', 'align': 'right', 'bg_color': '#F9FBFD'})
        }
    }

    # Добавляем базовые свойства границ ко всем маскам
    for group in formats.values():
        for fmt in group.values():
            fmt.set_font_name('Segoe UI')
            fmt.set_font_size(10)
            fmt.set_bottom(1)
            fmt.set_bottom_color('#E0E0E0')

    # ==========================================
    # 4. РУЧНАЯ ЗАПИСЬ КРАСИВОЙ ШАПКИ
    # ==========================================
    worksheet.set_row(0, 28)  # Делаем заголовок повыше и просторнее
    for col_idx, col_name in enumerate(df.columns):
        worksheet.write(0, col_idx, col_name, header_fmt)

    # ==========================================
    # 5. СТИЛИЗАЦИЯ СТРОК И АВТОПОДБОР ШИРИНЫ (КОЛОНКА С ДАТАМИ БУДЕТ ИДЕАЛЬНОЙ)
    # ==========================================

    # Проходим по строкам данных для наложения "зебры" и масок
    for row_idx in range(1, len(df) + 1):
        worksheet.set_row(row_idx, 20)  # Чуть увеличиваем высоту строк данных для «воздуха»
        style_type = 'zebra' if row_idx % 2 == 0 else 'plain'

        # Применяем точечные форматы к каждой ячейке строки
        worksheet.write(row_idx, 0, df.iloc[row_idx - 1, 0], zebra_fmt if style_type == 'zebra' else row_fmt)
        worksheet.write_datetime(row_idx, 1, df.iloc[row_idx - 1, 1], formats['date'][style_type])
        worksheet.write_number(row_idx, 2, float(df.iloc[row_idx - 1, 2]), formats['money'][style_type])
        worksheet.write_number(row_idx, 3, float(df.iloc[row_idx - 1, 3]), formats['percent'][style_type])

    # Умный расчет ширины колонок с учетом длины заголовков и данных
    for col_idx, col_name in enumerate(df.columns):
        # Для дат берем длину отформатированной строки (10 символов для yyyy-mm-dd), а не длину таймстемпа Pandas
        if col_idx == 1:
            max_len = 10
        else:
            max_len = df[col_name].astype(str).map(len).max()

        # Учитываем также длину названия самой колонки
        max_len = max(max_len, len(col_name))

        # Задаем ширину с комфортным запасом (+4 символа)
        worksheet.set_column(col_idx, col_idx, max_len + 4)

    # Включаем фильтры и аккуратную сетку
    worksheet.autofilter(0, 0, len(df), len(df.columns) - 1)
    worksheet.hide_gridlines(2)

print("Эстетичный бизнес-отчет успешно создан!")