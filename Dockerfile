FROM python:3.9-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY src/ src/
COPY templates/ templates/
COPY data/ data/

CMD ["python", "src/application.py"]