FROM python:3.10-slim

# Tizim kutubxonalari va zaruriy paketlarni o'rnatamiz
RUN apt-get update && apt-get install -y python3-venv python3-pip gcc libpq-dev

# Loyihani /app papkasiga ko'chiramiz
WORKDIR /app

# requirements.txt faylini ko'chiramiz
COPY requirements.txt .

# Virtual muhit yaratamiz va kutubxonalarni o'rnatamiz
RUN python -m venv env && \
    . env/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

# Barcha loyihani ko'chiramiz
COPY . .

# Portni ochamiz
EXPOSE 8000

# Django serverni ishga tushiramiz
CMD ["/bin/bash", "-c", ". env/bin/activate && python manage.py runserver 0.0.0.0:8000"]