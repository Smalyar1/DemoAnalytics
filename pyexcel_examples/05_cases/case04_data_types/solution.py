import csv
from datetime import datetime, date
from typing import TypedDict


class CleanRow(TypedDict):
    name: str
    age: int
    salary: float
    date: date
    active: bool
    percentage: float


def parse_salary(raw_data: str) -> float:
    """Удаляет пробелы-разделители тысяч (например, '50 000.5' -> 50000.5)"""
    clean = raw_data.replace(" ", "").strip()
    return float(clean)


def parse_date(raw_data: str) -> date:
    """Перебирает известные маски дат"""
    formats = [
        "%Y-%m-%d",  # 2020-01-15 (ISO)
        "%d.%m.%Y",  # 15.04.2018 (РФ/Европа)
        "%m/%d/%Y",  # 04/20/2017 (США)
    ]
    clean_data = raw_data.strip()
    for fmt in formats:
        try:
            return datetime.strptime(clean_data, fmt).date()
        except ValueError:
            continue

    raise ValueError(f"date format '{clean_data}' is not supported.")


def parse_active(val: str) -> bool:
    """Приводит регистр к единому стандарту булевых значений"""
    return val.strip().upper() == "TRUE"


def process_dirty_csv(file_path: str) -> list[CleanRow]:
    cleaned_data: list[CleanRow] = []

    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        for idx, row in enumerate(reader, start=2):
            try:
                clean_row: CleanRow = {
                    "name": row["Name"].strip(),
                    "age": int(row["Age"].strip()),
                    "salary": parse_salary(row["Salary"]),
                    "date": parse_date(row["Date"]),
                    "active": parse_active(row["Active"]),
                    "percentage": float(row["Percentage"])
                }
                cleaned_data.append(clean_row)

            except (ValueError, KeyError) as e:
                print(f"Parse error at line {idx}: {e}. Line skipped.")
                continue

    return cleaned_data


if __name__ == "__main__":
    result = process_dirty_csv("sample.csv")
    print(result)

    # for item in result:
    #     print(
    #         f"Имя: {item['name']:<8} | "
    #         f"ЗП: {item['salary']:<9} | "
    #         f"Дата: {item['date'].isoformat()} | "
    #         f"Статус: {str(item['active']):<5} | "
    #         f"Доля: {item['percentage']}"
    #     )
