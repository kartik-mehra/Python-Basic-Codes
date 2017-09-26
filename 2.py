import re
fh = open("kkk.txt")
for l in fh:
    if(re.search(r"k.*oor",l)):
        print(l)
fh.close()
