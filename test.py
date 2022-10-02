import requests
import mysql.connector
from mysql.connector import Error
import os.path, pickle
'''
pdfs = []
completed = []
for filename in os.listdir("./PDFs"):
    if os.path.isfile(f"./PDFs/{filename}"):
        pdfs.append(int(filename.split(".")[0]))

try:
    # CONNNECTION
    connection = mysql.connector.connect(host='localhost',
                                         database='NTRS',
                                         user='root',
                                         password='ashish99',
                                         )
    cursor = connection.cursor()

    # FETCH AND SELECT
    mySql_select_pdf_Query = "select id from pdfs where short_sum IS NOT NULL;"
    cursor.execute(mySql_select_pdf_Query)
    result = cursor.fetchall()

    for x in result:
        completed.append(x[0])

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        connection.commit()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

with open("completed.pickle","wb") as f:
    pickle.dump(completed,f)

'''
with open("completed.pickle","rb") as f:
    completed=pickle.load(f)

print(completed)

pdfs = []
for filename in os.listdir("./PDFs"):
    if os.path.isfile(f"./PDFs/{filename}"):
        id = str(filename.split(".")[0])
        if id not in completed:
            os.remove(f"./PDFs/{filename}")
