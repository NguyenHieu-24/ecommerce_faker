IF NOT EXISTS (
    SELECT * FROM sys.tables WHERE name = 'brand'
)
BEGIN
    CREATE TABLE dbo.brand (
        brand_id INT IDENTITY(1,1) PRIMARY KEY,
        brand_name VARCHAR(100) NOT NULL,
        country VARCHAR(50) NOT NULL,
        created_at DATETIME NOT NULL DEFAULT GETDATE()
    );
END;
