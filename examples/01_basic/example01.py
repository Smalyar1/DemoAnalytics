"""
example01.py

Короткая демонстрация основных приёмов работы с pandas.

Запуск:
  python3 example01.py

Если pandas не установлен, скрипт попросит установить зависимости из requirements.txt.
"""
from __future__ import annotations

import sys

try:
    import pandas as pd
except Exception:  # ImportError or other
    print("pandas не найден. Установите зависимости: pip install -r requirements.txt")
    sys.exit(1)


def main() -> None:
    print("=== Демонстрация pandas: создание DataFrame ===")
    data = {
        "city": ["Berlin", "Paris", "Berlin", "Paris", "Madrid"],
        "year": [2020, 2020, 2021, 2021, 2021],
        "temperature": [15.0, 17.5, 16.0, 18.0, 20.0],
        "rain_mm": [50, 40, 55, 35, 10],
    }

    df = pd.DataFrame(data)
    print(df)

    print("\n=== Информация и статистика ===")
    print(df.info())
    print(df.describe())

    print("\n=== Выборки и фильтрация ===")
    berlin = df[df["city"] == "Berlin"]
    print("Данные по Берлину:\n", berlin)

    recent = df[df["year"] >= 2021]
    print("\nГоды 2021+:\n", recent)

    print("\n=== Добавление столбца и агрегирование ===")
    df["temp_f"] = df["temperature"] * 9 / 5 + 32
    print(df)

    grouped = df.groupby(["city"]).agg(
        avg_temp=("temperature", "mean"), total_rain=("rain_mm", "sum"), cnt=("year", "size")
    )
    print("\nАгрегированные по городам:\n", grouped)

    print("\n=== Сортировка ===")
    print(df.sort_values(["year", "city"], ascending=[False, True]))

    print("\n=== Слияние (04_merge) ===")
    extra = pd.DataFrame({"city": ["Berlin", "Madrid"], "population_millions": [3.6, 3.2]})
    merged = df.merge(extra, on="city", how="left")
    print(merged)

    print("\n=== Pivot (сводная таблица) ===")
    pivot = pd.pivot_table(df, index="city", columns="year", values="temperature", aggfunc="mean")
    print(pivot)

    print("\n=== Работа с датами ===")
    df_dates = pd.DataFrame({"date": ["2021-01-01", "2021-06-15", "2022-03-20"], "value": [1, 2, 3]})
    df_dates["date"] = pd.to_datetime(df_dates["date"])  # преобразование типов
    print(df_dates)

    print("\n=== Запись/чтение CSV ===")
    out_file = "demo_output.csv"
    df.to_csv(out_file, index=False)
    print(f"Записал {out_file}")

    df2 = pd.read_csv(out_file)
    print("Прочитано обратно из CSV:\n", df2.head())


if __name__ == "__main__":
    main()

