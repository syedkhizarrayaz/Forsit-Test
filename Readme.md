# Forsit Test

## Setup Instructions

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/your-fastapi-project.git
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    cd your-fastapi-project
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the FastAPI application:

    ```bash
    uvicorn api.main:app --reload
    ```

6. Open your browser and go to [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) to access the Swagger documentation.

## Dependencies

- FastAPI: [FastAPI Documentation](https://fastapi.tiangolo.com/)
- Uvicorn: [Uvicorn Documentation](https://www.uvicorn.org/)
- SQLAlchemy: [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

## API Endpoints

### Sales

- **GET /sales/**

  Retrieve a list of sales data.

  Query Parameters:
  - `product_name` (optional): Filter sales data by product name.

- **GET /sales/total_amount/**

  Retrieve the total sales amount.

  Query Parameters:
  - `product_name` (optional): Filter total sales amount by product name.

### Inventory

- **GET /inventory/**

  Retrieve the current inventory status.

  Query Parameters:
  - `low_stock_threshold` (optional): Specify the threshold for low stock (default is 10).

- **PUT /inventory/update/{product_id}/{quantity_change}**

  Update the inventory quantity for a specific product.

  Path Parameters:
  - `product_id`: ID of the product.
  - `quantity_change`: Quantity change value (positive for addition, negative for subtraction).

## Database Problem
there is a problem in connecting the database somehow, i have returned the dummy values on error for testing.