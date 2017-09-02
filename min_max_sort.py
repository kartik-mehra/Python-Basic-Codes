l=[]
n=int(input("ENTER SIZE : "))
for i in range(0,n):
    a=int(input("ENTER NO : "))
    l.append(a)
p=sorted(l)
print(p[0],p[-1])
