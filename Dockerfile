FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# system deps
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# install deps
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# copy code
COPY . /app

# collect static files (only if settings allow it during build)
RUN python manage.py collectstatic --noinput || true

EXPOSE 8000

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--log-level", "info"]
