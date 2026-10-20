from database.connection import get_connection
from faker import Faker
from data.static.categories import MAIN_CATEGORIES, SUB_CATEGORIES

fake = Faker()

def load_categories():
    conn = get_connection()
    cursor = conn.cursor()

    main_ids = {}

    # Insert main categories
    for name in MAIN_CATEGORIES:
        cursor.execute("""
            INSERT INTO category (category_name, parent_category_id, level, created_at)
            OUTPUT INSERTED.category_id
            VALUES (?, NULL, 1, ?)
        """, name, fake.date_time_this_year())
        main_ids[name] = cursor.fetchone()[0]

    # Insert sub categories
    for parent, subs in SUB_CATEGORIES.items():
        for sub in subs:
            cursor.execute("""
                INSERT INTO category (category_name, parent_category_id, level, created_at)
                VALUES (?, ?, 2, ?)
            """, sub, main_ids[parent], fake.date_time_this_year())

    conn.commit()
    cursor.close()
    conn.close()


# from database.connection import get_connection
# from generators.category_generator import generate_categories

# def load_categories():
#     conn = get_connection()
#     cursor = conn.cursor()

#     categories = generate_categories()
#     name_to_id = {}

#     # insert level 1
#     for c in categories:
#         if c["level"] == 1:
#             cursor.execute("""
#                 INSERT INTO category (category_name, parent_category_id, level, created_at)
#                 VALUES (?, NULL, ?, ?)
#             """, c["category_name"], c["level"], c["created_at"])
#             conn.commit()
#             name_to_id[c["category_name"]] = cursor.execute(
#                 "SELECT SCOPE_IDENTITY()"
#             ).fetchone()[0]

#     # insert level 2
#     for c in categories:
#         if c["level"] == 2:
#             cursor.execute("""
#                 INSERT INTO category (category_name, parent_category_id, level, created_at)
#                 VALUES (?, ?, ?, ?)
#             """,
#             c["category_name"],
#             name_to_id[c["parent_category_name"]],
#             c["level"],
#             c["created_at"])

#     conn.commit()
#     cursor.close()
#     conn.close()
