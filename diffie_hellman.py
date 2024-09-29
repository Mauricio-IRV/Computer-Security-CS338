g = 7
p = 97
A = 53
B = 82

# Diffie Hellman
b_potential_keys = []
a_potential_keys = []

# Encryption formula: B = g^b mod p
def get_public_x(g, i, p):
	return g**i % p

for x in range(p):
	if get_public_x(g, x, p) == B:
		# x represents a potential "b" value
		b_potential_keys.append(A**x % p)

	if get_public_x(g, x, p) == A:
		# x represents a potential "a" value
		a_potential_keys.append(B**x % p)
	
# Convert to sets and find the intersection
shared_secret = list(set(b_potential_keys) & set(a_potential_keys))

print(shared_secret)
