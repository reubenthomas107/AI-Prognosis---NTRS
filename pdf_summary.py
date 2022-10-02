from typing import final
import pdfplumber
from transformers import BartTokenizer, BartForConditionalGeneration, BartConfig
import pickle
with open("19830024525_cleaned.pickle","rb") as f:
    final_cleaned_data1=pickle.load(f)
summary=[]
'''
with pdfplumber.open(r'19850003854.pdf') as pdf:
  l=len(pdf.pages)
  
  text=[]
  word_count=0
  for i in range(l):
    extracted_page =pdf.pages[i] 
    extracted_text = extracted_page.extract_text()
    text.append(extracted_text)
'''
extracted_text='. '.join(final_cleaned_data1)

word_count=len(extracted_text.split(" "))

print(word_count)
  
model = BartForConditionalGeneration.from_pretrained('sshleifer/distilbart-cnn-12-6')
tokenizer = BartTokenizer.from_pretrained('sshleifer/distilbart-cnn-12-6')

inputs = tokenizer([extracted_text], truncation=True, return_tensors='pt')

# Generate Summary
summary_ids = model.generate(inputs['input_ids'], num_beams=10,early_stopping=True,min_length=0, max_length=word_count)
summarized_text = ([tokenizer.decode(g, skip_special_tokens=True, clean_up_tokenization_spaces=True) for g in summary_ids])

summary.append(summarized_text)
print(summary)