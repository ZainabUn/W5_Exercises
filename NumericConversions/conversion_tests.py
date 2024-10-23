# Description: This script tests various numeric 
# conversion techniques
# Author: Sam Q. Newprogrammer

a = " 101.1 "
b = '55'
c = "402 Stevens"
d = 'Number 5 '

print(a,b,c,d)

a= int(float(a))
print(a,type(a))

a = float(" 101.1 ")
b = int('55')
c = "402 Stevens"
d = 'Number 5 '

print(a,type(a),b,type(b))


a_strip=str(a).strip()
print(a_strip)

d_strip= d.strip()
print(d_strip)


d = 'Number 5 '
b = int('55')
d_split= d.split(' ')
d_int= int(d_split[1])
print(d_int, type(d_int))

print(b+d_int)