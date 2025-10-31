#checks for incoming data and chek the type of the data
from pydantic import BaseModel
from datetime import datetime

class TaxiTripBase(BaseModel):
    pickup_datetime: datetime
    dropoff_datetime: datetime
    passenger_count: int
    trip_distance: float
    pickup_longitude: float
    pickup_latitude: float
    dropoff_longitude: float
    dropoff_latitude: float
    fare_amount: float

class TaxiTripCreate(TaxiTripBase):
    pass

class TaxiTripOut(TaxiTripBase):
    id: int

    class Config:
        from_attributes = True
