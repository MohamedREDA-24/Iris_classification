from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
import numpy as np
from typing import List

app = FastAPI()

# Load model
try:
    with open("iris_model.pkl", "rb") as f:
        model = pickle.load(f)
    print("Model loaded successfully")
except Exception as e:
    print(f"Error loading model: {e}")


# Pydantic model to validate the input data
class PredictionRequest(BaseModel):
    feature_array: List[float]


@app.post("/predict")
async def predict(request: PredictionRequest):
    try:
        # Extract features from the request
        features = np.array(request.feature_array).reshape(1, -1)

        # Make the prediction
        prediction = model.predict(features)

        # Return the prediction
        return {"prediction": prediction.tolist()}

    except Exception as e:
        # Raise HTTPException for errors
        raise HTTPException(status_code=500, detail=f"Error during prediction: {str(e)}")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
