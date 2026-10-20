IF NOT EXISTS (
    SELECT * FROM sys.tables WHERE name = 'seller'
)
BEGIN
    CREATE TABLE dbo.seller (
        seller_id INT IDENTITY PRIMARY KEY,
        seller_name VARCHAR(100) NOT NULL,
        join_date DATE NOT NULL,
        rating DECIMAL(3,2),
        country VARCHAR(50)
    );
END;