from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

# Chave fixa de 8 bytes (atenção: isso é apenas para testes!)
KEY = b'12345678'

def encrypt_des(plaintext: str) -> str:
    cipher = DES.new(KEY, DES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(plaintext.encode(), DES.block_size))
    return cipher.iv.hex() + ct_bytes.hex()  # IV + ciphertext em hexadecimal

def decrypt_des(ciphertext: str) -> str:
    try:
        iv = bytes.fromhex(ciphertext[:16])  # IV de 8 bytes (16 hex)
        ct = bytes.fromhex(ciphertext[16:])  # O restante é o ciphertext
        cipher = DES.new(KEY, DES.MODE_CBC, iv)
        pt = unpad(cipher.decrypt(ct), DES.block_size)
        return pt.decode()
    except Exception as e:
        return f"Erro ao descriptografar: {str(e)}"
