import mysql.connector
from mysql.connector import Error

try:
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        port=3306,
        user="root",  # Replace with your MySQL username
        password="Balaji#2003",  # Replace with your MySQL password
        database="testdb"  # Replace with your database name
    )

    if connection.is_connected():
        print("Connected to MySQL Database!")

        # Prepare a list to store user inputs
        data = []

        while True:
            # Get user input
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            age = int(input("Enter your age: "))

            # Append the data as a tuple to the list
            data.append((name, email, age))

            # Ask if the user wants to add more data
            more = input("Add another user? (yes/no): ")
            if more.lower() != 'yes':
                break

        # SQL query to insert multiple rows
        insert_query = "INSERT INTO users (name, email, age) VALUES (%s, %s, %s);"

        # Create a cursor object
        cursor = connection.cursor()

        # Execute the query with multiple data rows
        cursor.executemany(insert_query, data)

        # Commit the transaction
        connection.commit()

        print(f"{cursor.rowcount} rows inserted successfully!")

except Error as e:
    print("Error while connecting to MySQL:", e)

finally:
    # Close the connection
    if 'connection' in locals() and connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed.")
