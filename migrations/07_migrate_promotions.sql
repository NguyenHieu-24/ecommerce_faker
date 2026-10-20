IF NOT EXISTS (
    SELECT * FROM sys.tables WHERE name = 'promotions'
)
BEGIN
    CREATE TABLE dbo.promotions (
        promotion_id INT IDENTITY PRIMARY KEY,
        promotion_name VARCHAR(100),
        promotion_type VARCHAR(50),
        discount_type VARCHAR(20),
        discount_value DECIMAL(10,2),
        start_date DATE,
        end_date DATE
    );
END;
