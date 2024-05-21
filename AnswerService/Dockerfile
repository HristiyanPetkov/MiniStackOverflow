FROM python:3.8-slim-buster

COPY requirements.txt .
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .

CMD python app.py
