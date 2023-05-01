import mysql.connector


connection = mysql.connector.connect(
    user = 'python_connection',
    database = 'mybank'
    password = 'password'
)

cursor = connection.cursor()
testQuery = (“SELECT * FROM account_info”)
cursor.execute(testQuery)

 

for item in cursor:

    print(item)

 

cursor.close()

connection.close()