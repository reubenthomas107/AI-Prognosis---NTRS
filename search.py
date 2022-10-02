from txtai.embeddings import Embeddings
import pickle, os

def search_on_keyword(query):
    with open("embeddings.pickle","rb") as f:
        embeddings=pickle.load(f)

    with open("summary_data.pickle","rb") as f:
        summary_data=pickle.load(f)

    with open("values_summary.pickle","rb") as f:
        values_summary=pickle.load(f)

    res = embeddings.search(query, 5)
    keys = list(summary_data.keys())


    final_list = []
    print(res)
    uset = set()
    for r in res:
        uset.add(values_summary[r[0]])
        final_list.append(keys[r[0]])
    print(final_list)
    # print(len(uset))
    return final_list


