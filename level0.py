import json
f=open("Input data/level0.json")
d=json.load(f)
path=[]
m=min(d["restaurants"]["r0"]["neighbourhood_distance"])
i=d["restaurants"]["r0"]["neighbourhood_distance"].index(m)
path.append("r0")
path.append("n"+str(i))
def find_smallestpath(l):
    global path
    for i in range(len(l)):
        if(l[i]!=0 and ('n'+str(i)) not in path):
            m=l[i]
            break
    for i in l:
        if (i!=0 and i<m and ('n'+str(l.index(i))) not in path):
            m=i
    return l.index(m)
while(len(path)!=21):
    i=find_smallestpath(d["neighbourhoods"][path[-1]]["distances"])
    path.append("n"+str(i))
path.append("r0")
p={"v0":{"path":path}}
json_object = json.dumps(p, indent=4)
with open("level0_output.json", "w") as outfile:
    outfile.write(json_object)

