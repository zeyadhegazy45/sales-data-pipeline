-- Create the customers table with customer_id as the primary key
CREATE TABLE IF NOT EXISTS customers (
    customer_id VARCHAR(50) PRIMARY KEY,  -- Make customer_id the primary key
    customer_name VARCHAR NOT NULL,
    address VARCHAR NOT NULL,
    birth_date DATE NOT NULL
);

-- Create the sales table with a foreign key referencing customer_id
CREATE TABLE IF NOT EXISTS sales (
    sale_id SERIAL PRIMARY KEY,
    customer_id VARCHAR(50) REFERENCES customers(customer_id),
    product VARCHAR NOT NULL,
    amount DECIMAL NOT NULL,
    sale_date DATE NOT NULL
);
