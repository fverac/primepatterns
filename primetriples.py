import primesieve
import numpy as np 

#The following code was used to collect data on consecutive primes. Specifically, it iterated through all primes
#under 10000000 and kept count of all instances of a prime ending in x, the next prime ending in y,
#and the next prime ending in z

#e.g. kept count of all instances of a prime ending in 1, the next prime ending in 3, and the next prime ending in 7 
# **As well as all other digit triple combinations.

np.set_printoptions(suppress=True)

base = int( input("What base?"))

count = np.zeros( (base,base,base) )   # Create an array of all zeros


prev = 0
mid = 0
curr = 0


it = primesieve.Iterator()
prime = it.next_prime()

# Iterate over the primes below blah
while prime < 1000000:
    curr = prime % base
    count[prev,mid,curr] += 1

    prev = mid
    mid = curr

    prime = it.next_prime()


print("\nObserving results for base " + str(base))

for x in range(1, base):
	print("Primes of form " + str(x) + ":x:y")
	for y in range(1, base):
		for z in range(1,base):
			if (count[x,y,z] > 1):
				print("\t"+ str(y) + "." + str(z) + ":::" + str(count[x,y,z]))



##are bases generally preferred to be products of first k primes?

