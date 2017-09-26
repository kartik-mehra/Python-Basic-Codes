import re
x=re.search(r"cat","a happy cat")
print(x)
#".at" matches keyword like cat mat hat
for i in range(0,3):
    x=re.search(".at"," lllat\n happy \ncat\n lllat")
    print(x)
