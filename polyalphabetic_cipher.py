import string

# Generate Vigenère table
def generate_key(keyword, textl):
    key = ''
    keyword_length = len(keyword)
    for i in range(textl):
        key += keyword[i % keyword_length]
    return key


# Encrypt function using Vigenère cipher
def encrypt(content, key):
    encrypted = ""
    keymodm = generate_key(key, len(content))
    
    for i in range(len(content)):
        letter = content[i]
        kk = keymodm[i]
        if letter.isalpha():
            is_upper = letter.isupper()
            if is_upper:
                c = (string.ascii_uppercase.index(letter) + string.ascii_uppercase.index(kk.upper()) ) % 26
                encrypted += string.ascii_uppercase[c]
            else:
                c = (string.ascii_lowercase.index(letter) + string.ascii_lowercase.index(kk.lower()) ) % 26
                encrypted += string.ascii_lowercase[c]
        else:
            encrypted += letter
    return encrypted

# Decrypt function using Vigenère cipher
def decrypt(content, key):
    decrypted = ""
    keymodm = generate_key(key, len(content))
    
    for i in range(len(content)):
        letter = content[i]
        kk = keymodm[i]
        if letter.isalpha():
            is_upper = letter.isupper()
            if is_upper:
                c = (string.ascii_uppercase.index(letter) - string.ascii_uppercase.index(kk.upper()) ) % 25
                decrypted += string.ascii_uppercase[c]
            else:
                c = (string.ascii_lowercase.index(letter) - string.ascii_lowercase.index(kk.lower()) ) % 25
                decrypted += string.ascii_lowercase[c]
        else:
            decrypted += letter
    return decrypted

if __name__ == "__main__":
    msg = input("Enter Message To Be Encrypted: ")
    key = input("Enter the Vigenère key: ")
    
    encryptedMsg = encrypt(msg, key)
    print("Encrypted Message:", encryptedMsg)
    
    decryptedMsg = decrypt(encryptedMsg, key)
    print("Decrypted Message:", decryptedMsg)
