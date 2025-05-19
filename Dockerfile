FROM python:3.12-slim

WORKDIR /app

# Update system packages and install security updates
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt ./requirements.txt

# Install Python packages with security updates
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install -r ./requirements.txt

# Create data directory and copy data file
RUN mkdir -p Data
COPY Data/mtcars.csv Data/

# Copy application files
COPY app app/
COPY run.py .

# Expose port
EXPOSE 5001

# Run the application
CMD ["python", "run.py"]