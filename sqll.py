import mysql.connector
mydb=mysql.connector.connect(
    host="locathost",
    port="3306",
    user="root",
    password="spectrum",
    database="assignment"
    
)
if mydb.is_connected():
    print("connection established successfull.")
    mycursor=mydb.cursor()
    mycursor.execute("SELECT* FROM orderss")
    result=mycursor.fetchall()
    mycursor=mydb.cursor()
    mycursor.execute("SELECT*FROM orderss")
    result=mycursor.fetchall()
    for x in result:
        print(x)
        mydb.close()
    
