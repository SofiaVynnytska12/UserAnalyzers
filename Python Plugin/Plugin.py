import mysql.connector
from mysql.connector import Error
# Function to check your connection. Exception returns Error message
def test_connection(user, password):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            port=3306,
            user=user,
            password=password
        )
        if connection.is_connected():
            print(f"Succes, {user}!")
            cursor = connection.cursor()
            cursor.execute("SHOW DATABASES;")
            databases = cursor.fetchall()
            print(f"This is the list of databases of {user}:")
            for db in databases:
                print(db[0])
    except Error as e:
        print(f"Error occured for user {user}: {e}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            cursor.close()
            connection.close()
            print(f"Connection for {user} is closed .\n")
# Checking Analyzer
test_connection("Analyzer", "UA")
# Checking UserAnalyzers
test_connection("UserAnalyzers", "UA")