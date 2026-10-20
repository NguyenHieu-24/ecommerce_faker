import random

def generate_order_items(order_ids, product_ids):
    items = []
    for order_id in order_ids:
        for _ in range(random.randint(1, 5)):
            qty = random.randint(1, 3)
            price = random.randint(100_000, 2_000_000)
            items.append({
                "order_id": order_id,
                "product_id": random.choice(product_ids),
                "quantity": qty,
                "unit_price": price,
                "subtotal": qty * price
            })
    return items
