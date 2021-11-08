import math

def gamma(m):
    return ((len(str(bin(m)[2:]))-1)*'0')+bin(m)[2:]

def delta(m):
    n = 1 + math.floor(math.log(m,2))
    return gamma(n)+bin(m)[3:]

def goulomb(m,b):
    q = m//b
    q1 = q*'0'+str(1)
    i = math.floor(math.log(b,2))
    r = m - q*b
    d = int(math.pow(2,i+1) - b)
    if r<d:
        r1 = bin(r)[2:2+i+1]
        if(len(r1)<i):
            r1 = '0'*(i-len(r1)) + str(r1)
    else:
        r1 = bin(r+d)[2:2+i+2]
        if(len(r1)<i+1):
            r1 = '0'*(i-len(r1)+1) + str(r1)
    return q1+r1

for i in range(1,31):
    print(i,end=" ")
    print(gamma(i),end=" ")
    print(delta(i),end=" ")
    print(goulomb(i,10),end=" ")
    print()

print()
print(delta(56))
