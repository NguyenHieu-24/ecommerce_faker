from database.connection import get_connection
from generators.seller_generator import generate_sellers

def load_sellers():
    conn = get_connection()
    cursor = conn.cursor()

    sellers = generate_sellers(20)

    for s in sellers:
        cursor.execute("""
            INSERT INTO seller (seller_name, join_date, rating, country)
            VALUES (?, ?, ?, ?)
        """, s["seller_name"], s["join_date"], s["rating"], s["country"])

    conn.commit()
    cursor.close()
    conn.close()
