import streamlit as st
from crypto_algorithms.aes_module import encrypt_aes, decrypt_aes
from crypto_algorithms.des_module import encrypt_des, decrypt_des
from crypto_algorithms.rsa_module import encrypt_rsa, decrypt_rsa, generate_rsa_keys


# 🤖 Robô no topo
st.image("https://cdn-icons-png.flaticon.com/512/4712/4712109.png", width=100)
st.title("🤖 Comunicação Criptografada")

# Seleção do algoritmo
algoritmo = st.selectbox("Escolha o algoritmo de criptografia:", ["AES", "DES", "RSA"])
mensagem = st.text_area("Digite sua mensagem:", "")

# Geração de chave RSA e persistência entre cliques
if "public_key" not in st.session_state or "private_key" not in st.session_state:
    pub, priv = generate_rsa_keys()
    st.session_state["public_key"] = pub
    st.session_state["private_key"] = priv

# Botão de criptografar
if st.button("Criptografar"):
    try:
        if algoritmo == "AES":
            criptografado = encrypt_aes(mensagem)
        elif algoritmo == "DES":
            criptografado = encrypt_des(mensagem)
        elif algoritmo == "RSA":
            criptografado = encrypt_rsa(mensagem, st.session_state["public_key"])
              
        st.success("🔒 Texto criptografado:")
        st.code(criptografado)
    except Exception as e:
        st.error(f"Erro ao criptografar: {str(e)}")

# Entrada para descriptografar
mensagem_cifrada = st.text_area("Digite o texto criptografado para descriptografar:", "")

if st.button("Descriptografar"):
    try:
        if algoritmo == "AES":
            texto = decrypt_aes(mensagem_cifrada)
        elif algoritmo == "DES":
            texto = decrypt_des(mensagem_cifrada)
        elif algoritmo == "RSA":
            texto = decrypt_rsa(mensagem_cifrada, st.session_state["private_key"])
               
        st.success("🔓 Texto original:")
        st.code(texto)
    except Exception as e:
        st.error(f"Erro ao descriptografar: {str(e)}")
