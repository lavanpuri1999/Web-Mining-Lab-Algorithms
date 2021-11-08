from nltk import word_tokenize
from nltk import sent_tokenize
from nltk import FreqDist
import pandas as pd

sl = ["Oh wow lookie here here.","Holy crap lookie here, this is beautiful","Tushar is the opposite of beautiful here"]

stpwrds = [",",".","!","?","'"]

ml = []
l = []
h = []

for i in sl:
    l = []
    for j in word_tokenize(i):
        if j not in stpwrds:
            h.append(j.lower())
            l.append(j.lower())
    ml.append(l)

h = set(h)
h = list(h)
h.sort()

ans = []

for i in h:
    ltr = []
    ltr.append(i)
    c = 1
    for s in ml:
        ka = []
        ar = []
        ka.append("DOC "+str(c))
        if i not in s:
            ka.append("Count:0")
        if i in s:
            ka.append("Count:"+str(s.count(i)))
            for ch in range(len(s)):
                if s[ch]==i:
                    ar.append(ch+1)
        ka.append(ar)
        ltr.append(ka)
        c = c+1
    ans.append(ltr)

for i in ans:
    print(i)
