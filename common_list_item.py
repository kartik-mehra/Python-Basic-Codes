l=[1,2,3,4]
p=[0,5,6,7]
l=l+p
f=1;
for i in range(0,len(l)-1):
    if(l.count(l[i])==2):
        print("TRUE")
        f=0
        break
if(f==1):
    print("FALSE")
