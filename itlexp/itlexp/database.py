import mysql.connector

conn = mysql.connector.connect(host = '127.0.0.1',
            user = 'root',
            password = 'password',
            database = "medals")
curr = conn.cursor()

curr.execute("""INSERT INTO medals VALUES (%s,%s,%s,%s,%s)""", (
            "India",1,20,23,44,
        ))

conn.commit()
conn.close()