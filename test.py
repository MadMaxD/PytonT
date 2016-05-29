i=int(input())
f=[]
ml=[]
for k in range(1,i+1):
    if(i-k>0):
        f.append([k]*k)
        i-=k
    else:
        f.append([k]*i)
        i-=i
        break
for g in f:
    ml+=g
for g in ml:
    print(g, end=" ")




