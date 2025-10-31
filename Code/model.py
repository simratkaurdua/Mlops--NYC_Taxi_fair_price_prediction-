from sqlalchemy import Column, Integer, Float, String, DateTime
from database import Base

class TaxiTrip(Base):
    __tablename__ = "taxi_trips"

    id = Column(Integer, primary_key=True, index=True)
    pickup_datetime = Column(DateTime)
    dropoff_datetime = Column(DateTime)
    passenger_count = Column(Integer)
    pickup_longitude = Column(Float)
    pickup_latitude = Column(Float)
    dropoff_longitude = Column(Float)
    dropoff_latitude = Column(Float)
    fare_amount = Column(Float)
