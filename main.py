# Importing mysql connector module
import mysql.connector
# Making MySQL connection object
mycon = mysql.connector.connect(
	host='localhost', user='root',
	password='password',
	database='sboutique'
    )
# Making MySQL cursor object
mycur = mycon.cursor()
