FROM python:3.9-slim-buster

COPY requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt

COPY src /app/src

WORKDIR /app/src

CMD ["python", "main.py"]