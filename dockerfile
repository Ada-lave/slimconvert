FROM python:3.11-slim-buster

COPY . .

# Обновляем пакеты и устанавливаем LibreOffice
RUN apt-get update && apt-get install -y libreoffice --no-install-recommends \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/

# Устанавливаем зависимости Python
RUN pip install --no-cache-dir -r req.txt

CMD ["uvicorn", "slimconvert.server:app", "--host", "0.0.0.0", "--port", "8000"]