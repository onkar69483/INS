def poly_encrypt(text, key):
    text = text.upper().replace(" ", "")
    key = (key * (len(text) // len(key) + 1)).upper()
    return "".join(chr((ord(t) + ord(k) - 2*65)%26 + 65) for t, k in zip(text, key))

def poly_decrypt(cipher, key):
    cipher = cipher.upper().replace(" ", "")
    key = (key * (len(cipher) // len(key) + 1)).upper()
    return "".join(chr((ord(c) - ord(k))%26 + 65) for c, k in zip(cipher, key))

e = poly_encrypt("HELLO", "MAN")
d = poly_decrypt(e, "KEY")
print("Encrypted:", e)
print("Decrypted:", d)
