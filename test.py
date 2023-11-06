import mysql.connector


cnx = mysql.connector.connect(user='root', password="",
                              host='localhost',
                              database='stocks_log')

cursor = cnx.cursor()

query = "select ticker from stocks;"

cursor.execute(query)
print(cursor.rowcount)
for (ticker) in cursor:
  print(ticker)

cursor.close()
cnx.close()                              
