'''
This program can hack messages encrypted 
with the Caesar cipher from the previous project, even 
if you don’t know the key. There are only 26 
possible keys for the Caesar cipher, so a computer can easily try all possible decryptions and display the results to the user. In cryptography, we call 
this technique a brute-force attack.
'''

def brute_force_caesar_cipher(message):
    for key in range(26):
        decrypted_message = ""
        for character in message:
            if character.isalpha():
                shifted_character = chr((ord(character) - ord('a') + key) % 26 + ord('a'))
                decrypted_message += shifted_character
            else:
                decrypted_message += character
        print(f"Key {key}: {decrypted_message}")

encrypted_message = "YULIA BEZGINOVA"
brute_force_caesar_cipher(encrypted_message)
