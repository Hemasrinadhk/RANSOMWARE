from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
import os

def decrypt_file(dataFile, privateKeyFile):

    # read private key from file
    with open(privateKeyFile, 'rb') as f:
        privateKey = f.read()
        # create private key object
        key = RSA.import_key(privateKey)

    # read data from file
    with open(dataFile, 'rb') as f:
        # read the session key
        encryptedSessionKey, nonce, tag, ciphertext = [ f.read(x) for x in (key.size_in_bytes(), 16, 16, -1) ]
        f.close()
    # decrypt the session key
    cipher = PKCS1_OAEP.new(key)
    sessionKey = cipher.decrypt(encryptedSessionKey)

    # decrypt the data with the session key
    cipher = AES.new(sessionKey, AES.MODE_EAX, nonce)
    data = cipher.decrypt_and_verify(ciphertext, tag)

     #save the decrypted data to file
    #[ fileName, fileExtension ] = dataFile.split('.')
    #decryptedFile = fileName + '_decrypted.' + fileExtension
    with open(dataFile, 'wb') as f:
        f.write(data)
        f.close()

    print('Decrypted file saved to ' + dataFile)

def decrypt_files_in_folder(folder_path, private_key_file):
   
    # Get a list of all files in the folder
    files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]

    # Encrypt each file
    for file in files:
        file_path = os.path.join(folder_path, file)
        decrypt_file(file_path, private_key_file)


folder_path_to_decrypt = '/home/hk0648/ransomware/target'


private_key_file_path = '/home/hk0648/ransomware/priv_key.pem'


decrypt_files_in_folder(folder_path_to_decrypt, private_key_file_path)



