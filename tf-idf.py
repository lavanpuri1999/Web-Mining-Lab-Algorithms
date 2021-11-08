from nltk import word_tokenize
import math
import pandas as pd

sl = ["Oh wow lookie here here.","Holy crap lookie here, this is beautiful! Tushar ke bubs","oh wow Tushar is the opposite of beautiful here"]
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

h = set(h)
h = list(h)

tfm = []

for i in ml:
    tf = dict()
    ch = []
    for j in i:
        if j not in ch:
            ch.append(j)
            tf[j] = i.count(j)/len(set(i))
    tfm.append(tf)

idf = dict()

for i in h:
    c = 0
    for j in ml:
        if i in j:
            c = c+1
    idf[i] = math.log((1+len(sl))/c)


cnt = 1
for i in tfm:
    ans = pd.DataFrame(columns=['Term','TF','IDF','TF*IDF'])
    print("----------------DOCUMENT"+str(cnt)+"-------------------------")
    for j in list(i.keys()):
        l = []
        l.append(str(j))
        l.append(str(i[j]))
        l.append(str(idf[j]))
        l.append(str(i[j]*idf[j]))
        ans = ans.append(pd.Series(l,index=['Term','TF','IDF','TF*IDF']),ignore_index=True)
    cnt = cnt +1
    print(ans)
