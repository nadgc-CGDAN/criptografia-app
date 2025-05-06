from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes

def encrypt_aes(plaintext: str) -> str:
    key = get_random_bytes(16)  # Gerando uma chave AES de 16 bytes (128 bits)
    cipher = AES.new(key, AES.MODE_CBC)  # Usando o modo CBC
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return cipher.iv.hex() + ct_bytes.hex()  # Retorna o IV + texto criptografado

def decrypt_aes(ciphertext: str) -> str:
    iv = bytes.fromhex(ciphertext[:32])  # O primeiro bloco de 16 bytes é o IV
    ciphertext = bytes.fromhex(ciphertext[32:])  # O restante é o texto criptografado
    key = b'0123456789abcdef'  # A chave precisa ser a mesma usada no encriptamento
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return plaintext.decode()
