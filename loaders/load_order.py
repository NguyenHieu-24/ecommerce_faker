from database.connection import get_connection
from generators.order_generator import generate_orders

def load_orders():
    conn = get_connection()
    cursor = conn.cursor()

    seller_ids = [r[0] for r in cursor.execute(
        "SELECT seller_id FROM seller"
    )]

    orders = generate_orders(10000, seller_ids)

    for o in orders:
        cursor.execute("""
            INSERT INTO orders
            (order_date, seller_id, status, total_amount)
            VALUES (?, ?, ?, ?)
        """,
        o["order_date"],
        o["seller_id"],
        o["status"],
        o["total_amount"])

    conn.commit()
    cursor.close()
    conn.close()
