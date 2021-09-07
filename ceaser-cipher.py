alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def ceaser():
    def encrypt(text, shift):
        temp_string = ""
        for i in text:
            temp_index = alphabet.index(i) + shift
            temp_string += temp_string.join(alphabet[temp_index])
        print(f"The encode text is {temp_string}")

    def decode(text, shift):
        temp_string = ""
        for i in text:
            temp_index = alphabet.index(i) - shift
            temp_string += temp_string.join(alphabet[temp_index])
        print(f"The encode text is {temp_string}")

    if direction == "encode":
        encrypt(text, shift)
    else:
        decode(text, shift)


while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 26:
        newShift = shift % 26
        shift = newShift
    if not text.isalpha():
        print("Don't use character or number")
    else:
        ceaser()
        booli = input("Do you want to keep going?\n")
        if not booli:
            break
