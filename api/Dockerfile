# Use official Python image
FROM python:3.9

# Set work directory
WORKDIR /app

# Copy requirements and install them
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Expose port
EXPOSE 5000

# Run the API
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "5000"]
