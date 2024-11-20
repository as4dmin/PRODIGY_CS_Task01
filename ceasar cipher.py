
letters = 'abcdefghijklmnopqrstuvwxyz'
num_letters = len(letters)


def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key

    for letter in text:
        letter = letter.lower()
        if  letter != ' ':
            index = letters.find(letter)
            if index == -1:
                result += letter
            else:
                new_index = index + key
                if new_index >= num_letters:
                    new_index -= num_letters
                elif new_index < 0:
                    new_index += num_letters
                result += letters[new_index]
    return result


print('*** CEASAR CIPHER ***\n')

user_input = input("Do you want to encrypt or dcrypt : (e/d)\n").lower()

if user_input == 'e':
    print("ENCRYPTION MODE SELECTED\n")
    key = int(input('Enter a key ( 1 through 26): '))
    text = (input('Enter the text to encrypt : '))
    ciphertext = encrypt_decrypt(text , user_input, key)
    print(f'CIPHERTEXT: {ciphertext}')


elif user_input == 'd':
    print("DECRYPTION MODE SELECTED\n")
    key = int(input('Enter a key ( 1 through 26): '))
    text = (input('Enter the text to decrypt : '))
    plaintext = encrypt_decrypt(text , user_input , key)
    print(f'PLAINTEXT: {plaintext}')
 