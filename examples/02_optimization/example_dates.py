import pandas as pd

df_dates = pd.DataFrame({"raw_date": ["2026-05-01", "2026-05-02", "2026-06-15"]})
df_dates.info()
print("\n--- Преобразование в datetime ---")
df_dates["clean_date"] = pd.to_datetime(df_dates["raw_date"])
df_dates.info()

df_dates["month"] = df_dates["clean_date"].dt.month
df_dates["day_name"] = df_dates["clean_date"].dt.day_name()
df_dates["is_weekend"] = df_dates["clean_date"].dt.weekday >= 5

print(df_dates)