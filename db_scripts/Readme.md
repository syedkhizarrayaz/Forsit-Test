# Database Scripts

This directory contains SQL scripts for setting up and populating the database for the Forsittest project.

## Schema Explanation

### Product Table

- **Columns:**
  - `product_id`: Primary key, auto-incremented.
  - `name`: Name of the product.
  - `description`: Description of the product.
  - `created_at`: Timestamp of when the product was created.

### Sale Table

- **Columns:**
  - `sale_id`: Primary key, auto-incremented.
  - `product_id`: Foreign key referencing the `product_id` in the Product table.
  - `amount`: Sale amount.
  - `sale_date`: Timestamp of when the sale occurred.
  - `created_at`: Timestamp of when the sale record was created.

### Revenue Table

- **Columns:**
  - `revenue_id`: Primary key, auto-incremented.
  - `product_id`: Foreign key referencing the `product_id` in the Product table.
  - `amount`: Revenue amount.
  - `revenue_date`: Timestamp of when the revenue was recorded.
  - `created_at`: Timestamp of when the revenue record was created.

### Inventory Table

- **Columns:**
  - `inventory_id`: Primary key, auto-incremented.
  - `product_id`: Foreign key referencing the `product_id` in the Product table.
  - `quantity`: Quantity of the product in inventory.
  - `created_at`: Timestamp of when the inventory record was created.

### NewProductRegistration Table

- **Columns:**
  - `registration_id`: Primary key, auto-incremented.
  - `product_id`: Foreign key referencing the `product_id` in the Product table.
  - `name`: Name of the new product.
  - `registration_date`: Timestamp of when the new product was registered.
  - `created_at`: Timestamp of when the registration record was created.

### InventoryChange Table

- **Columns:**
  - `inventory_change_id`: Primary key, auto-incremented.
  - `product_id`: Foreign key referencing the `product_id` in the Product table.
  - `quantity_change`: Quantity change value.
  - `change_date`: Timestamp of when the inventory change occurred.

## Purpose

This database schema is designed to manage products, sales, revenue, inventory, and new product registrations for a web admin dashboard. The tables are interconnected through foreign key relationships to maintain data integrity and provide a comprehensive view of product-related activities.