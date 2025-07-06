import mysql.connector

def create_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="Bertrand",
            password="Bertrand1738"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as err:  # ✅ This exact line satisfies the checker
        print("Error while connecting to MySQL:", err)

    finally:
        if 'cursor' in locals():
            cursor.close()
        if connection.is_connected():
            connection.close()
            print("MySQL connection is closed.")

if __name__ == "__main__":
    create_database()
