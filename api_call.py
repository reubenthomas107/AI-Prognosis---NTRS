import requests,pickle
headers = {
    'accept': '*/*',
    'range': '1000',
}
params = {
    'attachment': 'true',
}
completed=[]
try:
    with open("completed.pickle","rb") as f:
        completed=pickle.load(f)
    print(completed)
    with open("final_ids.pickle","rb") as f:
        set1=pickle.load(f)
       
        for i in set1:
            try:
                if i in completed:
                    print("in1")
                    continue
                print(int(i))
                response = requests.get(f'https://ntrs.nasa.gov/api/citations/{i}/downloads/{i}.pdf', params=params, headers=headers)
                with open(f'{i}.pdf', 'wb') as f:
                    f.write(response.content)
                    completed.append(i)
            except:
                with open("completed.pickle","wb") as f:
                    completed=pickle.dump(completed,f)
                continue
except:
    with open("final_ids.pickle","rb") as f:
        set1=pickle.load(f)
        print("in")
        for i in set1:
            try:
                if i in completed:
                    continue
                print(int(i))
                response = requests.get(f'https://ntrs.nasa.gov/api/citations/{i}/downloads/{i}.pdf', params=params, headers=headers)
                with open(f'{i}.pdf', 'wb') as f:
                    f.write(response.content)
                    completed.append(i)
            except:
                with open("completed.pickle","wb") as f:
                    pickle.dump(completed,f)
                continue

        
