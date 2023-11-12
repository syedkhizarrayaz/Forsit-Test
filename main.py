from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from api import database



# # Create a FastAPI app
app = FastAPI()

database.sessionmaker()

metadata = MetaData()

# # Dependency to get the database session
# def get_database():
#     db = engine
#     try:
#         yield db
#         print(db)
#     finally:
#         db.dispose()

# Import the sales router from api.sales
from api.sales import router as sales_router
from api.inventory import router as inventory_router
# Include the sales router with a prefix
app.include_router(sales_router, prefix="/api", tags=["sales"])
app.include_router(inventory_router, prefix="/api", tags=["inventory"])
# Run the application using uvicorn
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
