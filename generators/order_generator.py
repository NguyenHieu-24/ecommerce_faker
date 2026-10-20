from faker import Faker
import random

fake = Faker()

def generate_orders(n=10000, seller_ids=[]):
    orders = []
    for _ in range(n):
        orders.append({
            "order_date": fake.date_time_this_year(),
            "seller_id": random.choice(seller_ids),
            "status": random.choice(["PLACED", "PAID", "SHIPPED", "DELIVERED"]),
            "total_amount": 0  # update sau
        })
    return orders
