import mysql.connector

# Replace these values with your MySQL database credentials
host = "localhost"
user = "root"
password = "spectrum"
database = "assingments"

# Establish a connection to the MySQL server
connection = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Check if the connection is successful
if connection.is_connected():
    print("Connected to MySQL database")

# Create a cursor object using the cursor() method
cursor = connection.cursor()

# Example: Execute a SQL query
cursor.execute("SELECT*FROM salesman")

# Fetch all the rows using the fetchall() method
rows = cursor.fetchall()

# Iterate and print the rows
for row in rows:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
