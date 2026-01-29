import random

def generate_key(plaintext_length):
    key = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') for _ in range(plaintext_length))
    return key

def encrypt(plaintext, key):
    ciphertext = []
    for p_char, k_char in zip(plaintext, key):
        c_char = chr(((ord(p_char) - ord('A')) ^ (ord(k_char) - ord('A'))) + ord('A'))
        ciphertext.append(c_char)
    return ''.join(ciphertext)


def decrypt(ciphertext, key):
    decrypted_text = []
    for c_char, k_char in zip(ciphertext, key):
        p_char = chr(((ord(c_char) - ord('A')) ^ (ord(k_char) - ord('A'))) + ord('A'))
        decrypted_text.append(p_char)
    return ''.join(decrypted_text)


if __name__ == "__main__":
    plaintext = "ANKIT"
    key = generate_key(len(plaintext))

    print(f"Plaintext: {plaintext}")
    print(f"Key: {key}")

    ciphertext = encrypt(plaintext, key)
    print(f"Ciphertext: {ciphertext}")

    decrypted_text = decrypt(ciphertext, key)
    print(f"Decrypted Text: {decrypted_text}")