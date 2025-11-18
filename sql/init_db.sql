CREATE TABLE IF NOT EXISTS sales (
    id SERIAL PRIMARY KEY,
    order_date DATE,
    product VARCHAR(255),
    region VARCHAR(100),
    quantity INTEGER,
    unit_price NUMERIC(10,2)
);
