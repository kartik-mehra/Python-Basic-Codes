s=input()
k=list(s)
k=set(k)
k=list(k)
k=list(s)

j=1
l=s.find(s[0],j,len(s))
while(l!=-1):
    k[l]='$'
    j=l+1
    l=s.find(s[0],j+1,len(s))
    #print(l)
s=''.join(k)
print(s)
