FROM python:3.10-slim-buster

WORKDIR /app

ENV PYTHONUNBUFFERED=1

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt


COPY . /app

EXPOSE 8001

CMD ["uvicorn","api:app","--reload","--host","0.0.0.0","--port","8001"]
