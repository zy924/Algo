#Interger Multiplication

import time
##input
number1 = '3141592653589793238462643383279502884197169399375105820974944592'
number2 = '2718281828459045235360287471352662497757247093699959574966967627'

#Common Recursive Call Method
def Recursive(number1,number2):
	n = max(len(number1),len(number2))
	if n == 1:
		return int(number1)*int(number2)
	else:
		b = number1[n/2:]
		a = number1[:n/2]
		d = number2[n/2:]
		c = number2[:n/2]
		product = pow(10,n)*Recursive(a,c)+pow(10,n/2)*(Recursive(a,d)+Recursive(b,c))+Recursive(b,d)
		return product

#Karatsuba Multiplication Method
def Kara_Multi(number1,number2):
	n = max(len(number1),len(number2))
	if n == 1:
		return int(number1)*int(number2)
	else:
		b = number1[n/2:]
		a = number1[:n/2]
		d = number2[n/2:]
		c = number2[:n/2]
		ac = Recursive(a,c)
		bd = Recursive(b,d)
		
		##when calculating a+b, remembering to transform a and b into int type
		product = pow(10,n)*ac+pow(10,n/2)*(Recursive(str(int(a)+int(b)),str(int(c)+int(d)))-ac-bd)+bd 
		return product

if __name__ == '__main__':
	assert Recursive('20','40')==800, "Recursive is false" #simple test
	assert Kara_Multi('40','20')==800, "Kara is false"
	
	# estimate elapse time
	t = time.time()
	print ("The result is: \n%.d") %(Recursive(number1,number2))
	print ("Time elapse=%.10f") %(time.time()-t)
	
	#estimate elapse time
	t = time.time()
	print ("The result is: \n%.d") %(Kara_Multi(number1,number2))
	print ("Time elapse=%.10f") %(time.time()-t)