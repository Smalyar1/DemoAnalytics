from ooodev.calc import CalcDoc
from ooodev.utils.lo import Lo
from ooodev.format.calc.direct.cell.font import Font
from ooodev.format.calc.direct.cell.background import Color as BgColor
from ooodev.format.calc.direct.cell.borders import Borders, Side
from ooodev.format.calc.direct.cell.numbers import Numbers
from ooodev.format.calc.direct.cell.alignment import HoriAlignKind, VertAlignKind, TextAlign
from ooodev.utils.color import StandardColor, Color
import os


def create_sales_report():
    """Создание отчета о продажах."""

    with Lo.Loader(connector=Lo.ConnectPipe()):
        # 1. Создаем новый документ Calc
        doc = CalcDoc.create_doc()
        sheet = doc.get_active_sheet()

        # --- Исходные данные ---
        headers = ["Товар", "Количество", "Цена", "Сумма"]
        products = [
            ["Ноутбук", 5, 1200.0],
            ["Мышь", 20, 25.5],
            ["Клавиатура", 15, 45.0],
            ["Монитор", 8, 300.0],
            ["Принтер", 4, 150.0],
        ]

        # Добавляем столбец "Сумма"
        data = []
        total = 0
        for row in products:
            amount = row[1] * row[2]
            data.append([row[0], row[1], row[2], amount])
            total += amount

        # --- Запись данных ---
        sheet.get_range(range_name="A1:D1").set_array([headers])
        sheet.get_range(range_name="A2:D6").set_array(data)
        sheet.get_range(range_name="A7:D7").set_array([["ИТОГО", "", "", total]])
        sheet.get_range(range_name="A7:C7").merge_cells()

        # --- Стилизация ---
        # Создаем Side объект для тонкой серой линии
        thin_side = Side(color=StandardColor.GRAY_DARK2, width=2)

        # Создаем границы через fmt_border_side
        border_all = Borders().fmt_border_side(thin_side)

        # Стиль заголовков
        header_style = [
            Font(size=12, b=True, color=StandardColor.WHITE),
            BgColor(color=Color(0x2F5496)),
            TextAlign(hori_align=HoriAlignKind.CENTER, vert_align=VertAlignKind.MIDDLE),
            border_all,
        ]
        sheet.get_range(range_name="A1:D1").apply_styles(*header_style)

        # Базовый стиль данных
        data_style = [
            Font(size=11),
            BgColor(color=Color(0xF2F2F2)),
            TextAlign(vert_align=VertAlignKind.MIDDLE),
            border_all,
        ]
        sheet.get_range(range_name="A2:D6").apply_styles(*data_style)

        # Товар - влево
        sheet.get_range(range_name="A2:A6").apply_styles(
            TextAlign(hori_align=HoriAlignKind.LEFT, vert_align=VertAlignKind.MIDDLE)
        )

        # Количество - целое число, центр
        sheet.get_range(range_name="B2:B6").apply_styles(
            Numbers(num_format_index=1),
            TextAlign(hori_align=HoriAlignKind.CENTER, vert_align=VertAlignKind.MIDDLE)
        )

        # Цена - валюта, центр
        sheet.get_range(range_name="C2:C6").apply_styles(
            Numbers(num_format_index=12),
            TextAlign(hori_align=HoriAlignKind.CENTER, vert_align=VertAlignKind.MIDDLE)
        )

        # Сумма - валюта, вправо
        sheet.get_range(range_name="D2:D6").apply_styles(
            Numbers(num_format_index=12),
            TextAlign(hori_align=HoriAlignKind.RIGHT, vert_align=VertAlignKind.MIDDLE)
        )

        # Стиль итоговой строки
        total_style = [
            Font(size=12, b=True, color=StandardColor.WHITE),
            BgColor(color=Color(0x404040)),
            TextAlign(hori_align=HoriAlignKind.CENTER, vert_align=VertAlignKind.MIDDLE),
            border_all,
        ]
        sheet.get_range(range_name="A7:D7").apply_styles(*total_style)

        # Итоговая сумма - вправо + валюта
        sheet.get_range(range_name="D7").apply_styles(
            Numbers(num_format_index=12),
            TextAlign(hori_align=HoriAlignKind.RIGHT, vert_align=VertAlignKind.MIDDLE)
        )

        sheet.set_sheet_name("Отчет о продажах")

        # Автоподбор ширины столбцов
        columns = sheet.component.getColumns()
        for i in range(4):  # столбцы A(0), B(1), C(2), D(3)
            column = columns.getByIndex(i)
            column.OptimalWidth = True

        doc.save_doc("sales_report.ods")


if __name__ == "__main__":
    create_sales_report()
