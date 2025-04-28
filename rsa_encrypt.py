def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

def rsa_encrypt(msg, e, n):
    return [(ord(ch) ** e) % n for ch in msg]

# Small primes
p = 3
q = 11
n = p * q             # 33
phi = (p - 1) * (q - 1)  # 20
e = 3                 # Public exponent

if gcd(e, phi) != 1:
    raise ValueError("e and phi(n) are not coprime")

# Encrypt
message = "HI"
cipher = rsa_encrypt(message, e, n)
print("Encrypted:", cipher)
