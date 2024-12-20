
# Caesar Cipher - Encryption and Decryption

This Python program implements the Caesar Cipher algorithm, a classical encryption technique. It allows the user to encrypt or decrypt a text based on a given key.

## Table of Contents

1. [Overview](#overview)
2. [How to Use](#how-to-use)
3. [Functionality](#functionality)
4. [Code Explanation](#code-explanation)
5. [Example](#example)
6. [License](#license)

## Overview

The Caesar Cipher is one of the simplest and most widely known encryption techniques. It works by shifting each letter of the plaintext by a certain number of places down or up the alphabet. The program provides a choice to the user to either **encrypt** or **decrypt** a given text based on a user-supplied key.

## How to Use

1. Clone or download the repository.
2. Run the Python script `caesar_cipher.py`.
3. Choose whether to encrypt or decrypt the text when prompted.
4. Enter a key (an integer between 1 and 26) when prompted.
5. Input the text to either encrypt or decrypt.

The script will then output the result: either the encrypted **ciphertext** or the decrypted **plaintext**.

## Functionality

### Encryption Mode (`e`)

- The program shifts each letter of the input text forward by the number of positions specified by the key.
- Non-alphabetic characters (such as spaces or punctuation) are not altered.
- The result will be displayed as the **ciphertext**.

### Decryption Mode (`d`)

- The program shifts each letter of the input text backward by the number of positions specified by the key.
- Like encryption, non-alphabetic characters are left unchanged.
- The result will be displayed as the **plaintext**.

## Code Explanation

### `encrypt_decrypt` function

This is the core function of the program that handles both encryption and decryption:

```python
def encrypt_decrypt(text, mode, key):
    result = ''
    if mode == 'd':
        key = -key  # Reverse the shift direction for decryption

    for letter in text:
        letter = letter.lower()  # Ensure all text is lowercase
        if letter != ' ':
            index = letters.find(letter)  # Find the index of the letter in the alphabet
            if index == -1:  # Non-alphabetic characters are not altered
                result += letter
            else:
                new_index = index + key  # Shift the letter by the key
                if new_index >= num_letters:
                    new_index -= num_letters  # Wrap around if the index exceeds the alphabet length
                elif new_index < 0:
                    new_index += num_letters  # Wrap around if the index goes negative
                result += letters[new_index]
    return result
```

- **Input:** The function takes the text, mode (either `'e'` for encryption or `'d'` for decryption), and the key.
- **Output:** It returns the modified text after applying the Caesar Cipher shift.

### User Interaction

1. The program asks the user if they want to encrypt or decrypt text.
2. The user provides a key (a number between 1 and 26) to determine how much to shift the alphabet.
3. The program processes the input text and outputs the result accordingly.

## Example

Here’s an example interaction:

```
*** CAESAR CIPHER ***

Do you want to encrypt or decrypt : (e/d)
e
ENCRYPTION MODE SELECTED

Enter a key ( 1 through 26): 3
Enter the text to encrypt : hello world
CIPHERTEXT: khoor zruog
```

For decryption, the user would select `d` and input the corresponding key used for encryption.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

You can now create a `README.md` file in your project repository, paste this content into it, and commit the changes. This will provide clear and comprehensive instructions for users to understand and use your Caesar Cipher program.
