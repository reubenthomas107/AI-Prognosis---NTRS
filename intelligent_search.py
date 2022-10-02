from txtai.embeddings import Embeddings
import json
import pickle, os
import mysql.connector
from mysql.connector import Error

embeddings = Embeddings({
    "path": "sentence-transformers/all-MiniLM-L6-v2"
})


summary_data={}
pdfs = []
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
    format_strings = ','.join(['%s'] * len(pdfs))
    cursor.execute("SELECT * FROM pdfs WHERE SHORT_SUM IS NOT NULL AND id IN  (%s)" % format_strings,
                   tuple(pdfs))

    # mySql_select_pdf_Query = f"SELECT * FROM pdfs WHERE SHORT_SUM IS NOT NULL AND id IN ({','.join(pdfs)}) ;"
    # cursor.execute(mySql_select_pdf_Query)
    result = cursor.fetchall()

    for x in result:
        summary_data.update({x[0]: x[4] + x[6]})

except mysql.connector.Error as error:
    print("Failed to create table in MySQL: {}".format(error))
finally:
    if connection.is_connected():
        connection.commit()
        cursor.close()
        connection.close()
        print("MySQL connection is closed")

with open("summary_data.pickle","wb") as f:
    pickle.dump(summary_data,f)

values_summary=list(summary_data.values())

with open("values_summary.pickle","wb") as f:
    pickle.dump(values_summary,f)

txtai_data = []
i=0
for text in values_summary:
    txtai_data.append((i, text, None))
    i=i+1
txtai_data[0]
embeddings.index(txtai_data)

with open("embeddings.pickle","wb") as f:
    pickle.dump(embeddings,f)

res = embeddings.search("HYDRODYNAMIOCSFACCELERATEDDROPS", 10)
keys=list(summary_data.keys())
values=list(summary_data.values())
values=list()

values_summary=list(values_summary)
final_list=[]
print(res)
for r in res:
    print(f"Text: {values_summary[r[0]]}")
    k=0
    m=0
    for i in values:
        if i==summary_data[r[0]]:
            m=k
            break
        k+=1
    final_list.append(keys[m])

print(final_list)
