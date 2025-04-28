def rail_encrypt(text, rails):
    rail = ['' for _ in range(rails)]
    dir = 1
    r = 0
    for ch in text.replace(" ", ""):
        rail[r] += ch
        r += dir
        if r == 0 or r == rails - 1:
            dir *= -1
    return ''.join(rail)

def rail_decrypt(cipher, rails):
    pattern = ['' for _ in range(len(cipher))]
    dir = 1
    r = 0
    for i in range(len(cipher)):
        pattern[i] = r
        r += dir
        if r == 0 or r == rails - 1:
            dir *= -1
    rail = ['' for _ in range(rails)]
    idx = 0
    for i in range(rails):
        for j in range(len(cipher)):
            if pattern[j] == i:
                rail[i] += cipher[idx]
                idx += 1
    out = ''
    pointers = [0]*rails
    for i in pattern:
        out += rail[i][pointers[i]]
        pointers[i] += 1
    return out

e = rail_encrypt("HELLO WORLD", 3)
d = rail_decrypt(e, 3)
print("Encrypted:", e)
print("Decrypted:", d)
