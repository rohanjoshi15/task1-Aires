# dictionary to map the notations
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 
    'Z': '--..', 

    '0': '-----', '1': '.----', '2': '..---', '3': '...--', 
    '4': '....-', '5': '.....', '6': '-....', '7': '--...', 
    '8': '---..', '9': '----.', 

    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', 
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', 
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-', 
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', 
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

# decoding
decoding = {v: k for k, v in morse_code.items()}

def morse_to_text(morse_code):
    
    words = morse_code.strip().split(" / ")  # take each word separately for converting
    decoded_message = []

    for word in words:
        letters = word.split()  #split the word into indivisual letters
        decoded_word = ''.join(decoding.get(letter, '?') for letter in letters) #the ? is just so that if an alphanumeric value is absent wrt the morse code itl give ? instead of error
        decoded_message.append(decoded_word)

    return ' '.join(decoded_message)  # to join the words with spaces


# first message
morse_message = "- .... .. ... / .. ... / -- --- .-. ... . / -.-. --- -.. ."
decoded_text = morse_to_text(morse_message)

print("Morse Code Message:", morse_message)
print("Decoded Text:", decoded_text)


# second message 
morse_message = "-- .- .-. ... / -.-. .-.. ..- -... / ... --- ..-. - .-- .- .-. . / .. -. - . .-. -."
decoded_text = morse_to_text(morse_message)

print("Morse Code Message:", morse_message)
print("Decoded Text:", decoded_text)
