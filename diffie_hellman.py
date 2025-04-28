# Diffie-Hellman Key Exchange Algorithm

# Function to calculate the power mod (base^exp % mod)
def power_mod(base, exp, mod):
    result = 1
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp = exp // 2
    return result

# Alice's side
def diffie_hellman_alice(p, g, private_key):
    # Alice calculates public key A = g^a % p
    A = power_mod(g, private_key, p)
    return A

# Bob's side
def diffie_hellman_bob(p, g, private_key):
    # Bob calculates public key B = g^b % p
    B = power_mod(g, private_key, p)
    return B

# Shared key calculation
def shared_key_calculation(public_key, private_key, p):
    # Each party calculates the shared secret key
    return power_mod(public_key, private_key, p)

# Main function to demonstrate Diffie-Hellman
if __name__ == "__main__":
    # Example prime numbers (p) and base (g)
    p = 23  # prime number
    g = 5   # primitive root modulo p

    # Alice and Bob each choose a private key
    alice_private_key = 6  # Alice's private key
    bob_private_key = 15   # Bob's private key

    # Alice computes her public key
    A = diffie_hellman_alice(p, g, alice_private_key)
    print(f"Alice's public key: {A}")

    # Bob computes his public key
    B = diffie_hellman_bob(p, g, bob_private_key)
    print(f"Bob's public key: {B}")

    # Alice and Bob exchange their public keys, and each calculates the shared key

    # Alice computes the shared key using Bob's public key
    alice_shared_key = shared_key_calculation(B, alice_private_key, p)
    print(f"Alice's shared key: {alice_shared_key}")

    # Bob computes the shared key using Alice's public key
    bob_shared_key = shared_key_calculation(A, bob_private_key, p)
    print(f"Bob's shared key: {bob_shared_key}")

    # The shared keys should be the same
    assert alice_shared_key == bob_shared_key, "Keys don't match!"
    print(f"Shared secret key: {alice_shared_key}")
