from database.connection import get_connection
from generators.promotion_generator import generate_promotions

def load_promotions():
    conn = get_connection()
    cursor = conn.cursor()

    promotions = generate_promotions(10)

    for p in promotions:
        cursor.execute("""
            INSERT INTO promotions
            (promotion_name, promotion_type, discount_type,
             discount_value, start_date, end_date)
            VALUES (?, ?, ?, ?, ?, ?)
        """,
        p["promotion_name"],
        p["promotion_type"],
        p["discount_type"],
        p["discount_value"],
        p["start_date"],
        p["end_date"])

    conn.commit()
    cursor.close()
    conn.close()
