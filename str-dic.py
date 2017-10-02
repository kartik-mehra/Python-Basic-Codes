s=input()
a=list(s)
a=set(a)
a=list(a)

l=[]
for i in a:
    l.append([i,s.count(i)])
l.sort(key= lambda x:x[1])
l.reverse()
print(l)
