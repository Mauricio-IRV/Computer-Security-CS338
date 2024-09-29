# (n_bob = p_bob * q_bob) where p & q are two prime numbers
e_bob, n_bob = [13, 162991]

encrypted_msg = [17645, 100861, 96754, 160977, 120780, 90338, 130962, 74096, 128123, 25052, 119569, 39404, 6697, 82550, 126667, 151824, 80067, 75272, 72641, 43884, 5579, 29857, 33449, 46274, 59283, 109287, 22623, 84902, 6161, 109039, 75094, 56614, 13649, 120780, 133707, 66992, 128221]

# Prime factorization of n_bob i.e of 162991
# https://www.calculatorsoup.com/calculators/math/prime-factors.php
p_q_bob_prime_factorization = [389, 419]

# compute n = lcm(p-1, q-1) where lcm(a, b) is the least common multiple of a and b.
# https://www.calculatorsoup.com/calculators/math/lcm.php
lambda_n_bob = 81092

# e_bob formulation: pick 1 < e < lambda_n such that gcd(e, lambda)
# we already know e is 13 though so we can use it to find d

# Find an integer d such that e_bob * d_bob % lambda_n_bob = 1
# Since we have e_bob and lambda_n_bob, but not d_bob, we will need to use 
# modular multiplicative which can be solved with pythons pow method
# https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
d_bob = pow(e_bob, -1, lambda_n_bob)

print("Private_Key", d_bob)

decrypted_msg = ''

def dec_16bit_to_ascii(dec):
	upper_8_bits = dec & 0xFF
	lower_8_bits = dec >> 8
	
	# Convert to ASCII character
	ascii_upper = chr(upper_8_bits)
	ascii_lower = chr(lower_8_bits)
	
	return ascii_lower + ascii_upper
		
for cipher in encrypted_msg:
	decrypted_dec = cipher**d_bob % n_bob
	decrypted_msg += dec_16bit_to_ascii(decrypted_dec)

print(decrypted_msg)


# Credits: 

# I received a huge help from Changwoo with figuring out that the cipher was coded in 16bit decimal numbers! I was getting such odd characters when I initially tried to convert to ascii and so it was a large help! I would most likely not have realized this otherwise!

# Additionally, I did not really know the mathematical formula to solve for d until Luke (a friend of mine who is good at math) mentioned to me that I'd need to solve for the modular multiplicative!
