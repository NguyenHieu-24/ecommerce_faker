from faker import Faker
from data.static.categories import MAIN_CATEGORIES, SUB_CATEGORIES

fake = Faker()

def generate_categories():
    categories = []

    # level 1
    for name in MAIN_CATEGORIES:
        categories.append({
            "category_name": name,
            "parent_category_id": None,
            "level": 1,
            "created_at": fake.date_time_this_year()
        })

    # level 2
    for parent in MAIN_CATEGORIES:
        for sub in SUB_CATEGORIES[parent]:
            categories.append({
                "category_name": sub,
                "parent_category_name": parent,  # dùng tên để map FK
                "level": 2,
                "created_at": fake.date_time_this_year()
            })

    return categories
