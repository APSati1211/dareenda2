# Use official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /app

# System dependencies (add others as needed)
RUN apt-get update \
    && apt-get install -y build-essential libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy project
COPY . /app

# Collect static files (if using Django static)
RUN python manage.py collectstatic --noinput

# Expose port
EXPOSE 8000

# Entrypoint: update this as needed for your project!
CMD ["gunicorn", "backend.wsgi:application", "--bind", "0.0.0.0:8000"]

# If your main app is NOT in core.wsgi, replace core with your Django project's main module name.
