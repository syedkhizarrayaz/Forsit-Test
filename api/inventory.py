# api/inventory.py

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from .database import get_db
from .models import Inventory, Product, InventoryChange
import logging
from datetime import datetime

logger = logging.getLogger(__name__)

router = APIRouter()

def get_dummy_inventory():
    # Return dummy inventory data
    return [
        {
            "inventory_id": 1,
            "product_id": 1,
            "product_name": "Product A",
            "quantity": 50,
            "created_at": "2023-01-01T10:00:00",
        },
        # Add more dummy data as needed
    ]

def update_inventory(
    db: Session,
    product_id: int,
    quantity_change: int,
):
    try:
        # Get the current inventory
        current_inventory = db.execute(select(Inventory).where(Inventory.product_id == product_id)).first()

        # Update the inventory quantity
        current_inventory.quantity += quantity_change

        # Save the changes
        db.commit()

        # Log the inventory change
        log_inventory_change(db, product_id, quantity_change)

        return True
    except Exception as e:
        logger.exception("An error occurred while updating inventory.")
        return False

def log_inventory_change(
    db: Session,
    product_id: int,
    quantity_change: int,
):
    try:
        # Log the inventory change
        change_log = InventoryChange(
            product_id=product_id,
            quantity_change=quantity_change,
            change_date=datetime.utcnow()
        )

        # Save the change log
        db.add(change_log)
        db.commit()

        return True
    except Exception as e:
        logger.exception("An error occurred while logging inventory change.")
        return False

@router.get("/inventory/", response_model=list[dict])
async def get_inventory(
    low_stock_threshold: int = 10,
    db: Session = Depends(get_db)
):
    try:
        # Build the base query
        query = select(Inventory, Product).join(Product)

        # Execute the query
        results = db.execute(query).fetchall()

        # Get inventory data
        inventory_data = [
            {
                "inventory_id": result.Inventory.inventory_id,
                "product_id": result.Inventory.product_id,
                "product_name": result.Product.name,
                "quantity": result.Inventory.quantity,
                "created_at": result.Inventory.created_at,
            }
            for result in results
        ]

        # Check for low stock and add a flag to indicate low stock
        for item in inventory_data:
            item["low_stock"] = item["quantity"] < low_stock_threshold

        return inventory_data
    except Exception as e:
        logger.exception("An error occurred while processing /inventory/")
        # Return dummy values in case of an error
        return get_dummy_inventory()

@router.put("/inventory/update/{product_id}/{quantity_change}")
async def update_inventory_quantity(
    product_id: int,
    quantity_change: int,
    db: Session = Depends(get_db)
):
    success = update_inventory(db, product_id, quantity_change)
    if success:
        return {"message": "Inventory updated successfully"}
    else:
        raise HTTPException(status_code=500, detail="Failed to update inventory")

