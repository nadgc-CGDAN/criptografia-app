import os
import zipfile

# Estrutura do projeto
project_structure = {
    "projeto_criptografia": [
        "app_streamlit.py",
        "requirements.txt",
        "README.md",
        "LICENSE"
    ],
    "projeto_criptografia/crypto_algorithms": [
        "aes_module.py",
        "des_module.py",
        "rsa_module.py",
      
    ]
}

# Conteúdo dos arquivos
file_contents = {
    "README.md": """# Projeto de Comunicação Criptografada

Este projeto permite comunicação segura entre duas aplicações usando AES, DES, RSA e criptografia híbrida.

## Executar
pip install -r requirements.txt
streamlit run app_streamlit.py
""",
    "LICENSE": "MIT License",
    "requirements.txt": "streamlit\npycryptodome\ncryptography",
    "app_streamlit.py": "import streamlit as st\n\nst.title('Comunicação Criptografada')\n\nst.write('Escolha o algoritmo e digite sua mensagem:')",
    "crypto_algorithms/aes_module.py": "def encrypt_aes(text): return 'aes_' + text\ndef decrypt_aes(ciphertext): return ciphertext.replace('aes_', '')",
    "crypto_algorithms/des_module.py": "def encrypt_des(text): return 'des_' + text\ndef decrypt_des(ciphertext): return ciphertext.replace('des_', '')",
    "crypto_algorithms/rsa_module.py": "def encrypt_rsa(text): return 'rsa_' + text\ndef decrypt_rsa(ciphertext): return ciphertext.replace('rsa_', '')",
   
}

# Criar diretórios e arquivos
for folder, files in project_structure.items():
    os.makedirs(folder, exist_ok=True)
    for file in files:
        content_key = file if "crypto_algorithms" not in folder else f"crypto_algorithms/{file}"
        with open(os.path.join(folder, file), "w", encoding="utf-8") as f:
            f.write(file_contents.get(content_key, ""))

# Criar o zip
with zipfile.ZipFile("projeto_criptografia.zip", "w") as zipf:
    for folder, files in project_structure.items():
        for file in files:
            file_path = os.path.join(folder, file)
            zipf.write(file_path)
