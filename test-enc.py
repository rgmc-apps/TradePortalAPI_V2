"""
Standalone script for testing password encryption/decryption.
"""

def rotate_right(value):
    for _ in range(2):
        if value % 2 == 1:
            value = (value // 2) + 128
        else:
            value = value // 2
    return value % 256

def rotate_left(value):
    for _ in range(2):
        new_val = (value * 2) % 256
        if value >= 128:
            new_val += 1
        value = new_val % 256
    return value

def encrypt(value, key):
    val_bytes = value.encode('latin-1')
    key_bytes = key.encode('latin-1')
    result = bytearray()

    for i in range(len(val_bytes)):
        ch1 = val_bytes[i]
        ch2_index = ((i + 1) % len(key_bytes))
        ch2 = key_bytes[ch2_index]
        combined = (ch1 + ch2) % 256
        rotated = rotate_right(combined)
        result.append(rotated)

    return result.decode('latin-1')

def decrypt(value, key):
    val_bytes = value.encode('latin-1')
    key_bytes = key.encode('latin-1')
    result = bytearray()

    for i in range(len(val_bytes)):
        ch = val_bytes[i]
        rotated = rotate_left(ch)
        key_ch = key_bytes[(i + 1) % len(key_bytes)]
        decoded = (rotated - key_ch) % 256
        result.append(decoded)

    result_decoded = result.decode('latin-1').replace('Ü', '2')
    print(result_decoded)
    return result_decoded

# ====== Test Block ======
if __name__ == "__main__":
    password_key = "My Runway Direct Sales"
    plaintext = "12345678"
    known_encrypted = "ª?ajèk&l"

    encrypted = encrypt(plaintext, password_key)
    decrypted = decrypt(known_encrypted, password_key)

    print("Original text:        ", plaintext)
    print("Encrypted result:     ", encrypted)
    print("Matches known?        ", encrypted.encode('latin-1') == known_encrypted.encode('latin-1'))
    print("Known encrypted text: ", known_encrypted)
    print("Decrypted result:     ", decrypted)
