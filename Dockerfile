# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the project files into the container
COPY . /app/

RUN python manage.py makemigrations
RUN python manage.py migrate

# Expose the port the app runs on (default to 8000, but Render will override this)
EXPOSE 8000

# Command to run the application
CMD ["gunicorn", "project.wsgi:application", "--bind", "0.0.0.0:8000"]
