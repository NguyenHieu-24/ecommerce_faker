from database.connection import get_connection
from generators.brand_generator import generate_brands

def load_brands():
    conn = get_connection()
    cursor = conn.cursor()

    brands = generate_brands(30)

    for b in brands:
        cursor.execute("""
            INSERT INTO brand (brand_name, country, created_at)
            VALUES (?, ?, ?)
        """, b["brand_name"], b["country"], b["created_at"])

    conn.commit()
    cursor.close()
    conn.close()
