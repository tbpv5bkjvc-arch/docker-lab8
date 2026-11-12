# Лабораторная работа №8: Dockerfile — собственный образ

## Сборка образа
```bash
docker build -t report:3.2 .
```

## Запуск отчёта по CSV-файлу
По городам (по умолчанию):
```bash
docker run --rm -v "$(pwd)/data:/data" report:3.2
```

По товарам с указанием собственного файла:
```bash
docker run --rm -v "$(pwd)/data:/data" -e DATA_FILE=/data/my_sales.csv report:3.2 product
```

## Запуск отчёта из PostgreSQL
1. Создайте сеть и запустите контейнер БД:
```bash
docker network create labnet
docker run -d --name warehouse --network labnet -e POSTGRES_PASSWORD=student123 postgres:17
```

2. После создания и наполнения таблицы `sales` запустите отчёт:
```bash
docker run --rm --network labnet \
  -e DATABASE_URL="postgresql+psycopg2://postgres:student123@warehouse:5432/postgres" \
  --entrypoint python report:3.2 db_report.py
```
