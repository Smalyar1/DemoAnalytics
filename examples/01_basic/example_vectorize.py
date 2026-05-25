"""
Примеры использования векторизации в pandas.
Векторизация — это использование встроенных numpy/pandas операций вместо циклов
для значительного повышения производительности.
"""
from __future__ import annotations

import sys
import time

try:
    import pandas as pd
    import numpy as np
except Exception:  # ImportError or other
    print("pandas и numpy не найдены. Установите зависимости: pip install -r requirements.txt")
    sys.exit(1)


def main() -> None:
    # ==================== 1. СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ ====================
    print("=" * 70)
    print("1. СРАВНЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ: цикл vs. векторизация")
    print("=" * 70)

    n = 100_000
    df = pd.DataFrame({"price": np.random.randint(10, 1000, n), "quantity": np.random.randint(1, 100, n)})

    # Способ 1: медленный цикл Python
    start = time.time()
    results_loop = []
    for i in range(len(df)):
        results_loop.append(df.loc[i, "price"] * df.loc[i, "quantity"])
    time_loop = time.time() - start

    # Способ 2: быстрая векторизация
    start = time.time()
    df["total_vectorized"] = df["price"] * df["quantity"]
    time_vectorized = time.time() - start

    print(f"Цикл Python:          {time_loop:.4f} сек")
    print(f"Векторизация pandas:  {time_vectorized:.4f} сек")
    print(f"Ускорение:            {time_loop / time_vectorized:.1f}x\n")

    # ==================== 2. АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ ====================
    print("=" * 70)
    print("2. АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ")
    print("=" * 70)

    df_math = pd.DataFrame({
        "a": [10, 20, 30, 40],
        "b": [2, 5, 3, 8],
        "c": [1.5, 2.5, 3.5, 4.5],
    })

    print("Исходные данные:")
    print(df_math)

    # Простые арифметические операции
    df_math["sum"] = df_math["a"] + df_math["b"]
    df_math["product"] = df_math["a"] * df_math["c"]
    df_math["division"] = df_math["a"] / df_math["b"]
    df_math["power"] = df_math["c"] ** 2

    print("\nПосле арифметических операций:")
    print(df_math)

    # ==================== 3. УСЛОВНЫЕ ОПЕРАЦИИ ====================
    print("\n" + "=" * 70)
    print("3. УСЛОВНЫЕ ОПЕРАЦИИ (np.where и mask)")
    print("=" * 70)

    df_cond = pd.DataFrame({
        "temperature": [15.0, 22.5, 8.0, 19.5, 28.0],
        "humidity": [60, 45, 70, 50, 30],
    })

    print("Исходные данные:")
    print(df_cond)

    # Простое условие с np.where
    df_cond["is_warm"] = np.where(df_cond["temperature"] > 20, "Да", "Нет")

    # Множественные условия
    df_cond["weather"] = np.where(
        df_cond["temperature"] > 25,
        "Ж��рко",
        np.where(df_cond["temperature"] > 15, "Комфортно", "Холодно")
    )

    # Комплексные условия с mask
    mask_wet = df_cond["humidity"] > 50
    df_cond.loc[mask_wet, "condition"] = "Влажно"
    df_cond.loc[~mask_wet, "condition"] = "Сухо"

    print("\nПосле условных операций:")
    print(df_cond)

    # ==================== 4. ПРИМЕНЕНИЕ ФУНКЦИЙ ====================
    print("\n" + "=" * 70)
    print("4. ПРИМЕНЕНИЕ ФУНКЦИЙ: apply() и np.vectorize()")
    print("=" * 70)

    df_func = pd.DataFrame({
        "x": [1, 2, 3, 4, 5],
        "y": [10, 20, 30, 40, 50],
    })

    print("Исходные данные:")
    print(df_func)

    # apply для одной колонки (Series)
    df_func["x_squared"] = df_func["x"].apply(lambda x: x ** 2)

    # apply для строк (axis=1)
    df_func["sum"] = df_func.apply(lambda row: row["x"] + row["y"], axis=1)

    # apply с именованной функцией
    def categorize_y(val):
        return "Низко" if val < 25 else "Средне" if val < 45 else "Высоко"

    df_func["y_category"] = df_func["y"].apply(categorize_y)

    print("\nПосле apply():")
    print(df_func)

    # np.vectorize для пользовательской функции
    def complex_calc(a, b):
        """Сложная функция с логикой"""
        if a > 2:
            return a * b * 1.5
        return a * b

    vec_func = np.vectorize(complex_calc)
    df_func["complex"] = vec_func(df_func["x"], df_func["y"])

    print("\nПосле np.vectorize():")
    print(df_func)

    # ==================== 5. СТРОКОВЫЕ ОПЕРАЦИИ ====================
    print("\n" + "=" * 70)
    print("5. СТРОКОВЫЕ ОПЕРАЦИИ")
    print("=" * 70)

    df_str = pd.DataFrame({
        "name": ["Alice Smith", "Bob Johnson", "Charlie Brown"],
        "email": ["alice@example.com", "bob@example.com", "charlie@example.com"],
    })

    print("Исходные данные:")
    print(df_str)

    # Строковые методы (доступны через .str accessor)
    df_str["first_name"] = df_str["name"].str.split().str[0]
    df_str["last_name"] = df_str["name"].str.split().str[-1]
    df_str["name_upper"] = df_str["name"].str.upper()
    df_str["email_domain"] = df_str["email"].str.split("@").str[1]
    df_str["name_length"] = df_str["name"].str.len()

    print("\nПосле строковых операций:")
    print(df_str)

    # ==================== 6. КОМБИНИРОВАННЫЕ ОПЕРАЦИИ ====================
    print("\n" + "=" * 70)
    print("6. КОМБИНИРОВАННЫЕ ОПЕРАЦИИ")
    print("=" * 70)

    df_combined = pd.DataFrame({
        "product": ["A", "B", "C", "A", "B"],
        "base_price": [100, 200, 150, 100, 200],
        "discount_pct": [10, 5, 20, 0, 15],
        "quantity": [5, 3, 2, 10, 1],
    })

    print("Исходные данные:")
    print(df_combined)

    # Комбинированная векторизованная операция
    df_combined["discounted_price"] = df_combined["base_price"] * (1 - df_combined["discount_pct"] / 100)
    df_combined["total"] = df_combined["discounted_price"] * df_combined["quantity"]
    df_combined["price_tier"] = np.where(
        df_combined["base_price"] < 120,
        "Budget",
        np.where(df_combined["base_price"] < 180, "Standard", "Premium")
    )

    print("\nПосле комбинированных операций:")
    print(df_combined)

    # Агрегация с использованием vectorized операций
    summary = df_combined.groupby("product").agg(
        avg_price=("base_price", "mean"),
        total_quantity=("quantity", "sum"),
        total_revenue=("total", "sum"),
    )
    print("\nСводная таблица по продуктам:")
    print(summary)

    # ==================== 7. РАБОТА С ВРЕМЕННЫМИ РЯДАМИ ====================
    print("\n" + "=" * 70)
    print("7. РАБОТА С ВРЕМЕННЫМИ РЯДАМИ (datetime операции)")
    print("=" * 70)

    df_time = pd.DataFrame({
        "date": pd.date_range("2024-01-01", periods=5),
        "value": [100, 110, 105, 120, 115],
    })

    print("Исходные данные:")
    print(df_time)

    # Временные операции векторизованы
    df_time["month"] = df_time["date"].dt.month
    df_time["day_of_week"] = df_time["date"].dt.day_name()
    df_time["is_weekend"] = df_time["date"].dt.dayofweek >= 5
    df_time["change"] = df_time["value"].diff()
    df_time["ma3"] = df_time["value"].rolling(window=3).mean()  # скользящее среднее

    print("\nПосле операций со временем:")
    print(df_time)

    print("\n" + "=" * 70)
    print("Все примеры выполнены успешно!")
    print("=" * 70)


if __name__ == "__main__":
    main()

