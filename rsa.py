# RSA Simulation Program
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Step 1: Choose two small prime numbers (p and q)
p = 61
q = 53

# Step 2: Calculate n and φ(n)
n = p * q
phi = (p - 1) * (q - 1)

# Step 3: Choose public key 'e' such that 1 < e < φ(n) and gcd(e, φ(n)) = 1
e = 17  # Example choice
while gcd(e, phi) != 1:
    e += 1

# Step 4: Calculate private key 'd' such that (d * e) % φ(n) = 1
d = pow(e, -1, phi)

# Encryption Function
def encrypt(message, e, n):
    return [pow(ord(char), e, n) for char in message]

# Decryption Function
def decrypt(ciphertext, d, n):
    return ''.join([chr(pow(char, d, n)) for char in ciphertext])

# Example Usage
message = "HELLO"
ciphertext = encrypt(message, e, n)
decrypted_message = decrypt(ciphertext, d, n)

print("Original Message:", message)
print("Ciphertext:", ciphertext)
print("Decrypted Message:", decrypted_message)
