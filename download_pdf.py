import requests
import mysql.connector
from mysql.connector import Error
import os.path

try:
    # CONNNECTION
    connection = mysql.connector.connect(host='localhost',
                                         database='NTRS',
                                         user='root',
                                         password='ashish99',
                                    )
    cursor = connection.cursor()

    # FETCH AND SELECT
    mySql_select_pdf_Query = "SELECT ID FROM pdfs;"
    cursor.execute(mySql_select_pdf_Query)
    result = cursor.fetchall()

    for x in result:
        if os.path.isfile(f'./PDFs/{x[0]}.pdf'):
            continue
        url = f"https://ntrs.nasa.gov/api/citations/{x[0]}/downloads/{x[0]}.pdf"
        response = requests.request("GET", url)
        with open(f'./PDFs/{x[0]}.pdf', 'wb') as f:
            f.write(response.content)
  
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        connection.commit()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
