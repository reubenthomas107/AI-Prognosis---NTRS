import pickle
final_long_summary_dict={}
final_short_summary_dict={}
final_conclusion_summary_dict={}

with open(f"final_all_long_summary2.pickle","rb") as f:
    final_cleaned_data2=pickle.load(f)
    
    print(len(final_cleaned_data2.keys()))
with open(f"final_conclusion_summary2.pickle","rb") as f:
    final_cleaned_data2=pickle.load(f)
    print(len(final_cleaned_data2.keys()))
'''
          


    
with open(f"final_all_short_summary1.pickle","rb") as f:
    final_cleaned_data2=pickle.load(f)
    
    for i,j in final_cleaned_data2.items():
        final_short_summary_dict.update({i:j})
    
    
with open(f"final_all_short_summary.pickle","rb") as f:
    final_cleaned_data2=pickle.load(f)
    
    for i,j in final_cleaned_data2.items():
        final_short_summary_dict.update({i:j})


with open(f"final_conclusion_summary1.pickle","rb") as f:
    final_cleaned_data2=pickle.load(f)
    for i,j in final_cleaned_data2.items():
        final_conclusion_summary_dict.update({i:j})
with open(f"final_conclusion_summary.pickle","rb") as f:
   final_cleaned_data2=pickle.load(f)
   for i,j in final_cleaned_data2.items():
        final_conclusion_summary_dict.update({i:j})

with open(f"final_all_long_summary2.pickle","wb") as f:

    pickle.dump(final_long_summary_dict,f)
with open(f"final_all_short_summary2.pickle","wb") as f:

    pickle.dump(final_short_summary_dict,f)


with open(f"final_conclusion_summary2.pickle","wb") as f:
    pickle.dump(final_conclusion_summary_dict,f)
'''              