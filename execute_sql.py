import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

load_dotenv()

db_config = {
    'host': os.getenv('DB_HOST'),
    'port': 3306,
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD'),
    'database': os.getenv('DB_NAME', 'companydb')
}

print("DB config:", db_config)


with open('create_projects.sql', 'r') as file:
    sql_script = file.read()


statements = sql_script.strip().split(';')

try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    for stmt in statements:
        stmt = stmt.strip()
        if stmt:
            cursor.execute(stmt)
            print(f"Executed: {stmt}")

    cursor.execute("""
        SELECT COUNT(*)
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME = 'projects'
          AND COLUMN_NAME = 'budget';
    """)
    column_exists = cursor.fetchone()[0]

    if column_exists == 0:
        cursor.execute("""
            ALTER TABLE projects
            ADD COLUMN budget DECIMAL(10,2);
        """)
        print("Added 'budget' column.")
    else:
        print("'budget' column already exists — skipping ALTER TABLE.")

    connection.commit()
    print("All changes committed successfully.")

except Error as e:
    print(f"Error: {e}")

finally:
    try:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection closed.")
    except NameError:
        print("Connection was never established — check error above.")
