from typing import final
import pdfplumber
from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig
import pickle
import gensim 
import nltk  
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mysql.connector
from mysql.connector import Error

def cleaned_data(pdf_id):
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
        
        final_cleaned_data1=text
        lst_tokens = nltk.tokenize.word_tokenize(final_cleaned_data1)
        ngrams = [1]
    
        bigrams=list(nltk.bigrams(lst_tokens))
        d={}
        for i in bigrams:
            d[i]=d.get(i,0)+1
    
        ## calculate
        df1=pd.DataFrame(columns=["Bigrams","Freq"])
        df1["Bigrams"]=d.keys()
        df1["Freq"]=d.values()

        df1=df1.sort_values(by="Freq",ascending=False)
        ax = sns.barplot(x="Freq", y="Bigrams", dodge=False,data=df1.head(10))
        figure = plt.gcf()
        figure.set_size_inches(10, 6)
        plt.savefig(f"./static/bigrams/{pdf_id}.png", dpi=100)
        print("\n\n SAVED \n\n")
        
    except mysql.connector.Error as error:
        print("Failed to create table in MySQL: {}".format(error))
    finally:
        if connection.is_connected():
            connection.commit()
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    

    
 

