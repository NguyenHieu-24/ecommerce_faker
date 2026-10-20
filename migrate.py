import os
from database.connection import get_connection

MIGRATION_DIR = "migrations"

def run_migrations():
    conn = get_connection()
    cursor = conn.cursor()

    for file in sorted(os.listdir(MIGRATION_DIR)):
        if file.endswith(".sql"):
            print(f"Running migration: {file}")
            with open(os.path.join(MIGRATION_DIR, file), "r", encoding="utf-8") as f:
                sql = f.read()
                cursor.execute(sql)
                conn.commit()

    cursor.close()
    conn.close()
    print("✅ All migrations applied")

if __name__ == "__main__":
    run_migrations()

