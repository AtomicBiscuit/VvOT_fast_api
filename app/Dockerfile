FROM python:3.10-slim

EXPOSE 8050 80

COPY requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /app/

COPY main.py /app/main.py
COPY fastapi_module.py /app/fastapi_module.py

ENTRYPOINT ["python", "main.py"]