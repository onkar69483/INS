def col_encrypt(text, key):
    text = text.replace(" ", "")
    cols = len(key)
    rows = (len(text) + cols - 1) // cols
    padded = text.ljust(rows * cols, 'X')
    matrix = [padded[i:i+cols] for i in range(0, len(padded), cols)]
    order = sorted(range(cols), key=lambda k: key[k])
    return ''.join(''.join(row[i] for row in matrix) for i in order)

def col_decrypt(cipher, key):
    cols = len(key)
    rows = (len(cipher) + cols - 1) // cols
    order = sorted(range(cols), key=lambda k: key[k])
    col_lens = [rows] * cols
    extra = rows * cols - len(cipher)
    for i in reversed(order):
        if extra > 0:
            col_lens[i] -= 1
            extra -= 1
    idx = 0
    cols_data = [''] * cols
    for i in order:
        cols_data[i] = cipher[idx:idx+col_lens[i]]
        idx += col_lens[i]
    return ''.join(cols_data[i][r] for r in range(rows) for i in range(cols) if r < len(cols_data[i]))

e = col_encrypt("WE ARE DISCOVERED", "4312567")
d = col_decrypt(e, "4312567")
print("Encrypted:", e)
print("Decrypted:", d)