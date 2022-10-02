import pickle,requests
ids=[]
for j in range(100):
    response1 = requests.get('https://ntrs.nasa.gov/search?center=CDMS&stiTypeDetails=Thesis%2FDissertation')

    with open(f'Thesis.txt{j}', 'wb') as f:
        f.write(response1.content)
    print(response1.content)
    l1=[]
    l=[]
    with open(f'Thesis.txt{j}', 'r') as f:
        k=0
        for i in f.readlines():
            k+=1
            if k==37:
                
                l=i.split(",&q;submissionId&q;:")
                
    



    for i in range(0,len(l)):
        ids.append(l[i][:11])
final_ids=set(ids)





with open("final_ids.pickle","wb") as f:
    pickle.dump(final_ids,f)

