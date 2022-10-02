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
    print(text)
    return text

def text_rank_conclusion_summary(id,final_cleaned_data1):
    
    
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

    final_conclusion_summary.update({id:final_summary})
def text_rank_short_summary(id,final_cleaned_data1):
    
    
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

    final_short_summary.update({id:final_summary})

    
def text_rank_long_summary(id,final_cleaned_data1):
    
    try:
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
                
                sentence=clean_content(sentence)
            
                sentence=process_sentences(sentence)
                
                final_cleaned_data2.append(sentence)
            text_rank_conclusion_summary(id,final_cleaned_data2)
    except:
        pass
        
    
    '''
    with open(f"cleaned_short_summary_{id}.pickle","wb") as f:

        pickle.dump(final_cleaned_data2,f)

    with open(f"cleaned_short_summary_{id}.pickle","rb") as f:
        final_cleaned_data2=pickle.load(f)
    print("Short Summary:  \n"+final_cleaned_data2)
    # Convert PDF to Text
    '''
def long_summary(id):
    try:
        with pdfplumber.open(f'{id}.pdf') as pdf:
            l=len(pdf.pages)
            
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
    '''
    with open(f"cleaned_long_{id}.pickle","wb") as f:

        pickle.dump(final_cleaned_data,f)

    with open(f"cleaned_long_{id}.pickle","rb") as f:
        final_cleaned_data1=pickle.load(f)
   '''

with open("final_ids.pickle","rb") as f:
        set1=pickle.load(f)
          
with open("final_all_ids.pickle","rb") as f:
        val=pickle.load(f)
        set2=val.get("ids")
for i in set1:
    if i not in set2:
        set2.append(i)
print("this",len(set(set2)))
print(set1,set2)
'''
for i in set2:
    print()
    short_summary(i)
    long_summary(i)
    conclusion_summary(i)

'''
'''
with open(f"final_all_long_summary1.pickle","wb") as f:

    pickle.dump(final_long_summary,f)
with open(f"final_all_short_summary1.pickle","wb") as f:

    pickle.dump(final_short_summary,f)


with open(f"final_conclusion_summary1.pickle","wb") as f:
    pickle.dump(final_conclusion_summary,f)

'''
with open(f"final_all_long_summary1.pickle","rb") as f:
    final_cleaned_data2=pickle.load(f)
    
    print(len(final_cleaned_data2.keys()))
          
          


    
with open(f"final_all_short_summary1.pickle","rb") as f:
    final_cleaned_data2=pickle.load(f)
    
    print(len(final_cleaned_data2.keys()))


with open(f"final_conclusion_summary.pickle","rb") as f:
    final_conclusion_summary1=pickle.load(f)
    




'''
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx

# Summary using frequencies

def sentence_similarity(sent1, sent2, stopwords=None):
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1.split(" ")]
    sent2 = [w.lower() for w in sent2.split(" ")]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = [0] * len(all_words)
    vector2 = [0] * len(all_words)
 
    # build the vector for the first sentence
    for w in sent1:
        
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    # build the vector for the second sentence
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
 
    return 1 - cosine_distance(vector1, vector2)
def build_similarity_matrix(sentences, stop_words):
    # Create an empty similarity matrix
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: #ignore if both are same sentences
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)
            
    return similarity_matrix
def generate_summary(final_cleaned_data1, top_n=5):
    stop_words = stopwords.words('english')
    summarize_text = []

    # Step 1 - Read text anc split it
    
    sentences=final_cleaned_data1
    print(len(sentences))
    # Step 2 - Generate Similary Martix across sentences
    sentence_similarity_martix = build_similarity_matrix(sentences, stop_words)
    print(sentence_similarity_martix)
    # Step 3 - Rank sentences in similarity martix
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_martix)
    scores = nx.pagerank(sentence_similarity_graph)

    # Step 4 - Sort the rank and pick top sentences
    ranked_sentence = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)    
    print("Indexes of top ranked_sentence order are ", ranked_sentence)    

    for i in range(top_n):
      summarize_text.append("".join(ranked_sentence[i][1]))

    # Step 5 - Offcourse, output the summarize texr
    summary=". ".join(summarize_text)
    print("Summarize Text: \n",summary)
    with open("19830024525_summary.txt","w") as f:
        f.writelines(summary)
        
generate_summary(final_cleaned_data1[:100])
'''
'''
freq_table=dict()
def calculate_freq(final_cleaned_data1):
    text=' '.join(final_cleaned_data1)
    print(len(list(text)))
    for word in text.split(" "):
        word=word.lower()
        freq_table[word]=freq_table.get(word,0)+1

sentence_value=dict()
def sentence_freq():
    
    for sentence in final_cleaned_data1:
        words=sentence.split(" ")
        words=[i.lower() for i in words]
        for word,freq in freq_table.items():
            if word in words:
                if sentence in sentence_value:
                    sentence_value[sentence]+=freq
                else:
                    sentence_value[sentence]=freq
def summary():
    sumvalues=0
    for sentence in sentence_value:
        sumvalues+=sentence_value[sentence]
    average=int(sumvalues/len(final_cleaned_data1))
    summary=''
    for sentence in final_cleaned_data1:
        if (sentence in sentence_value) and (sentence_value[sentence] >(10*average)):
            summary+=". "+sentence
    print(len(list(summary)))
    with open("summary.txt","w") as f:
        f.write(summary)
calculate_freq(final_cleaned_data1)
sentence_freq()
summary()

''' 
    





