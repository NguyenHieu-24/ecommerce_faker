from faker import Faker

fake = Faker()

def generate_brands(n=20):
    brands = []
    for _ in range(n):
        brands.append({
            "brand_name": fake.company(),
            "country": fake.country(),
            "created_at": fake.date_time_this_decade()
        })
    return brands
