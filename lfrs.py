#linear feedback regsister shift

def binary(a):
	s=''
	for i in range(len(a)):
		s=s+format(mapper[a[i]],'05b')
	return s
def string(a,bit):
	c=''
	for i in range(len(a)/bit):
		c=c+mapper_inverse[int(a[i*bit:(i+1)*bit],2)]
	return c
def lshift(a,x):
	b=''
	for i in range(len(a)-x):
		b=b+a[i+x]
	for i in range(x):
		b=b+a[i]
	return b
def rshift(a,x):
	b=''
	for i in range(len(a)-x):
		b=b+a[i]
	for i in range(len(a)-1,len(a)-x-1,-1):
		b=a[i]+b
	return b
def register_shift(a):
	b=''
	for i in range(len(a)-1):
		b=b+a[i]
	return b
def xor(a,b):
	c=''
	for i in range(len(a)):
		c=c+str(int(a[i])^int(b[i]))
	return c
def selfxor(a,p):
	c=int(a[0])*int(p[0])
	for i in range(1,len(a)):
		c=c^(int(a[i])*int(p[i]))
	return str(c)

#create mapper
mapper=tuple((chr(i+65),i) for i in range(26))+tuple((('0',26),('1',27),('2',28),('3',29),('4',30),('5',31)))
mapper=dict(mapper)
mapper_inverse=((v,k) for k,v in mapper.items())
mapper_inverse=dict(mapper_inverse)

#information about plain-cipher

header='WPI' #message always starts by WPI
header_bin=binary(header)
cipher='J5A0EDJ2B' #cipher-text
cipher_bin=binary(cipher)
p='000011' #self-calculate
initial_state='111111' #self-calculate
key='1' #key initial state

#Keygen-----------------------#
current_state=initial_state
while(len(key)<len(cipher_bin)):
	key=key+current_state[4]
	current_state=selfxor(current_state,p)+register_shift(current_state)

plaintext=xor(cipher_bin,key)
print(string(plaintext,5))