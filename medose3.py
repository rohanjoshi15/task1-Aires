def decode(encrypted_text):
    encrypted_text = encrypted_text.upper()  # convert to uppercase
    decoded_message = ""

    for i, char in enumerate(encrypted_text):
        if 'A' <= char <= 'Z':  
            original_char = chr(ord(char) - (i + 1))  # reverse shift
            if original_char < 'A': 
                original_char = chr(ord(original_char) + 26)
        else:
            original_char = '?'  # for unexpected input

        decoded_message += original_char

    return decoded_message


# user input
encrypted_text = input("Enter encrypted message: ").strip()
decoded_text = decode(encrypted_text)


print("Encrypted message:", encrypted_text)
print("Decoded message:", decoded_text)

