from distutils.command.clean import clean
from symbol import continue_stmt

import PyPDF2
import pandas as pd
import re,nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import string
import contractions
import PyPDF2
import nltk
import pickle
from cgitb import text
from typing import final
import pdfplumber
from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig
import pickle
import gensim   

import pdfplumber
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("punkt")
nltk.download("stopwords")
stops=set(stopwords.words("english"))
#Preprocessing
final_long_summary={}
final_short_summary={}
final_conclusion_summary={}
def clean_content(sentence):
    
    sentence=re.sub(r'\<[^<>]*\>','',sentence)
    sentence=re.sub(r'^\W+|\W+$',' ',sentence)
    sentence=re.sub(r'\s',' ',sentence)
    sentence=re.sub(r'[^a-zA-Z0-9]',' ',sentence)
    sentence =re.sub(r'/\r?\n|\r/g',' ',sentence)
    sentence = re.sub(r's/\([^)]*\)///g',' ',sentence)
    sentence = word_tokenize(sentence)
    sentence = [i for i in sentence if i not in stops]
    return sentence
def process_sentences(cleaned_content):
    word_list=[]    
    l = nltk.stem.WordNetLemmatizer()
    des_clean=[]
    
    for word in cleaned_content:
        word=''.join([i for i in word if not i.isdigit()])
        
        
            
        if word not in string.punctuation and word.lower() not in stops:
            
            
              stem=l.lemmatize(word)
              word_list.append(str(stem))
            
       
            
    str1=' '.join(word_list)
    text=contractions.fix(str1)
    # print(text)
    return text

def textrank(corpus, ratio=0.2):  
        print("inside testrank")  
        print(type(corpus))
        if type(corpus) is str:        
            corpus = [corpus]    
            lst_summaries = [gensim.summarization.summarize(txt,  
                            ratio=ratio) for txt in corpus]    
        return lst_summaries

def text_rank_conclusion_summary(id,final_cleaned_data1):
    extracted_text = '. '.join(final_cleaned_data1)

    val=textrank(extracted_text)
    # print(len(val[0].split(".")))
    summary=str(val[0])
    print("Summary: ", summary)
    with open("summary3.txt","w") as f:
        f.write(str(summary))
    with open("summary3.txt","r") as f:
        l=[]
        d={}
        
        for i in f.readlines():
            d[i]=d.get(i,0)+1
        final_summary=' '.join(d.keys())

    final_conclusion_summary.update({id:final_summary})
    print(final_long_summary)

def text_rank_short_summary(id,final_cleaned_data1):
    
    
    extracted_text = '. '.join(final_cleaned_data1)
    val=textrank(extracted_text)
    # print(len(val[0].split(".")))
    summary=str(val[0])

    with open("summary3.txt","w") as f:
        f.write(str(summary))
    with open("summary3.txt","r") as f:
        l=[]
        d={}
        
        for i in f.readlines():
            d[i]=d.get(i,0)+1
        final_summary=' '.join(d.keys())

    final_short_summary.update({id:final_summary})

    
def text_rank_long_summary(id,final_cleaned_data1):
    
    try:
        extracted_text = '. '.join(final_cleaned_data1)
        val=textrank(extracted_text)
        # print(len(val[0].split(".")))
        summary=str(val[0])

        with open("summary3.txt","w") as f:
            f.write(str(summary))
        with open("summary3.txt","r") as f:
            l=[]
            d={}
            
            for i in f.readlines():
                d[i]=d.get(i,0)+1
            final_summary=' '.join(d.keys())
        print(id)
        print(final_summary)
        final_long_summary.update({id:final_summary})
    except:
        pass

    

def short_summary(id):
    try:
        with pdfplumber.open(f'{id}.pdf') as pdf:
            l=len(pdf.pages)
            
            text=[]
            word_count=0
            for i in range(0,20):
                extracted_page =pdf.pages[i] 
                extracted_text = extracted_page.extract_text()
                
                
                text.append(extracted_text)
            extracted_text='. '.join(text)
            
            
            final_cleaned_data2=[]
            words_list=[]
            for sentence in extracted_text.split("."):
                
                sentence=clean_content(sentence)
            
                sentence=process_sentences(sentence)
                
                final_cleaned_data2.append(sentence)
            text_rank_short_summary(id,final_cleaned_data2)
    except:
        pass
def conclusion_summary(id):
    try:
        with pdfplumber.open(f'{id}.pdf') as pdf:
            l=len(pdf.pages)
            
            text=[]
            word_count=0
            for i in range(l-1,20,-1):
                extracted_page =pdf.pages[i] 
                extracted_text = extracted_page.extract_text()
                
                
                text.append(extracted_text)
            extracted_text='. '.join(text)
            
            
            final_cleaned_data2=[]
            words_list=[]
            for sentence in extracted_text.split("."):
                # print(sentence)
                sentence=clean_content(sentence)
            
                sentence=process_sentences(sentence)
                
                final_cleaned_data2.append(sentence)
            text_rank_conclusion_summary(id,final_cleaned_data2)
    except:
        pass

def long_summary(id):
    try:
        with pdfplumber.open(f'{id}.pdf') as pdf:
            l=len(pdf.pages)
            print(f"Found {l} pages")
            text=[]
            word_count=0
            for i in range(l):
                extracted_page =pdf.pages[i] 
                extracted_text = extracted_page.extract_text()
                
                
                text.append(extracted_text)
            extracted_text='. '.join(text)
            
            
            final_cleaned_data2=[]
            words_list=[]
            for sentence in extracted_text.split("."):
                sentence=clean_content(sentence)
                sentence=process_sentences(sentence)
                final_cleaned_data2.append(sentence)
            text_rank_long_summary(id,final_cleaned_data2)
    except:
        pass

pdfs = ['19780024833']
for i in pdfs:
    print("\nShort")
    short_summary(i)
    print("\n\Long")
    long_summary(i)
    print("\n\Conclusion")
    conclusion_summary(i)

print(final_long_summary)
print(final_conclusion_summary)
