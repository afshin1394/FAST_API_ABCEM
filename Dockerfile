# Use an official Python runtime as a parent image
FROM python:3.10-slim-buster

# Set a working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy your FastAPI application code into the container
COPY ./app ./app

# Expose the port FastAPI will run on
EXPOSE 8000

# Start FastAPI using uvicorn
CMD ["uvicorn", "abcem.main:app", "--host", "0.0.0.0", "--port", "8000"]
