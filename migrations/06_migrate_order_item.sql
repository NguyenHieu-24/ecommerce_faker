IF NOT EXISTS (
    SELECT * FROM sys.tables WHERE name = 'order_item'
)
BEGIN
    CREATE TABLE dbo.order_item (
        order_item_id INT IDENTITY PRIMARY KEY,
        order_id INT NOT NULL,
        product_id INT NOT NULL,
        quantity INT NOT NULL,
        unit_price DECIMAL(12,2),
        subtotal DECIMAL(12,2),

        FOREIGN KEY (order_id) REFERENCES orders(order_id),
        FOREIGN KEY (product_id) REFERENCES product(product_id)
    );
END;