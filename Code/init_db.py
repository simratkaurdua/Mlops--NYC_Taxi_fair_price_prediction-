from database import Base, engine
from model import TaxiTrip

print("🚀 Creating tables in PostgreSQL...")
Base.metadata.create_all(bind=engine)
print("✅ Tables created!")
