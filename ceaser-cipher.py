alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def ceaser():
  def encrypt(text, shift):
    tempString =""
    for i in text:
      tempIndex = alphabet.index(i) + shift 
      tempString += tempString.join(alphabet[tempIndex])
    print(f"The encode text is {tempString}")
    
  def decode(text, shift):
    tempString =""
    for i in text:
      tempIndex = alphabet.index(i) - shift 
      tempString += tempString.join(alphabet[tempIndex])
    print(f"The encode text is {tempString}")

  if direction=="encode":
    encrypt(text,shift)
  else:
    decode(text, shift)

while True:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  if(shift > 26):
      newShift =shift % 26
      shift = newShift
  if not text.isalpha():
    print("Don't use charcter or number")
  else:
    
    ceaser()
    bool =input("Do you want to keep going?\n")
    if not bool:
      break;

  
