def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char
    return result

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

# Example usage:
plain_text = "Hello, World!"
shift_value = 32

encrypted_text = caesar_cipher_encrypt(plain_text, shift_value)
print(f"Encrypted: {encrypted_text}")

decrypted_text = caesar_cipher_decrypt(encrypted_text, shift_value)
print(f"Decrypted: {decrypted_text}")
