from database.connection import get_connection
import random

def load_promotion_products():
    conn = get_connection()
    cursor = conn.cursor()

    promotion_ids = [r[0] for r in cursor.execute(
        "SELECT promotion_id FROM promotions"
    )]

    product_ids = [r[0] for r in cursor.execute(
        "SELECT product_id FROM product"
    )]

    for promo_id in promotion_ids:
        products = random.sample(product_ids, k=random.randint(5, 15))
        for product_id in products:
            cursor.execute("""
                INSERT INTO promotion_products
                (promotion_id, product_id)
                VALUES (?, ?)
            """, promo_id, product_id)

    conn.commit()
    cursor.close()
    conn.close()
