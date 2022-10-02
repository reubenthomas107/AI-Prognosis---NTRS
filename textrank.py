import pdfplumber
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
def textrank(corpus, ratio=0.2):
    print("inside testrank")

    with pdfplumber.open(f'./PDFs/19950021496.pdf') as pdf:
        l = len(pdf.pages)
        print(l)
        text = []
        word_count = 0
        for i in range(0, 20):
            extracted_page = pdf.pages[i]
            extracted_text = extracted_page.extract_text()

            text.append(extracted_text)
        extracted_text = '. '.join(text)

    corpus = extracted_text
    if type(corpus) is str:
        corpus = [corpus]
        lst_summaries = [gensim.summarization.summarize(txt, ratio=ratio) for txt in corpus]
    print(lst_summaries)
    return lst_summaries

textrank(1)