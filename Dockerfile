# Використовуємо офіційний образ Python
FROM python:3.11

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо файли проєкту в контейнер
COPY . /app

# Встановлюємо залежності з requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо вашу базу даних у контейнер
COPY fitness.db /app/fitness.db

# Вказуємо, яку команду виконати для запуску програми
CMD ["python", "interactive.py"]
