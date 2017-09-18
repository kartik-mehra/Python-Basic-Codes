def sum_prime(num,num1):
    s=0
    for j in range(num,num1+1):
        flag=1;
        for i in range(2,int(j/2)+1):
            if(j%i==0):
                flag=0;
                break;
        if(flag==1):
            s=s+j;
    return(s)
a=int(input("enter number1 = "));
b=int(input("enter number2 = "));
print(sum_prime(a,b))
