-- Create the Product table
CREATE TABLE Product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    category VARCHAR(255) DEFAULT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create the Sale table
CREATE TABLE Sale (
    sale_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    amount DECIMAL(10, 2) NOT NULL,
    sale_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

-- Create the Revenue table
CREATE TABLE Revenue (
    revenue_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    amount DECIMAL(10, 2) NOT NULL,
    revenue_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

-- Create the Inventory table
CREATE TABLE Inventory (
    inventory_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    quantity INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

-- Create the NewProductRegistration table
CREATE TABLE NewProductRegistration (
    registration_id INT AUTO_INCREMENT PRIMARY KEY,
    product_id INT,
    name VARCHAR(255) NOT NULL, -- Include the name column
    category VARCHAR(255) DEFAULT NULL;
    registration_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
);

-- Insert 10 dummy values into the Product table
INSERT INTO Product (name, description) VALUES
    ('Product 1', 'Description for Product 1','category1'),
    ('Product 2', 'Description for Product 2','category1'),
    ('Product 3', 'Description for Product 3','category1'),
    ('Product 4', 'Description for Product 4','category1'),
    ('Product 5', 'Description for Product 5','category1'),
    ('Product 6', 'Description for Product 6','category1'),
    ('Product 7', 'Description for Product 7','category1'),
    ('Product 8', 'Description for Product 8','category1'),
    ('Product 9', 'Description for Product 9','category1'),
    ('Product 10', 'Description for Product 10','category1');

-- Insert 10 dummy values into the Sale table
INSERT INTO Sale (product_id, amount) VALUES
    (1, 100.0),
    (2, 150.0),
    (3, 120.0),
    (1, 80.0),
    (2, 200.0),
    (3, 90.0),
    (1, 110.0),
    (2, 170.0),
    (3, 130.0),
    (1, 95.0);

-- Insert 10 dummy values into the Revenue table
INSERT INTO Revenue (product_id, amount) VALUES
    (1, 500.0),
    (2, 750.0),
    (3, 600.0),
    (1, 400.0),
    (2, 800.0),
    (3, 450.0),
    (1, 550.0),
    (2, 700.0),
    (3, 650.0),
    (1, 480.0);

-- Insert 10 dummy values into the Inventory table
INSERT INTO Inventory (product_id, quantity) VALUES
    (1, 50),
    (2, 75),
    (3, 60),
    (1, 40),
    (2, 100),
    (3, 45),
    (1, 55),
    (2, 85),
    (3, 65),
    (1, 47);

-- Insert 10 dummy values into the NewProductRegistration table
INSERT INTO NewProductRegistration (product_id, name) VALUES
    (4, 'New Product 1', 'category1'),
    (5, 'New Product 2','category2'),
    (6, 'New Product 3','category3'),
    (7, 'New Product 4','category4'),
    (8, 'New Product 5','category5'),
    (9, 'New Product 6','category6'),
    (10, 'New Product 7','category7'),
    (1, 'New Product 8', 'category8'),
    (2, 'New Product 9','category9'),
    (3, 'New Product 10','category10');
