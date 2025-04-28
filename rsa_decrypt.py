def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def modinv(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

def rsa_decrypt(cipher, d, n):
    return ''.join([chr((ch ** d) % n) for ch in cipher])


p = 3
q = 11
n = p * q             # 33
phi = (p - 1) * (q - 1)  # 20
e = 3                 # Public exponent

if gcd(e, phi) != 1:
    raise ValueError("e and phi(n) are not coprime")

d = modinv(e, phi)    # Private exponent

# Encrypting the message "HI"
message = "HI"
cipher = [(ord(ch) ** e) % n for ch in message]
print("Encrypted:", cipher)

# Decrypt the message
decrypted_message = rsa_decrypt(cipher, d, n)
print("Decrypted:", decrypted_message)
