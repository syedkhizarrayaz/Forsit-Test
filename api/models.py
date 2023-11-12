# api/models.py

from sqlalchemy import Column, Integer, String, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from pydantic import BaseModel

Base = declarative_base()

class Product(Base):
    __tablename__ = "Product"
    product_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    description = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationship with Sale, Revenue, Inventory, and NewProductRegistration
    sales = relationship("Sale", back_populates="product")
    revenues = relationship("Revenue", back_populates="product")
    inventory = relationship("Inventory", back_populates="product")
    new_product_registrations = relationship("NewProductRegistration", back_populates="product")

class Sale(Base):
    __tablename__ = "Sale"
    sale_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("Product.product_id"), nullable=False)
    amount = Column(Float, nullable=False)
    sale_date = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship with Product
    product = relationship("Product", back_populates="sales")

class Revenue(Base):
    __tablename__ = "Revenue"
    revenue_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("Product.product_id"), nullable=False)
    amount = Column(Float, nullable=False)
    revenue_date = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship with Product
    product = relationship("Product", back_populates="revenues")

class Inventory(Base):
    __tablename__ = "Inventory"
    inventory_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("Product.product_id"), nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship with Product
    product = relationship("Product", back_populates="inventory")

class NewProductRegistration(Base):
    __tablename__ = "NewProductRegistration"
    registration_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("Product.product_id"), nullable=False)
    name = Column(String(255), nullable=False)  # Include the name column
    registration_date = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationship with Product
    product = relationship("Product", back_populates="new_product_registrations")

class InventoryChange(Base):
    __tablename__ = "InventoryChange"
    inventory_change_id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer, ForeignKey("Product.product_id"), nullable=False)
    quantity_change = Column(Integer, nullable=False)
    change_date = Column(DateTime, default=datetime.utcnow)