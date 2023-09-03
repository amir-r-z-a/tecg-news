# Use the official Python image as the base image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Create and set the working directory
WORKDIR /app

# Install system dependencies if needed (uncomment and add commands as necessary)
# RUN apt-get update && apt-get install -y ...

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

# Copy the Django project files into the container
COPY . .

# Expose the port your Django app will run on (if needed)
# EXPOSE 8000

# Command to run your Django app (customize this as needed)
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]

