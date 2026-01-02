def caesar(text, shift, encrypt=True):

    if not isinstance(shift, int):
        return 'Shift must be an integer value.'

    if shift < 1 or shift > 25:
        return 'Shift must be an integer between 1 and 25.'

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    if not encrypt:
        shift = -shift

    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    translation_table = str.maketrans(
        alphabet + alphabet.upper(),
        shifted_alphabet + shifted_alphabet.upper()
    )

    return text.translate(translation_table)


def encrypt(text, shift):
    return caesar(text, shift)


def decrypt(text, shift):
    return caesar(text, shift, encrypt=False)



while True:
    choice = input("\nType 'e' to encrypt, 'd' to decrypt, or 'q' to quit: ").lower()

    if choice == 'q':
        print("Goodbye! 👋")
        break

    if choice not in ('e', 'd'):
        print("Invalid choice. Try again.")
        continue

    text = input("Enter your message: ")

    try:
        shift = int(input("Enter shift (1–25): "))
    except ValueError:
        print("Shift must be a number.")
        continue

    if choice == 'e':
        result = encrypt(text, shift)
    else:
        result = decrypt(text, shift)

    print("Result:", result)
