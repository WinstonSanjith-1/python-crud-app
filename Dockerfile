FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install dependencies (including uvicorn)
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Start the FastAPI application
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "5000"]
