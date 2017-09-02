'''print('C:\now')
print (r'C:\\now')
print (u'Hello')
'''
str='pypppthon'
#print (str.capitalize())
#print (str.center(11,'_'))
#print (str.count('p',0,len(str)))

#b=str.encode('utf-16','strict')

#print('Encode string = ',b)

#str=str.decode('base64','strict')
#print('decode string = ' + str)

#print( str.endswith('o',0,len(str)))

str='krit {0} tawesome'

str = str.format('krit')
print (str)
'''
str='1today today is krit'
print"Hello {0}, your balance is {1:9.3f}".format('adam',203.23242432)
str1='thisi spy hon'
print str.isalnum()
print str1.isalnum()
str='0'
print str.isdigit()
str=' '
print str.isspace(),'isspace'
print str1.islower()
str1='This Is Python'
print str1.istitle()
print 'isJoin',str.join(str1)
seq=('a','b','c')
s='_'
print s.join(seq)
s='this python'
print s.ljust(15,'_')
print s.rjust(15,'_')
''''''
str='222  1221  pplpp asa  '
print str.lstrip('2')

str='abcsdeA1'
print max(str)
print min(str)

str='This is a python class. It is very interesting'
print str.replace('is','was')
print str.replace('is','was',2)


print str.split()
print str.split(' ',1)'''
str = 'This is krit \n here'
print (str.split(' ',str.count(' ')))
