# Use official Python image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE=1

# Ensure logs are shown instantly
ENV PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# COPY requirements.txt first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN  pip install --no-cache-dir --upgrade pip && \
pip install --no-cache-dir -r requirements.txt

# Copy entire application code
COPY . .

# Expose the port FastAPI will run on
EXPOSE 8000

# Run FastAPI with Uvicorn
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "8000"]

# Health check
HEALTHCHECK --interval=30s --timeout=10s  --retries=3 CMD curl -f http://localhost:8000/health || exit 1
