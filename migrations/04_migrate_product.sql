IF NOT EXISTS (
    SELECT * FROM sys.tables WHERE name = 'product'
)
BEGIN
    CREATE TABLE dbo.product (
        product_id INT IDENTITY PRIMARY KEY,
        product_name VARCHAR(200) NOT NULL,
        category_id INT NOT NULL,
        brand_id INT NOT NULL,
        seller_id INT NOT NULL,
        price DECIMAL(12,2) NOT NULL,
        discount_price DECIMAL(12,2),
        stock_qty INT NOT NULL,
        rating FLOAT,
        created_at DATETIME DEFAULT GETDATE(),
        is_active BIT DEFAULT 1,

        FOREIGN KEY (category_id) REFERENCES category(category_id),
        FOREIGN KEY (brand_id) REFERENCES brand(brand_id),
        FOREIGN KEY (seller_id) REFERENCES seller(seller_id)
    );
END;