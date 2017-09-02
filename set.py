a=set(["krit","karm"])
print "krit" in a
print "Krit" in a
b=a.copy()
print b
b.add("india")
print b.issuperset(a)
'''b.remove("india")
print b'''
c=a|b
print c
c=a&b
print c
