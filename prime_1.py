num=int(input("enter number1 = "));
num1=int(input("enter number2 = "));
for j in range(num,num1+1):
    flag=1;
    for i in range(2,int(j/2)+1):
        if(j%i==0):
            flag=0;
            break;
    if(flag==1):
        print(j);
