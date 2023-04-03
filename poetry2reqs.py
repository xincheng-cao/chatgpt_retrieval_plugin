with open(file='poetry.lock' , mode='r') as f:
    res=f.readlines()

ans=[]

for i in range(len(res)):
    if res[i]=='[[package]]\n':
        ans.append(
            (res[i+1].replace('name = \"','').replace('\"\n',''),
             res[i+2].replace('version = \"','').replace('\"\n','')
             )
        )

with open(file='requirements.txt' , mode='w') as f:
    for e in ans:
        f.write(e[0]+'=='+e[1]+'\n')

print('done')