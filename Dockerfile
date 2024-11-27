# Вказуємо базовий образ Python
FROM python:3.9-alpine

# Встановлюємо робочу директорію всередині контейнера
WORKDIR /app

# Копіюємо файл з кодом у контейнер
COPY program.py ./

# Вказуємо команду для запуску вашої програми NoteManager
CMD ["python", "program.py"]
