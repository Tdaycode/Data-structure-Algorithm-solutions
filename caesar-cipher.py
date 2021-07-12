alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n','o', 'p',
 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
  'i', 'j', 'k', 'l', 'm', 'n','o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'];
direction = input('Type encode to encrypt, type decode to decrypt:\n');
shift = int(input('Type the number of shift:\n'));
text = input('Input the text to be encrypted\n');
# abc
# ENCRYPTION CODE
def encrypt(plain_text, shift_amount):
    cipher_text = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        position += shift_amount
        encrypted = alphabet[position];
        cipher_text += encrypted
    print(f'The Encoded is {cipher_text} ')
        

       
        
        
encrypt(text, shift)


# DECRYPTION CODE

direction = input('Type decode to encrypt, type decode to decrypt:\n');
shift = int(input('Type the number of shift:\n'));
text = input('Input the text to be decrypted\n');

def decrypt(plain_text=text, shift_amount = shift):
    cipher_decrypt = ''
    for letter in plain_text:
        position = alphabet.index(letter)
        position -= shift_amount
        decrypted = alphabet[position];
        cipher_decrypt += decrypted
    print(f'The decoded is {cipher_decrypt} ')


decrypt(text, shift)
    

   



