def myFun(a):
    s=0;
    for i in range(1,a+1):
        if(i%2!=0):
            s=s+i
    return(s)
a = int(input("ENTER NO : "))
print(myFun(a))
