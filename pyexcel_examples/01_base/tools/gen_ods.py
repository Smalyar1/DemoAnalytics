import pyexcel as pe


def generate_demo_ods(filename: str = "prices.ods") -> None:
    # Тестовые данные те же самые
    demo_data = [
        ["Наименование", "Цена", "Количество"],
        ["Смартфон", 45000, 10],
        ["Ноутбук", 95000, 5],
        ["Наушники", 7000, 15],
        ["Монитор", 22000, 8],
        ["Мышь", 2500, 30],
    ]

    # Запись в ODS одной строчкой (требуется установленный pyexcel-ods3)
    pe.save_as(array=demo_data, dest_file_name=filename)
    print(f"Демо-файл '{filename}' успешно сгенерирован.")


if __name__ == "__main__":
    generate_demo_ods()