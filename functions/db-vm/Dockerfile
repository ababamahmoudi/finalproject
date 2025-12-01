FROM python:3.10-slim

WORKDIR /app

COPY order_processor.py .
COPY email_notifier.py .
COPY inventory_worker.py .
RUN pip install redis

CMD ["python3", "order_processor.py"]
