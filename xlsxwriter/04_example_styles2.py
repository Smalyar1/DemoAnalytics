import datetime
import random
import xlsxwriter

# Имитируем большой датасет (100 000 транзакций)
# В реальной жизни эти данные пришли бы из базы данных или Pandas
TOTAL_ROWS = 100_000

print("Старт генерации объемного отчета...")

with xlsxwriter.Workbook("huge_styled_report.xlsx", {'constant_memory': True}) as workbook:
    ws = workbook.add_worksheet("Лог транзакций")

    # ==========================================
    # 1. ОБЪЯВЛЕНИЕ СТИЛЕЙ (СТРОГО ДО ЦИКЛА!)
    # ==========================================

    # Шапка таблицы
    header_fmt = workbook.add_format({
        'bold': True,
        'font_name': 'Segoe UI',
        'font_size': 11,
        'font_color': '#FFFFFF',
        'bg_color': '#1F4E79',
        'align': 'center',
        'border': 1
    })

    # Текстовые идентификаторы (ID транзакции, маскированный номер карты)
    code_fmt = workbook.add_format({
        'font_name': 'Courier New',  # Моноширинный шрифт идеален для ID и карт
        'font_size': 10,
        'align': 'center',
        'border': 1,
        'bg_color': '#FAFAFA'
    })

    # Категории (обычный текст)
    text_fmt = workbook.add_format({
        'font_name': 'Segoe UI',
        'font_size': 10,
        'align': 'left',
        'border': 1
    })

    # Формат Даты и Времени (Важно: Excel требует маску yyyy-mm-dd hh:mm:ss)
    datetime_fmt = workbook.add_format({
        'font_name': 'Segoe UI',
        'font_size': 10,
        'num_format': 'yyyy-mm-dd hh:mm:ss',
        'align': 'center',
        'border': 1
    })

    # Финансовый формат (Денежный с разделителями тысяч и копейками)
    money_fmt = workbook.add_format({
        'font_name': 'Segoe UI',
        'font_size': 10,
        'num_format': '#,##0.00 ₽',
        'align': 'right',
        'border': 1
    })

    # Кешбэк (Процентный формат)
    percent_fmt = workbook.add_format({
        'font_name': 'Segoe UI',
        'font_size': 10,
        'num_format': '0.0%',
        'align': 'right',
        'border': 1
    })

    # ==========================================
    # 2. НАСТРОЙКА СЕТКИ
    # ==========================================
    ws.set_row(0, 24)  # Высота шапки
    ws.set_column('A:A', 15)  # ID
    ws.set_column('B:B', 22)  # Дата и время
    ws.set_column('C:C', 20)  # Карта
    ws.set_column('D:D', 25)  # Категория
    ws.set_column('E:E', 18)  # Сумма
    ws.set_column('F:F', 12)  # % Кешбэка

    # ==========================================
    # 3. ЗАПИСЬ ШАПКИ
    # ==========================================
    headers = ["ID Транзакции", "Дата и Время", "Номер карты", "Категория расходов", "Сумма операции", "Кешбэк"]
    for col_idx, header in enumerate(headers):
        ws.write(0, col_idx, header, header_fmt)

    # ==========================================
    # 4. ЗАПИСЬ БОЛЬШОГО ОБЪЕМА ДАННЫХ В ЦИКЛЕ
    # ==========================================
    categories = ["Супермаркеты", "Автозаправки", "Рестораны и кафе", "Одежда и обувь", "Аптеки", "Такси"]
    base_date = datetime.datetime(2026, 1, 1, 0, 0, 0)

    # Используем write_* методы для максимальной скорости в цикле
    for i in range(1, TOTAL_ROWS + 1):
        # Имитируем случайные, но реалистичные данные
        tx_id = f"TX-{1000000 + i}"
        tx_date = base_date + datetime.timedelta(minutes=i * 5, seconds=random.randint(0, 59))
        card_num = f"4276 **** **** {random.randint(1000, 9999)}"
        category = random.choice(categories)
        amount = round(random.uniform(50.0, 75000.0), 2)
        cashback_rate = random.choice([0.01, 0.02, 0.05, 0.10])

        # Записываем строго по типам с применением созданных форматов
        ws.write_string(i, 0, tx_id, code_fmt)
        ws.write_datetime(i, 1, tx_date, datetime_fmt)
        ws.write_string(i, 2, card_num, code_fmt)
        ws.write_string(i, 3, category, text_fmt)
        ws.write_number(i, 4, amount, money_fmt)
        ws.write_number(i, 5, cashback_rate, percent_fmt)

        # Выводим прогресс каждые 25 000 строк, чтобы студенты видели триггер работы
        if i % 25000 == 0:
            print(f"Записано {i} строк...")

print("Файл успешно сформирован и сохранен!")