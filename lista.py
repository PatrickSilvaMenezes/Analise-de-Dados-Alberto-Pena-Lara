import math,operator
from functools import reduce



#s1 = {1,3,4,7,9}
#print(s1)
#s2 = range(0,101)
#print(s2)



#s5 =[ x for x in l1]
#print(s5)

#s6 = [ x*2 for x in l1 if x>5 ]
#print("\n listando o dobro dos numeros naturais sendo eles maiores que 5 \n")
#print(s6)

#s7 = [x**2 for x in l1 if x**2>5 ]
#print (s7)

#def Mult2(x):
	#return 2*x
#s8 = map(Mult2,l1)
#print(s8)

#def Soma(x):
#	return x 
#l1 = range(0,1000)
#s9 = reduce(operator.add,l1)
#print(s9)
def MaiorZero(x):
	return x>0

l9 =  list(range(-100,10))
s9 = list(filter(MaiorZero,l9))
print(s9)