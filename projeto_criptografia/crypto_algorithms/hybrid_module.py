from Crypto.PublicKey import RSA
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def hybrid_encrypt(plaintext: str, public_key: bytes) -> str:
    aes_key = get_random_bytes(16)  # Chave AES de 16 bytes
    cipher_aes = AES.new(aes_key, AES.MODE_CBC)
    ct_bytes = cipher_aes.encrypt(pad(plaintext.encode(), AES.block_size))
    
    # Criptografar a chave AES com RSA
    rsa_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    enc_aes_key = cipher_rsa.encrypt(aes_key)

    return cipher_aes.iv.hex() + enc_aes_key.hex() + ct_bytes.hex()

def hybrid_decrypt(ciphertext: str, private_key: bytes) -> str:
    iv = bytes.fromhex(ciphertext[:32])  # Primeiro bloco é o IV
    enc_aes_key = bytes.fromhex(ciphertext[32:384])  # A chave AES criptografada com RSA
    ct = bytes.fromhex(ciphertext[384:])  # Texto criptografado com AES
    
    # Descriptografar a chave AES com RSA
    rsa_key = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(rsa_key)
    aes_key = cipher_rsa.decrypt(enc_aes_key)
    
    # Descriptografar o texto com AES
    cipher_aes = AES.new(aes_key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher_aes.decrypt(ct), AES.block_size)
    return plaintext.decode()
