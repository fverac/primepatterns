import primesieve
import numpy as np 


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

