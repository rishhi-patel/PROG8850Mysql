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

try:
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()

    with open('add_departments.sql', 'r') as file:
        sql_script = file.read()

    statements = sql_script.strip().split(';')

    for stmt in statements:
        stmt = stmt.strip()
        if stmt:
            cursor.execute(stmt)
            print(f"Executed: {stmt}")

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
