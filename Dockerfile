FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
ENV DATA_FILE=/data/sales.csv
ENTRYPOINT ["python", "report.py"]
CMD ["city"]
