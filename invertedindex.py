from nltk import word_tokenize
from nltk import sent_tokenize
from nltk import FreqDist
import pandas as pd

sl = ["Oh wow lookie here here.","Holy crap lookie here, this is beautiful","Tushar is the opposite of beautiful here"]

stpwrds = [",",".","!","?","'"]

ml = []
h = []

for i in sl:
    l = []
    for j in word_tokenize(i):
        if j not in stpwrds:
           l.append(j.lower())
           h.append(j.lower())
    ml.append(l)

di = dict(FreqDist(h))

ans = []

for i in list(di.keys()):
    lt = []
    c = 1
    for j in ml:
        ltt = []
        ltt.append("Doc: "+str(c))
        if i in j:
            ltt.append("Count: "+str(j.count(i)))
        else:
            ltt.append(0)
        for k in range(len(j)):
            if i==j[k]:
                ltt.append(k+1)
        lt.append(ltt)
        c = c+1
    ans.append(lt)

d = 0
for i in list(di.keys()):
    print(i,end="          ")
    print(ans[d])
    print()
    d = d + 1

m = input("enter word plssss")
d = 0
for i in list(di.keys()):
    if i==m:
        print(i,end="          ")
        print(ans[d])
    d = d+1
