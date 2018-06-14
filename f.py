import primesieve
import numpy as np 


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



##make table readable when doing print(count)
#for x in range(0, base):
#	count[0,x] = x
#	count[x,0] = x


print("\nObserving results for base " + str(base))

#print(count)
for x in range(1, base):
	print("Primes of form " + str(x) + ":x")
	for y in range(1, base):
		if (count[x,y] > 1):
			print("\t"+ str(y) + ":::" + str(count[x,y]))

print("\n")


##are bases generally preferred to be products of first k primes?

