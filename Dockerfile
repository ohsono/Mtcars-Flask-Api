FROM python:3.12-slim

WORKDIR /app

# Install build dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy just the requirements first to leverage Docker caching
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir numpy==1.26.0 && \
    pip install --no-cache-dir -r requirements.txt

COPY app app/
COPY run.py .

RUN mkdir -p data

# Expose port
EXPOSE 5001

CMD ["python", "run.py"]