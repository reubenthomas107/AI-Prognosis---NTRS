import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud

import mysql.connector
from mysql.connector import Error


def generate_wordcloud(pdf_id):
    try:
        # CONNNECTION
        connection = mysql.connector.connect(host='localhost',
                                            database='NTRS',
                                            user='root',
                                            password='ashish99',
                                        )
        cursor = connection.cursor()

        # FETCH AND SELECT
        mySql_select_pdf_Query = "SELECT long_sum FROM pdfs WHERE ID = '{}';".format(pdf_id)
        cursor.execute(mySql_select_pdf_Query)
        result = cursor.fetchall()
        text=' '.join(result[0])
        word_cloud = WordCloud(collocations = False, background_color = 'white').generate(text)
        plt.imshow(word_cloud, interpolation='bilinear')
        plt.axis("off")
        plt.savefig(f"./static/wordclouds/{pdf_id}.png")
        
    
    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    

    