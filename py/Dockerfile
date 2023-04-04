FROM python:slim-bullseye

WORKDIR /app

COPY requirements/backend.in .

COPY . .

RUN pip install --no-cache-dir -r backend.in


CMD ["uvicorn", "spaceship.main:app", "--host=0.0.0.0", "--port=8080"]