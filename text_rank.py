from cgitb import text
from typing import final
import pdfplumber
from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig
import pickle
import gensim   
from Seq2Ser import *
with open("19830024525_cleaned_10.pickle","rb") as f:
    final_cleaned_data1=pickle.load(f)
print(len(final_cleaned_data1))
extracted_text = '. '.join(final_cleaned_data1)
def textrank(corpus, ratio=0.2):    
    if type(corpus) is str:        
       corpus = [corpus]    
    lst_summaries = [gensim.summarization.summarize(txt,  
                     ratio=ratio) for txt in corpus]    
    return lst_summaries
val=textrank(extracted_text)
print(len(val[0].split(".")))
summary=str(val[0])

with open("summary3.txt","w") as f:
    f.write(str(summary))
with open("summary3.txt","r") as f:
    l=[]
    d={}
    
    for i in f.readlines():
        d[i]=d.get(i,0)+1
    final_summary=' '.join(d.keys())

    

with open("final_summary.txt","w") as f:
    f.write(final_summary)
