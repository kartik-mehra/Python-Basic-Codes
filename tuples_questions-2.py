# tuples programs

#WAP to swap two values using tuple assignment
val1=10
val2=20
print("val1= ",val1,"val2=",val2)
(val1,val2)=(val2,val1)
print("******")
print("val1= ",val1,"val2=",val2)

#WAP that scans an email address and forms a tuple of user name and domain name.
print("Enter the email address:")
add=input("Enter the email address:")
username,domain_name=add.split("@")
print("Username = ",username)
print("Domain name = ",domain_name)

#WAP that has two sequences. First which stores some questions and second stores the corresponding answers.
#Use zip() function to form avalid question answer series.
ques=["Roll_no","name","course"]
ans=["18","vidhi","CSE"]
for i,j in zip(ques,ans):
    print("What is your ",i," ?")
    print("My ",i,"is : ",j)
          
      
