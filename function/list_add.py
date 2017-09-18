def l_add(ls):
    a=int(input("ENTER POS : "))
    b=int(input("ENTER NO : "))
    ls[a:a]=[b]
    #ls.insert(a,b)
    return(ls)

def l_del(l):
    a=int(input("ENTER POS : "))
    del l[a]
    return(l)
l=[]
for i in range(0,5):
    l=l_add(l)
print(l)
l=l_del(l)
print(l)
