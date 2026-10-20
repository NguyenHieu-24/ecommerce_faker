IF NOT EXISTS (
    SELECT * FROM sys.tables WHERE name = 'orders'
)
BEGIN
    CREATE TABLE dbo.orders (
        order_id INT IDENTITY PRIMARY KEY,
        order_date DATETIME NOT NULL,
        seller_id INT NOT NULL,
        status VARCHAR(30),
        total_amount DECIMAL(12,2),
        created_at DATETIME DEFAULT GETDATE(),
        CONSTRAINT fk_orders_seller
        FOREIGN KEY (seller_id)
        REFERENCES seller(seller_id)
    );
END;