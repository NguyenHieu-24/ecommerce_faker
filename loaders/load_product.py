from database.connection import get_connection
from generators.product_generator import generate_products

def load_products():
    conn = get_connection()
    cursor = conn.cursor()

    category_ids = [r[0] for r in cursor.execute("SELECT category_id FROM category")]
    brand_ids = [r[0] for r in cursor.execute("SELECT brand_id FROM brand")]
    seller_ids = [r[0] for r in cursor.execute("SELECT seller_id FROM seller")]

    products = generate_products(200, category_ids, brand_ids, seller_ids)

    for p in products:
        cursor.execute("""
            INSERT INTO product
            (product_name, category_id, brand_id, seller_id,
             price, discount_price, stock_qty, rating, created_at, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """,
        p["product_name"], p["category_id"], p["brand_id"], p["seller_id"],
        p["price"], p["discount_price"], p["stock_qty"],
        p["rating"], p["created_at"], p["is_active"])

    conn.commit()
    cursor.close()
    conn.close()
