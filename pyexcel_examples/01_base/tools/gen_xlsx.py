import openpyxl


def generate_demo_file(filename: str = "prices.xlsx") -> None:
    # Создаем новую рабочую книгу и выбираем активный лист
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Цены"

    # Тестовые данные (заголовки и несколько строк)
    demo_data = [
        ["Наименование", "Цена", "Количество"],
        ["Смартфон", 45000, 10],
        ["Ноутбук", 95000, 5],
        ["Наушники", 7000, 15],
        ["Монитор", 22000, 8],
        ["Мышь", 2500, 30],
    ]

    # Записываем данные в таблицу
    for row in demo_data:
        ws.append(row)

    # Сохраняем файл
    wb.save(filename)
    print(f"Демо-файл '{filename}' успешно сгенерирован для занятия.")


if __name__ == "__main__":
    generate_demo_file()