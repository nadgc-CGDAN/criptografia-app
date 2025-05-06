from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Random import get_random_bytes

# Gerar chave RSA
def generate_rsa_keys():
    key = RSA.generate(2048)
    private_key = key.export_key()
    public_key = key.publickey().export_key()
    return public_key, private_key

def encrypt_rsa(plaintext: str, public_key: bytes) -> str:
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)
    ciphertext = cipher.encrypt(plaintext.encode())
    return ciphertext.hex()

def decrypt_rsa(ciphertext: str, private_key: bytes) -> str:
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)
    decrypted = cipher.decrypt(bytes.fromhex(ciphertext))
    return decrypted.decode()
