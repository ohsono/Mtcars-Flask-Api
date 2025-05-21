# Mtcars Flask API

**Class:** UCLA-MASDS-STATS418-S25  
**Author:** Hochan Son  
**Date:** 2025-05-18

## Project Overview
This project implements a Flask-based REST API for predicting MPG (Miles Per Gallon) using the classic mtcars dataset. The API provides endpoints for model predictions, health checks, and model performance metrics.

## Project Requirements
- [x] Create a standalone GitHub repository for the Mtcars Flask API
- [x] Implement a predictive linear model using the mtcars dataset
- [x] Containerize the application using Docker
- [x] Create a functional Flask API
- [x] Push the image to DockerHub
- [x] Deploy to Google Cloud Run

## Project Structure
```
.
├── app/                    # Application package
│   ├── __init__.py        # Package initialization
│   ├── model.py           # ML model implementation
│   └── server.py          # API endpoints
├── Data/                   # Dataset directory
│   └── mtcars.csv         # Training data
├── docker-compose.yml     # Docker Compose configuration
├── Dockerfile             # Docker build instructions
├── requirements.txt       # Python dependencies
└── run.py                 # Application entry point
```

## Setup and Installation

### Prerequisites
- Docker
- Docker Compose
- Python 3.12

### Dependencies
```
flask==2.0.1
werkzeug==2.0.1
scikit-learn==1.3.2
pandas==2.0.3
numpy==1.26.0
pytest==7.4.0
```

### Running the Application

#### Using Docker Compose (Recommended)
```bash
docker-compose up -d
```

#### Using Docker Directly
```bash
# Build the image
docker build -t flask-app-hochan:1.0 .

# Run the container
docker run -d -p 5001:5001 --name mtcars-api flask-app-hochan:1.0
```

## API Endpoints
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/health` | GET | Health check |
| `/predict` | POST | Predict MPG based on car features |
| `/model/info` | GET | Get model information and metrics |


### 1. Health Check
```bash
curl http://localhost:5001/health
```
Response:
```json
{
  "code": 200,
  "model_features": ["cyl", "disp", "hp", "drat", "wt", "qsec", "vs", "am", "gear", "carb"],
  "model_status": "trained",
  "status": "healthy"
}
```

### 2. MPG Prediction
```bash
curl -X POST http://localhost:5001/predict \
  -H "Content-Type: application/json" \
  -d '{
    "cyl": 6,
    "disp": 160,
    "hp": 110,
    "drat": 3.9,
    "wt": 2.62,
    "qsec": 16.46,
    "vs": 0,
    "am": 1,
    "gear": 4,
    "carb": 4
  }'
```
Response:
```json
{
  "features_used": ["cyl", "disp", "hp", "drat", "wt", "qsec", "vs", "am", "gear", "carb"],
  "predicted_mpg": 21.87895894528168
}
```

### 3. Model Information
```bash
curl http://localhost:5001/model/info
```
Response:
```json
{
  "coefficients": {
    "am": 1.076624251329717,
    "carb": 0.14713124818156334,
    "cyl": -0.4762499019891346,
    "disp": 0.018311070453806498,
    "drat": 1.0021304842965426,
    "gear": 1.3271075861045074,
    "hp": -0.009500305884922615,
    "qsec": 1.84095198396203,
    "vs": -1.9371857925347522,
    "wt": -4.862037065437054
  },
  "intercept": -5.593700289851515,
  "r_squared": 0.7466453084791007,
  "rmse": 3.1827903901745196,
  "sample_size": 25
}
```

## Stopping the Application
To stop the application:
1. If using Docker Compose:
   ```bash
   docker-compose down -v
   ```
2. If using Docker directly:
   ```bash
   docker stop mtcars-api
   docker rm mtcars-api
   ```

## Model Performance
The linear regression model achieves:
- R-squared: 0.747
- RMSE: 3.183
- Sample Size: 25 observations

## Docker Hub Repository
The application is available as a Docker image:
- **Repository:** docker.io/ohsonoresearch/mtcars-api
- **Tag:** latest
- **Size:** 976MB (444.86 MB, compressed)

### Building and Pushing to Docker Hub
To build and push the multi-architecture image:
```bash
# Create and use a new builder instance
docker buildx create --use

# Build and push the image
docker buildx build --platform linux/amd64 -t docker.io/ohsonoresearch/mtcars-api:latest . --push
```
or simply run this:
```
docker_hub_build.sh
```
