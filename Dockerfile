FROM python:3.12-slim

WORKDIR /app

# Update system packages and install security updates
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python packages with security updates
RUN pip install --no-cache-dir --upgrade pip setuptools wheel && \
    pip install --no-cache-dir \
    flask==2.0.1 \
    werkzeug==2.0.1 \
    scikit-learn==1.3.2 \
    pandas==2.0.3 \
    numpy==1.26.0 \
    pytest==7.4.0

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