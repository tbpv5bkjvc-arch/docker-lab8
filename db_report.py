import os
import pandas as pd
from sqlalchemy import create_engine

url = os.getenv("DATABASE_URL", "postgresql+psycopg2://postgres:student123@db:5432/postgres")
engine = create_engine(url)

query = """
SELECT product, count(*) AS sales, sum(amount) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
"""
print(pd.read_sql(query, engine).to_string(index=False))
