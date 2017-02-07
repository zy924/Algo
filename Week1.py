import time
import urllib
import re
fh = open("week1.txt")
data = fh.read()
number1 = re.findall('314[0-9]+',data)
number2 = re.findall('271[0-9]+',data)
def Recursive(number1,number2):
	n = len(number1)
	if n == 1:
		return int(number1)*int(number2)
	else:
		b = number1[n/2:]
		a = number1[:n/2]
		d = number2[n/2:]
		c = number2[:n/2]
		product = pow(10,n)*Recursive(a,c)+pow(10,n/2)*(Recursive(a,d)+Recursive(b,c))+Recursive(b,d)
		return product

t = time.time()
print Recursive(number1[0],number2[0])
elapse = time.time()-t
print "elapse=", elapse