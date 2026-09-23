FROM python:3.14-slim

WORKDIR /app

COPY app.py .

RUN pip install --no-cache-dir Flask

EXPOSE 5002

CMD ["python", "app.py"]