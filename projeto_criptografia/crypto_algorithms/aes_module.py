from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

# Usar chave fixa para testes — 16 bytes (AES-128)
KEY = b'0123456789abcdef'  # Exatamente 16 caracteres

def encrypt_aes(plaintext: str) -> str:
    cipher = AES.new(KEY, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    # Retorna IV + texto criptografado, tudo codificado em base64
    result = base64.b64encode(cipher.iv + ct_bytes).decode('utf-8')
    return result

def decrypt_aes(ciphertext_b64: str) -> str:
    data = base64.b64decode(ciphertext_b64)
    iv = data[:16]
    ct = data[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    pt = unpad(cipher.decrypt(ct), AES.block_size)
    return pt.decode('utf-8')
