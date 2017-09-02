def myfn(i):
    k=str(i**2)
    k=list(k)
    l=list(map(int,k))
    if(l[-1]==4):
        print(i)
l=list(range(1,101))
k=set(map(myfn,l))

    

