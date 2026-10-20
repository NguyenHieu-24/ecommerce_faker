IF NOT EXISTS (
    SELECT * FROM sys.tables WHERE name = 'promotion_products'
)
BEGIN
    CREATE TABLE dbo.promotion_products (
        promotion_product_id INT IDENTITY PRIMARY KEY,
        promotion_id INT NOT NULL,
        product_id INT NOT NULL,
        created_at DATETIME DEFAULT GETDATE(),

        FOREIGN KEY (promotion_id) REFERENCES promotions(promotion_id),
        FOREIGN KEY (product_id) REFERENCES product(product_id)
    );
END;