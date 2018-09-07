import primesieve
import numpy as np 




#given a number x, a base q, and an array a, 
#Uses formula from Main Conjecture of "Unexpected Biases in the Distribution of Consecutive Primes" to calculate
#expected occurences of pattern denoted by array a in base q under number x

#e.g. pi(10000, 10, [1,3,7]) returns expected number of times that the pattern [[[prime ends in a 1 (base 10), the next
#prime ends in a 3 (base 10), and the next prime ends in a 7 (base 10)]]] occurs under 10000.

def pi(x,q,a):
	r = len(a)
	return (x/np.log(x)/np.power(4,r)) * (1 + c1(q,a)* np.log(np.log(x))/np.log(x) + c2(q,a)/np.log(x) )

def c1(q,a):
	count = 0
	r = len(a)

	for x in range(0,r-1):
		if (a[x] == a[x+1]):
			count+=1

	return 2*( (r-1)/4 - count)


def c2(q,a):
	return c2part1(q,a) + c2part2(q,a)

def c2part1(q,a): 
	sum = 0
	r = len(a) 
	for x in range(0,r-1):
		sum += c2array[ a[x] ,a[x+1] ]
	return sum

def c2part2(q,a):
	sum = 0
	r = len(a)
	
	for j in range(1,r-1): #jump sizes
		count = 0;
		for i in range(0,r - j - 1):
			if (a[i] == a[i+j+1]):
				count += 1
		sum += (1/j)*( (r-1-j)/4  - count )

	return 2 * sum 


#values for c2 constant
c2array = np.zeros((10,10))
c2array[1,1] = -0.3426587
c2array[1,3] = 2.2820316
c2array[1,7] = 1.7606099
c2array[1,9] = -3.6999958
c2array[3,1] = -2.0535924
c2array[3,3] = -0.342658
c2array[3,7] = 0.6356801
c2array[3,9] = 1.7606099
c2array[7,1] = -1.53217076
c2array[7,3] = -0.40724102
c2array[7,7] = -0.34265873
c2array[7,9] = 2.2820316
c2array[9,1] = 3.9284349
c2array[9,3] = -1.5321707
c2array[9,7] = -2.0535924
c2array[9,9] = -0.3426587


np.set_printoptions(suppress=True)


#given array and final, run pi(x,q,a) on all possible patterns of length r, and store scores in final.
def initial(final, r):
	a = [0] * r
	calculate_patterns(final,r,a)

def calculate_patterns(final, r, a):
	if (r == 0):
		b = []
		for x in a:
			b.append(x)

		final.append( (b,pi(100000000,10,a)) ) 
		return 
			

	for x in mod:
		a[r-1] = x
		calculate_patterns(final, r-1, a)
	


#code that analyzes only r=1mod3
"""	if (r % 3 == 1):
		a[r-1] = 3
		calculate_patterns(final, r-1, a)
		a[r-1] = 7
		calculate_patterns(final, r-1, a)
	elif (r % 3 == 2):
		a[r-1] = 9
		calculate_patterns(final, r-1, a)
	elif (r % 3 == 0):
		a[r-1] = 1
		calculate_patterns(final, r-1, a)
"""


mod = [1,3,7,9]

final = []

r = int( input("What size pattern?"))

initial(final, r)

final.sort(key=lambda tup: tup[1], reverse = True)

#print top 20 patterns
limit = 20;
for (x,y) in final:
	if (limit == 0):
		break
	print( str(x) + '::::' + str(y) + '\n') 
	limit -= 1



#print sorted c2 scores by score
pairscores = []
for x in range(0,10):
	for y in range(0,10):
		pairscores.append( (10*x+y ,c2array[x][y] )   )

pairscores.sort(key=lambda tup: tup[1], reverse = True)

for (x,y) in pairscores:
	if (y == 0):
		continue
	print( str(x) + '::::' + str(y) + '\n') 
	

