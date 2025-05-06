from Crypto.Cipher import DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_des(plaintext: str) -> str:
    key = get_random_bytes(8)  # Gerando uma chave DES de 8 bytes
    cipher = DES.new(key, DES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), DES.block_size))
    return cipher.iv.hex() + ct_bytes.hex()  # Retorna o IV + texto criptografado

def decrypt_des(ciphertext: str) -> str:
    iv = bytes.fromhex(ciphertext[:16])  # O primeiro bloco de 8 bytes é o IV
    ciphertext = bytes.fromhex(ciphertext[16:])  # O restante é o texto criptografado
    key = b'12345678'  # A chave precisa ser a mesma usada no encriptamento
    cipher = DES.new(key, DES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), DES.block_size)
    return plaintext.decode()
