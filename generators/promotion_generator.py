from faker import Faker
import random

fake = Faker()

def generate_promotions(n=10):
    promos = []
    for _ in range(n):
        start = fake.date_this_year()
        promos.append({
            "promotion_name": fake.catch_phrase(),
            "promotion_type": random.choice(["Flash Sale", "Seasonal"]),
            "discount_type": random.choice(["percent", "fixed"]),
            "discount_value": random.randint(5, 50),
            "start_date": start,
            "end_date": fake.date_between(start_date=start, end_date="+30d")
        })
    return promos
