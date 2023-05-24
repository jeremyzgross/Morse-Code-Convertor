MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--',
    '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...', ':': '---...',
    ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-',
    '"': '.-..-.', '$': '...-..-', '@': '.--.-.', ' ': '/'
}


def text_to_morse(text):
    morse_code = []
    for char in text:
        char = char.upper()
        if char in MORSE_CODE_DICT:
            morse_code.append(MORSE_CODE_DICT[char])
    return ' '.join(morse_code)


def morse_to_text(morse_code):
    inverted_dict = {value: key for key, value in MORSE_CODE_DICT.items()}
    words = morse_code.split('/')
    text = []
    for word in words:
        chars = word.split()
        for char in chars:
            if char in inverted_dict:
                text.append(inverted_dict[char])
    return ''.join(text)


# Get user input
user_input = input("Enter '1' for text to Morse code conversion or '2' for Morse code to text conversion: ")

if user_input == '1':
    text = input("Enter the text to convert to Morse code: ")
    morse = text_to_morse(text)
    print(f"Morse code: {morse}")
elif user_input == '2':
    morse_code = input("Enter the Morse code to convert to text: ")
    decoded_text = morse_to_text(morse_code)
    print(f"Decoded text: {decoded_text}")
else:
    print("Invalid input. Please enter '1' or '2'.")


