def caesar_cipher_encrypt(plaintext, shift):
    result = ''
    for char in plaintext:
        if char.isalpha():
            
            is_upper = char.isupper()
            
            
            char_code = ord(char)
            shifted_code = (char_code - ord('A' if is_upper else 'a') + shift) % 26
            encrypted_char = chr(shifted_code + ord('A' if is_upper else 'a'))
            
            result += encrypted_char
        else:
            
            result += char

    return result

def main():
    
    plaintext = input("Enter the plaintext: ")
    shift = int(input("Enter the shift value: "))

    
    ciphertext = caesar_cipher_encrypt(plaintext, shift)

    
    print("Encrypted text:", ciphertext)

if __name__ == "__main__":
    main()
