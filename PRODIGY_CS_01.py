alphabet=['a', 'b', 'c', 'd', 'e', 'f', 'g','h','i', 'j', 'k', 'l', 'm',
          'n', 'o','p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]

def encryption(plain_text, shift_key):
   cipher_text =""
   for char in plain_text:
       if char in alphabet:
            position = alphabet.index(char)
            new_position = (position+shift_key)%26
            cipher_text +=alphabet[new_position]
       else:
           cipher_text += char
   print(f"Here is the encrypted text: {cipher_text}")

def decryption(encrypted_text, shift_key):
    text = ""
    for char in encrypted_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = (position-shift_key)%26
            text +=alphabet[new_position]
        else:
            text += char
    print(f"Here is the plain text: {text}")

wanna_end = False
while not wanna_end:
    print("1. Encrypt a text")
    print("2. Decrypt a text")

    request = input("Press 1 to encrypt or 2 to decrypt:")
    shift = int(input("Enter shift key:"))
    text = input("Enter the text:").lower()
    if request == "1":
        encryption(text, shift)
    elif request == "2":
        decryption(text, shift)
    play_again=input("Type 0 to exit or type any number to continue:")
    if play_again=='0':
        wanna_end=True
        print("End")

