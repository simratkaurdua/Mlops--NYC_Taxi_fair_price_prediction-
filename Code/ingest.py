import os
import pandas as pd
from sqlalchemy import create_engine
from Code import model

DB_URL = os.getenv("DATABASE_URL", "postgresql+psycopg2://mlops_user:mlops_pwd@localhost:5432/nyc_trips")

def create_tables(engine):
    model.Base.metadata.create_all(engine)

def ingest(csv_path: str):
    engine = create_engine(DB_URL)
    create_tables(engine)
    df = pd.read_csv(csv_path, low_memory=False)
    # ensure only expected columns
    required_cols = [
        "pickup_datetime", "dropoff_datetime", "passenger_count",
        "pickup_longitude", "pickup_latitude",
        "dropoff_longitude", "dropoff_latitude", "fare_amount"
    ]
    df = df[required_cols]
    df.to_sql("taxi_trips", engine, if_exists="append", index=False, method="multi")
    print(f"Ingested {len(df)} rows into taxi_trips table.")

if __name__ == "__main__":
    import sys
    csv = sys.argv[1] if len(sys.argv) > 1 else r"C:\sim_project\MLOPS Project\Mlops--NYC_Taxi_fair_price_prediction-\Data\yellow_tripdata_2015-01.csv"
    ingest(csv)
