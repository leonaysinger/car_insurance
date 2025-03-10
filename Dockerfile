# Use Python 3.10 slim as base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Set environment variable
ENV CAR_VALUE_LIMIT_CALCULATION=10000
ENV CAR_YEAR_RATE=0.5
ENV CAR_VALUE_RATE=0.5

# Copy only the requirements file first for better caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose FastAPI default port
EXPOSE 8000

# Command to run FastAPI with Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
