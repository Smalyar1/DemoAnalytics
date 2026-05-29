import xlsxwriter

with xlsxwriter.Workbook("charts_demo.xlsx") as workbook:
    ws = workbook.add_worksheet("Аналитика")

    # 1. Данные для вывода
    months = ["Янв", "Фев", "Мар", "Апр", "Май", "Июн"]
    sales = [120000, 145000, 130000, 180000, 210000, 195000]

    # Записываем данные
    ws.write(0, 0, "Месяц")
    ws.write(0, 1, "Выручка")

    for i in range(len(months)):
        ws.write(i + 1, 0, months[i])
        ws.write_number(i + 1, 1, sales[i])

    # 2. УСЛОВНОЕ ФОРМАТИРОВАНИЕ (Тепловая карта для Выручки)
    ws.conditional_format('B2:B7', {
        'type': '2_color_scale',  # Использовать строго '2_color_scale' или '3_color_scale'
        'min_type': 'min',
        'min_color': '#FFFFFF',  # Белый
        'max_type': 'max',
        'max_color': '#63BE7B'  # Зеленый
    })

    # 3. СОЗДАНИЕ И НАСТРОЙКА ГРАФИКА
    chart = workbook.add_chart({'type': 'line'})

    # Добавляем ряд данных
    chart.add_series({
        'name': 'Динамика продаж',
        'categories': '=Аналитика!$A$2:$A$7',  # Ось X
        'values': '=Аналитика!$B$2:$B$7',  # Ось Y
        'line': {'color': '#1F497D', 'width': 2.25}  # Стильный цвет линии
    })

    # Названия осей и графика
    chart.set_title({'name': 'Итоги первого полугодия'})
    chart.set_x_axis({'name': 'Месяцы'})
    chart.set_y_axis({'name': 'Рубли'})

    # Отключаем легенду (так как у нас всего один ряд данных)
    chart.set_legend({'position': 'none'})

    # Вставляем график на лист (с отступом в ячейку D2)
    ws.insert_chart('D2', chart)

print("Отчет с графиком и условным форматированием создан!")