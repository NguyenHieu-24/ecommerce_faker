IF NOT EXISTS (
    SELECT * FROM sys.tables WHERE name = 'category'
)
BEGIN
    CREATE TABLE dbo.category (
        category_id INT IDENTITY(1,1) PRIMARY KEY,
        category_name VARCHAR(100) NOT NULL,
        parent_category_id INT NULL,
        level SMALLINT NOT NULL,
        created_at DATETIME NOT NULL DEFAULT GETDATE(),

        CONSTRAINT fk_category_parent
            FOREIGN KEY (parent_category_id)
            REFERENCES dbo.category(category_id)
    );
END;
