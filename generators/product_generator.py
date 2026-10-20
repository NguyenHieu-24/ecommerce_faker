from faker import Faker
import random

fake = Faker()

def generate_products(n=200, category_ids=[], brand_ids=[], seller_ids=[]):
    products = []

    for _ in range(n):
        price = random.randint(100_000, 5_000_000)
        discount = random.choice([0, random.randint(10_000, 300_000)])

        products.append({
            "product_name": fake.word().title(),
            "category_id": random.choice(category_ids),
            "brand_id": random.choice(brand_ids),
            "seller_id": random.choice(seller_ids),
            "price": price,
            "discount_price": price - discount if discount else None,
            "stock_qty": random.randint(10, 500),
            "rating": round(random.uniform(3, 5), 1),
            "created_at": fake.date_time_this_year(),
            "is_active": True
        })

    return products
