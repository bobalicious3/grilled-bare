#!/usr/bin/python
def is_prime(number):
	if number % 2 == 0:										# an even number?
		return False										# its even - not prime
	else:
		for i in range(2, number):							# for all the values up to this number value
			if number % i == 0:								# see if it divides into the number value,
				return False								# does, so its not prime
		else:												# no 'return', thus
			return True										# didnt find it in the loop, its a prime

n = int(raw_input("enter a number: "))

for p in range(2, n+1):
	if is_prime(p):
		print ("{0}".format(p))
print('Done')

