import random

def generate_key(key_length):
    key = [random.randint(0, 1) for _ in range(key_length)]
    return key

def encrypt_stream_cipher(plaintext, key):
    ciphertext = ""
    for i in range(len(plaintext)):
        # Generate a keystream bit using the key
        keystream_bit = key[i % len(key)]
        # XOR the plaintext bit with the keystream bit
        ciphertext_bit = str(int(plaintext[i]) ^ keystream_bit)
        ciphertext += ciphertext_bit
    return ciphertext

def decrypt_stream_cipher(ciphertext, key):
    plaintext = ""
    for i in range(len(ciphertext)):
        # Generate a keystream bit using the key
        keystream_bit = key[i % len(key)]
        # XOR the ciphertext bit with the keystream bit to retrieve the plaintext bit
        plaintext_bit = str(int(ciphertext[i]) ^ keystream_bit)
        plaintext += plaintext_bit
    return plaintext

if __name__ == "__main__":
    plaintext = input("Enter plaintext (binary): ")
    key_length = int(input("Enter key length: "))
    
    key = generate_key(key_length)
    print("Generated Key:", ''.join(map(str, key)))
    
    ciphertext = encrypt_stream_cipher(plaintext, key)
    print("Encrypted Ciphertext:", ciphertext)
    
    decrypted_text = decrypt_stream_cipher(ciphertext, key)
    print("Decrypted Plaintext:", decrypted_text)
