FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install flask prometheus_client

EXPOSE 8002

CMD ["python", "app.py"]
