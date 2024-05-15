from Crypto.PublicKey import RSA

def generate_key_pair(k_size):
    key = RSA.generate(k_size)
    public_key = key.publickey().export_key()
    private_key = key.export_key()

    return public_key, private_key

public_key, private_key = generate_key_pair(3072)

with open('pub_key.pem', 'wb') as f:
    f.write(public_key)

with open('priv_key.pem', 'wb') as f:
    f.write(private_key)

print('Public and private keys generated and saved.')
