from faker import Faker
import random

fake = Faker()

def generate_sellers(n=20):
    sellers = []
    for _ in range(n):
        sellers.append({
            "seller_name": fake.company(),
            "join_date": fake.date_this_decade(),
            "rating": round(random.uniform(3.5, 5.0), 2),
            "country": fake.country()
        })
    return sellers
