import requests
import mysql.connector
from mysql.connector import Error

payload={}
files={}
headers = {
  'Cookie': 'connect.sid=s%3AEhSPBsHTRAzVimlIWlkJQifqq1N_S949.fM7hbzk7DgIHKIR0Q3OyRZNzifAyp4AtdUSUSZHjjoQ'
}

try:
    # CONNNECTION
    connection = mysql.connector.connect(host='localhost',
                                         database='NTRS',
                                         user='root',
                                         password='ashish99',
                                    )
    cursor = connection.cursor()

    # FETCH AND INSERT
    pgs = [str(i) for i in range(0, 10000, 100)]
    for i in pgs:
        url = f"https://ntrs.nasa.gov/api/citations/search?center=CDMS&page.size=100&sort.field=published&page.from={i}&sort.order=desc"
        response = requests.request("GET", url, headers=headers, data=payload, files=files)
        response = response.json()
        for paper in response["results"]:
            if len(paper["downloads"]) > 0:
                cats = ', '.join(paper["subjectCategories"])
                title = paper["title"]
                id = paper["id"]
                abstract = paper["abstract"]

                title = title.replace('"', '')
                cats = cats.replace('"', '')
                abstract = abstract.replace('"', '')

                title = title.replace("'", '')
                cats = cats.replace("'", '')
                abstract = abstract.replace("'", '')

                mySql_insert_pdf_Query = "INSERT INTO pdfs (id, TITLE, ABSTRACT, SUB_CATEGORIES)  VALUES ('{}', '{}', '{}', '{}') ON DUPLICATE KEY UPDATE id='{}';".format(id, str(title), abstract, cats, id)

                result = cursor.execute(mySql_insert_pdf_Query)
        print(f"{i} inserted")
        
except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        connection.commit()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
