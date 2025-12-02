# Use a lightweight Python base
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Open port 5000
EXPOSE 5000

# Command to run the app
CMD ["python", "app.py"]