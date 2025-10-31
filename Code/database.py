from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# format: postgresql://username:password@host:port/dbname
DATABASE_URL = "postgresql://postgres:sim123@localhost:5432/taxi_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=engine)
Base = declarative_base()

# Test connection
try:
    with engine.connect() as conn:
        print("✅ Connected to PostgreSQL!")
except Exception as e:
    print("❌ Connection failed:", e)

