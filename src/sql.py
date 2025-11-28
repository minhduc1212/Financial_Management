import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="minhduc!1@2"
)

mycursor = mydb.cursor()

mycursor.execute("DROP DATABASE Test")