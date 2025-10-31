from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PredictRequest(BaseModel):
    pickup_longitude: float
    pickup_latitude: float
    dropoff_longitude: float
    dropoff_latitude: float
    passenger_count: Optional[int] = 1

class PredictResponse(BaseModel):
    predicted_fare: float
    predicted_duration: Optional[float] = None
    model_name: str
