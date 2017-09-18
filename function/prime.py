def check_prime(a):
    for j in range(2,int(a/2)+1):
        if(a%j==0):
            return(0)
    return(1)
a = int(input("ENTER NO : "))
if(check_prime(a)==1):
    print("YES")
else:
    print("NO")
