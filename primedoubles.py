import primesieve
import numpy as np 

#The following code was used to collect data on consecutive primes. Specifically, it iterated through all primes
#under 10000000 and kept count of all instances of a prime ending in x, and the next prime ending in y.

#e.g. kept count of all instances of a prime ending in 1, and the next prime ending in 3. 
# **As well as all other digit pair combinations.


np.set_printoptions(suppress=True)

base = int( input("What base?"))

count = np.zeros((base,base))   # Create an array of all zeros

prev = 0
curr = 0

it = primesieve.Iterator()
prime = it.next_prime()

# Iterate over the primes below blah
while prime < 10000000:
    curr = prime % base
    count[prev,curr] += 1

    prev = curr

    prime = it.next_prime()



print("\nObserving results for base " + str(base))

for x in range(1, base):
	print("Primes of form " + str(x) + ":x")
	for y in range(1, base):
		if (count[x,y] > 1):
			print("\t"+ str(y) + ":::" + str(count[x,y]))



##are bases generally preferred to be products of first k primes?

