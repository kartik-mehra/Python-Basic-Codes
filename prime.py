num=int(input("enter number = "));
flag=1;
for i in range(2,int(num/2)+1):
    if(num%i==0):
        flag=0;
        break;
if(flag==1):
    print("PRIME");
else:
    print("NOT PRIME");
    
    

