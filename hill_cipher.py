import numpy as np

def mod_inv(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i
    return None

def matrix_mod_inv(matrix, m):
    det = int(round(np.linalg.det(matrix)))
    det_inv = mod_inv(det % m, m)
    if det_inv is None:
        raise ValueError("Matrix not invertible")
    adj = np.round(det * np.linalg.inv(matrix)).astype(int) % m
    return (det_inv * adj) % m

def text_to_nums(text):
    return [ord(c) - ord('A') for c in text.upper().replace(" ", "")]

def nums_to_text(nums):
    return ''.join(chr(n % 26 + ord('A')) for n in nums)

def hill_encrypt(text, key_matrix):
    nums = text_to_nums(text)
    if len(nums) % 2 != 0:
        nums.append(ord('X') - ord('A'))
    pairs = np.array(nums).reshape(-1, 2)
    encrypted = (pairs @ key_matrix) % 26
    return nums_to_text(encrypted.flatten())

def hill_decrypt(cipher, key_matrix):
    inv_key = matrix_mod_inv(key_matrix, 26)
    nums = text_to_nums(cipher)
    pairs = np.array(nums).reshape(-1, 2)
    decrypted = (pairs @ inv_key) % 26
    return nums_to_text(decrypted.flatten())

key = np.array([[3, 3], [2, 5]])  
e = hill_encrypt("HELLO", key)
d = hill_decrypt(e, key)
print("Encrypted:", e)
print("Decrypted:", d)
