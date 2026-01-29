def encrypt(plaintext, key):
    ciphertext= ""
    cipher = []

    for i in range(len(key)):
        cipher.append(ord(plaintext[i]) - ord('A') + (ord(key[i]) - ord('A')))

    for i in range(len(key)):
        if cipher[i] > 25:
            cipher[i] = cipher[i] - 26

    for i in range(len(key)):
        ciphertext += chr(cipher[i] + ord('A'))

    return ciphertext

def decrypt(ciphertext, key):
    decrypted_text = ""
    plain = []

    for i in range(len(key)):
        plain.append(ord(ciphertext[i]) - ord('A') - (ord(key[i]) - ord('A')))

    for i in range(len(key)):
        if plain[i] < 0:
            plain[i] = plain[i] + 26

    for i in range(len(key)):
        decrypted_text += chr(plain[i] + ord('A'))

    return decrypted_text

plaintext = "ANKIT"

key="MONEY"

ciphertext = encrypt(plaintext.upper(), key.upper())
print(f"Ciphertext: {ciphertext}")

decrypted_text = decrypt(ciphertext, key.upper())
print(f"Decrypted Text: {decrypted_text}")