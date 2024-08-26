# 4. Write a program that inputs a main string and then creates an encrypted string by embedding a short symbol-based string after each character. The program should also be able to produce the decrypted string from encrypted string.


def encrypt_string(main_string, short_string):
    encrypted = ''
    for char in main_string:
        encrypted += char + short_string
    return encrypted

def decrypt_string(encrypted_string, short_string):
    decrypted = ''
    short_string_length = len(short_string)
    for i in range(0, len(encrypted_string), short_string_length + 1):
        decrypted += encrypted_string[i]
    return decrypted

main_string = "hello"
short_string = "!"
encrypted = encrypt_string(main_string, short_string)
print("Encrypted String:", encrypted)
decrypted = decrypt_string(encrypted, short_string)
print("Decrypted String:", decrypted)
