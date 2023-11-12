# api/database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Specify your database connection parameters
DB_USERNAME = "root"
DB_PASSWORD = ""
DB_HOST = "127.0.0.1"
DB_PORT = 3306
DB_NAME = "forsittest"

# Create the database connection string
DATABASE_URL = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()