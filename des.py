from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from binascii import hexlify, unhexlify

# Function to pad the input data to make it a multiple of 8 bytes (64 bits)
def pad(data):
    length = 8 - (len(data) % 8)
    return data + bytes([length]) * length

# Function to encrypt data using DES
def encrypt_des(key, data):
    cipher = DES.new(key, DES.MODE_ECB)  # Using ECB mode for demonstration (not recommended for real use)
    padded_data = pad(data)
    ciphertext = cipher.encrypt(padded_data)
    return ciphertext

# Input plaintext data from the user
plain_text = input("Enter the plaintext data: ")

# Ensure the plaintext length is a multiple of 8 bytes (64 bits)
while len(plain_text) % 8 != 0:
    plain_text += " "  # Pad with spaces if needed

# Convert plaintext to bytes
data = plain_text.encode()

# Generating a random 8-byte (64-bit) key
key = get_random_bytes(8)

# Encryption
print("\n--- Encryption ---")
encrypted = encrypt_des(key, data)
print("Encrypted:", hexlify(encrypted).decode())

# Displaying the ciphertext
print("\n--- Ciphertext Blocks ---")
for i in range(0, len(encrypted), 8):
    block = encrypted[i:i+8]
    print(f"Block {i // 8 + 1}: {hexlify(block).decode()}")

# Changing one bit in the original data
modified_data = bytearray(data)
modified_data[0] ^= 1  # Changing the first bit

# Encryption after modifying one bit
print("\n--- Encryption after changing 1 bit ---")
encrypted_modified = encrypt_des(key, bytes(modified_data))
print("Encrypted (1-bit change):", hexlify(encrypted_modified).decode())

# Displaying the modified ciphertext
print("\n--- Ciphertext Blocks after changing 1 bit ---")
for i in range(0, len(encrypted_modified), 8):
    block = encrypted_modified[i:i+8]
    print(f"Block {i // 8 + 1}: {hexlify(block).decode()}")

# Displaying DESPY and creator's name in a cool way
print("\n--- Details ---")
print()
print("Created by: Yousef")
