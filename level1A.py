import json
from itertools import permutations
f=open("Input data/level1a.json")
d=json.load(f)
cap=d["vehicles"]["v0"]["capacity"]
r_dist=d["restaurants"]["r0"]["neighbourhood_distance"]
dict_r={i:r_dist[i] for i in range(len(r_dist))}
sorted_dict_r = dict(sorted(dict_r.items(), key=lambda item: item[1]))
path=[['r0']]
visited=[]
orders=[d["neighbourhoods"][i]["order_quantity"] for i in d["neighbourhoods"]]
capacity=0
co=0
print(sorted_dict_r)
def find_smallestpath(l,x,y):
    for i in range(len(l)):
        if((l[i]!=0 )and (('n'+str(i)) not in y) and (('n'+str(i)) in x )):
            m=l[i]
            break
    for j in range(i+1,len(l)):
        if ((l[j]!=0) and (l[j]<m) and (('n'+str(i)) not in y) and (('n'+str(i)) in x )):
            m=l[j]
    return l.index(m)
def find_path(l):
    path=[l[0]]
    while(len(path)!=len(l)):
        i=find_smallestpath(d["neighbourhoods"][path[-1]]["distances"],l,path)
        path.append("n"+str(i))
    return path

while(len(visited)<20):
    for i in sorted_dict_r:
        capacity+=orders[i]
        if (capacity>=cap):
            capacity=orders[i]
            path[co].append('r0')
            path.append(['r0'])
            co+=1
        path[co].append('n'+str(i))
        visited.append(i)
path[co].append('r0')
print(path)
min_path=[]
for i in path:
    a=find_path(i[1:len(i)-1])
    min_path.append(a)
print(min_path)

    
        
