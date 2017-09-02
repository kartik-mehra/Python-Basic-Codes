'''v=["python",'is','awesome']
print v
n=[1,2,3]
print n
a=['apple',3,'krit',2.5]
print a
a=range(1,10)
b=range(10)
c=range(1,10,2)
print a,b,c
print c[3]
print c[-1]
for i in range(0,len(c)):
    print c[i];
'''
'''slicing operation'''
l=['a','b','c','d','e','f']
'''
print l
print l[1:4]
print l[3:]

print l[:4]
print l[-3:]
print l[:-3]
print l[:-3]*2;
fruit=['mango','papaya','kela']
fruit[0]='l';
fruit[-1]='k';
print fruit
l[1:3]=['x','y']
'''
l[4:5]="k"#replace

print l
l=['a','b','c','d','e','f']
l[4:4]='k'#append
print l;

#deleote
del l[1]
print l
del l[1:3]
o=l[1:3]
print l,o
