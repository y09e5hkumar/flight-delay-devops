# ✈️ Flight Delay Prediction — DevOps for AI

## Project Overview
A machine learning API that predicts flight delays using a Random Forest model, deployed with full DevOps practices.

## Tech Stack
- **ML Model:** Random Forest (scikit-learn)
- **API:** FastAPI
- **Container:** Docker
- **CI/CD:** GitHub Actions
- **Deployment:** Render.com

## Live API
🔗 https://flight-delay-devops.onrender.com/docs

## How to Run Locally
```bash
docker build -t flight-delay-api .
docker run -p 8000:8000 flight-delay-api
```

## Input Features
| Feature | Description |
|---------|-------------|
| OP_CARRIER | Airline code |
| ORIGIN | Departure airport |
| DEST | Arrival airport |
| CRS_DEP_TIME | Scheduled departure time |
| CRS_ARR_TIME | Scheduled arrival time |
| DISTANCE | Flight distance (miles) |

## Sample Prediction
Input: AA flight JFK→LAX
Output: On Time (16% delay probability)