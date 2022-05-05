import threading
import mysql.connector
#from mysql.connector import Error

def check(aadhaar):
    threading.Timer(5.0, check).start()
    try:

        connection = mysql.connector.connect(host='localhost',
        database= 'mydatabase',
        user='root',
        password='')

        sql_select_Query = "select * from tax_details where aadhaar_no='"+aadhaar+"' order by date DESC LIMIT 1" 
        cursor = connection.cursor()
        cursor.execute(sql_select_Query)

# get all records
        records = cursor.fetchall()
        print("Total number of rows in table: ", cursor.rowcount)
        print("\nPrinting each row")
        for row in records:
            if row[3]!='Paid':
                print('Tax payment is open')
    except mysql.connector.Error as e:

        print("Error reading data from MySQL table", e)

    finally:

        if connection.ts_connected(): 
            connection.close()

            cursor.close()

aadhaar=input()
check(aadhaar)