FROM python:3.10-slim

EXPOSE 8050 80

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

COPY app/main.py /app/main.py
COPY app/fastapi_module.py /app/fastapi_module.py
COPY app/test.py /app/test.py

WORKDIR /app/

ENTRYPOINT ["python", "main.py"]