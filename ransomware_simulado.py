import os
import pyaes
import hashlib

# Criando uma chave de 32 bytes (AES-256) a partir da string "123456"
key = hashlib.sha256("123456".encode()).digest()  # Garante 32 bytes

# Função para criptografar um arquivo
def encrypt_file(file_name, key):
    # Abrindo o arquivo para leitura binária
    with open(file_name, "rb") as file:
        file_data = file.read()

    # Criando um IV fixo para testes (NÃO FAÇA ISSO EM PRODUÇÃO)
    iv = b"1234567890abcdef"  # IV de 16 bytes (apenas para testes)

    # Criando o modo de operação CTR
    aes = pyaes.AESModeOfOperationCTR(key, counter=lambda: iv)

    # Criptografando o arquivo
    encrypted_data = aes.encrypt(file_data)

    # Salvando o arquivo criptografado
    new_file_name = file_name + ".locked"
    with open(new_file_name, "wb") as new_file:
        new_file.write(iv + encrypted_data)  # Salva IV + dados criptografados

    print(f"🔒 Arquivo criptografado: {new_file_name}")

    # Removendo o arquivo original (opcional)
    # os.remove(file_name)

# Função para descriptografar um arquivo
def decrypt_file(encrypted_file_name, key):
    # Lendo o arquivo criptografado
    with open(encrypted_file_name, "rb") as file:
        encrypted_data = file.read()

    # Separando o IV dos dados criptografados
    iv = encrypted_data[:16]
    encrypted_data = encrypted_data[16:]

    # Criando o modo de operação CTR com o IV extraído
    aes = pyaes.AESModeOfOperationCTR(key, counter=lambda: iv)

    # Descriptografando os dados
    decrypted_data = aes.decrypt(encrypted_data)

    # Recuperando o nome original do arquivo
    original_file_name = encrypted_file_name.replace(".locked", "")

    # Salvando o arquivo descriptografado
    with open(original_file_name, "wb") as decrypted_file:
        decrypted_file.write(decrypted_data)

    print(f"🔓 Arquivo recuperado: {original_file_name}")

    # Removendo o arquivo criptografado (opcional)
    # os.remove(encrypted_file_name)

# Nome do arquivo para teste
file_name = "foto.txt"

# Criptografando o arquivo
encrypt_file(file_name, key)

# Descriptografando o arquivo (simulação de recuperação)
decrypt_file(file_name + ".locked", key)
