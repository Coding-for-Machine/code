# Python 3.9 asosidagi imajni ishlatamiz
FROM python:3.14.0a1-slim

# Ishlash papkasini yaratamiz
WORKDIR /app

# Kerakli kutubxonalarni o‘rnatish uchun requirements.txt faylini konteynerga nusxalaymiz
COPY requirements.txt /app/

# Kutubxonalarni o‘rnatamiz
RUN pip install --no-cache-dir -r requirements.txt

# Kodni konteynerga nusxalaymiz
COPY . /app

# Flask API serverini ishga tushuramiz
CMD ["python", "app.py"]
