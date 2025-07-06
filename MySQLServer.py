import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Connect to MySQL server (no specific database yet)
        connection = mysql.connector.connect(
            host="localhost",
            user="Bertrand",
            password="Bertrand1738"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Create database (will not fail if it already exists)
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("✅ Database 'alx_book_store' created successfully!")

    except Error as e:
        print("❌ Error while connecting to MySQL:", e)

    finally:
        # Ensure proper cleanup
        if 'cursor' in locals():
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("🔒 MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
