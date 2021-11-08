import numpy as np
a = [[0,0,1,0,0,0],[0.5,0,0.5,0,0,0],[1,0,0,0,0,0],[0,0,0,0,0.5,0.5],[0,0,0.5,0.5,0,0],[0,0,0,0.5,0.5,0]]
M = np.array(a)
H = np.transpose(a)
N = np.array([0.85,0.85,0.85,0.85,0.85,0.85])
res = N
ans = []
for i in range(7):
    print("iteration",i+1)
    res = np.dot(H,res)
    if(i==0):
        c = res
    print(res)
v = c.tolist()
v.sort(reverse=True)
o = c.tolist()
for i in range(6):
    print("The rank of page number "+str(i+1)+" is "+str(v.index(o[i])+1))
