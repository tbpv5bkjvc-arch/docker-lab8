import os
import sys
import pandas as pd

data_file = os.getenv("DATA_FILE", "data/sales.csv")
group_by = sys.argv[1] if len(sys.argv) > 1 else "city"

df = pd.read_csv(data_file)
print(f"Файл: {data_file}, строк: {len(df)}")
print(f"Выручка по столбцу «{group_by}»:")

report = (
    df.groupby(group_by)["amount"]
    .agg(count="count", sum="sum", mean="mean")
    .sort_values("sum", ascending=False)
)
report["mean"] = report["mean"].round(2)
print(report.to_string())
