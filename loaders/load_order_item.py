from database.connection import get_connection
from generators.order_item_generator import generate_order_items

def load_order_items():
    conn = get_connection()
    cursor = conn.cursor()

    order_ids = [r[0] for r in cursor.execute(
        "SELECT order_id FROM orders"
    )]

    product_ids = [r[0] for r in cursor.execute(
        "SELECT product_id FROM product"
    )]

    items = generate_order_items(order_ids, product_ids)

    order_totals = {}

    for i in items:
        cursor.execute("""
            INSERT INTO order_item
            (order_id, product_id, quantity, unit_price, subtotal)
            VALUES (?, ?, ?, ?, ?)
        """,
        i["order_id"],
        i["product_id"],
        i["quantity"],
        i["unit_price"],
        i["subtotal"])

        order_totals[i["order_id"]] = (
            order_totals.get(i["order_id"], 0) + i["subtotal"]
        )

    # Update order total_amount
    for order_id, total in order_totals.items():
        cursor.execute("""
            UPDATE orders
            SET total_amount = ?
            WHERE order_id = ?
        """, total, order_id)

    conn.commit()
    cursor.close()
    conn.close()
