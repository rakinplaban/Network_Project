import psycopg2
import os

DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://postgres:qnr63363@db_social:5432/social')

try:
    conn = psycopg2.connect(DATABASE_URL)
    print("Connection successful")
except Exception as e:
    print(f"Connection failed: {e}")
# finally:
#     if conn:
#         conn.close()
