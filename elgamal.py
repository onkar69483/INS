def power_mod(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

def modinv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return None

# Key generation
p = 23       # prime number
g = 5        # primitive root mod p
x = 6        # private key
y = power_mod(g, x, p)  # public key

# Encryption
m = 13       # message (must be < p)
k = 7        # random (should be coprime to p-1)
c1 = power_mod(g, k, p)
c2 = (m * power_mod(y, k, p)) % p

# Decryption
s = power_mod(c1, x, p)
s_inv = modinv(s, p)
m_decrypted = (c2 * s_inv) % p

print("Original message:", m)
print("Encrypted:", (c1, c2))
print("Decrypted:", m_decrypted)
