import pyodbc

conn = pyodbc.connect(
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost\\SQLEXPRESS;"
    "DATABASE=ecommerce;"
    "Trusted_Connection=yes;"
)

print("CONNECTED SUCCESSFULLY ✅")
conn.close()
