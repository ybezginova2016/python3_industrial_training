'''
The Caesar cipher is an ancient encryption algorithm used by Julius Caesar. It 
encrypts letters by shifting them over by a 
certain number of places in the alphabet. We 
call the length of shift the key. For example, if the 
key is 3, then A becomes D, B becomes E, C becomes 
F, and so on. To decrypt the message, you must shift 
the encrypted letters in the opposite direction. This 
program lets the user encrypt and decrypt messages 
according to this algorithm.

When you run the code, the output will look like this:

Do you want to (e)ncrypt or (d)ecrypt?
> e
Please enter the key (0 to 25) to use.
> 4
Enter the message to encrypt.
> Meet me by the rose bushes tonight.
QIIX QI FC XLI VSWI FYWLIW XSRMKLX.


Do you want to (e)ncrypt or (d)ecrypt?
> d
Please enter the key (0 to 26) to use.
> 4
Enter the message to decrypt.
> QIIX QI FC XLI VSWI FYWLIW XSRMKLX.
MEET ME BY THE ROSE BUSHES TONIGHT.
'''


def caesar_cipher(message, key, mode):
    """Encrypts or decrypts a message using the Caesar cipher.

    Args:
        message (str): The message to be encrypted or decrypted.
        key (int): The key to use for encryption or decryption.
        mode (str): The mode to use - 'encrypt' or 'decrypt'.

    Returns:
        str: The encrypted or decrypted message.
    """
    if mode == 'decrypt':
        key = -key

    result = ''
    for char in message:
        if char.isalpha():
            num = ord(char) + key
            if char.isupper():
                if num > ord('Z'):
                    num -= 26
                elif num < ord('A'):
                    num += 26
            else:
                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26
            result += chr(num)
        else:
            result += char

    return result


def main():
    while True:
        mode = input("Do you want to (e)ncrypt or (d)ecrypt?\n> ")
        if mode.lower() not in ('e', 'd'):
            print("Invalid input. Please enter 'e' or 'd'.")
            continue

        key = None
        while key is None:
            try:
                key = int(input("Please enter the key (0 to 25) to use.\n> "))
                if not 0 <= key <= 25:
                    print("Invalid key. Please enter a number between 0 and 25.")
                    key = None
            except ValueError:
                print("Invalid input. Please enter a number.")

        message = input("Enter the message to {}.\n> ".format('encrypt' if mode.lower() == 'e' else 'decrypt'))
        print(caesar_cipher(message, key, mode.lower()))

        another = input(
            "Do you want to {} another message? (y/n)\n> ".format('encrypt' if mode.lower() == 'e' else 'decrypt'))
        if another.lower() == 'n':
            break


if __name__ == '__main__':
    main()
