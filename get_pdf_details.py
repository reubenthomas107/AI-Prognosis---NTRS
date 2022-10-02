from numpy import result_type
import requests
import mysql.connector
from mysql.connector import Error
import os.path

def fetch_pdf_details(res_list):
    try:
        # CONNNECTION
        connection = mysql.connector.connect(host='localhost',
                                            database='NTRS',
                                            user='root',
                                            password='ashish99',
                                        )
        cursor = connection.cursor()

        ids = res_list

        format_strings = ','.join(['%s'] * len(ids))
        cursor.execute("SELECT * FROM pdfs WHERE id IN  (%s)" % format_strings,
                    tuple(ids))

        result = cursor.fetchall()

        ids = []
        title = []
        abstract = []
        cats = []
        short_sum = []
        long_sum = []
        con_sum = []

        for res in result:
            ids.append(res[0])
            title.append(res[1])
            abstract.append(res[2])
            cats.append(res[3])
            short_sum.append(res[4])
            long_sum.append(res[5])
            con_sum.append(res[6])
        
        final_res = {"ids": ids, "title": title, "abstract": abstract, "cats": cats, "short_sum": short_sum, "long_sum": long_sum, "con_sum": con_sum}

        return final_res 
           
    
    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
