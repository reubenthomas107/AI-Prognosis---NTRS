import requests

headers = {
    'accept': 'application/json',
    # Already added when you pass json= but not when you pass data=
    # 'Content-Type': 'application/json',
}

json_data = {
    'stiType': 'THESIS_DISSERTATION',
    "downloadsAvailable": "true"

}

response = requests.post('https://ntrs.nasa.gov/api/citations/search', headers=headers, json=json_data)

json_response=response.json()
results=json_response["results"]
print(results)

ids=[]
title=[]
abstract=[]
sub_categories=[]
d={}
for i in results:
    ids.append(i["id"])
    title.append(i["title"])
    abstract.append(i["abstract"])
    sub_categories.append(i["subjectCategories"])
d.update({"ids":ids,"title":title,"abstract":abstract,"sub_categories":sub_categories})
import pickle
with open("final_all_ids.pickle","wb") as f:
    pickle.dump(d,f)

    
    
    