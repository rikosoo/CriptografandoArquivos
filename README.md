# 🔐 Ransomware Simulador - Criptografia de Arquivos com AES

Este é um **projeto educacional** que simula um ransomware de maneira **ética**, demonstrando como arquivos podem ser criptografados e recuperados utilizando **AES-256**.  
O objetivo deste código é **ensinar criptografia e segurança defensiva**, mostrando tanto a criptografia quanto a recuperação do arquivo.

⚠ **Aviso Importante**  
Este código deve ser utilizado **apenas para fins educativos e dentro de um ambiente controlado**.  
**Não use este projeto para atividades mal-intencionadas ou em sistemas sem permissão.**  

---

## 🚀 Como funciona?

1. O usuário **especifica um arquivo** para criptografar.
2. O script **gera uma chave AES-256 aleatória** e criptografa o arquivo usando **AES no modo CTR**.
3. O arquivo original é **substituído por uma versão criptografada (`.locked`)**.
4. O script também possui a função de **descriptografar o arquivo** caso a chave correta seja usada.
5. A chave foi pré definida como 123456 para facilitar

---

## 🛠️ Tecnologias Utilizadas

- **Python 3**
- **AES-256** para criptografia segura
- **Módulo `pyaes`** para implementação do algoritmo AES
- **Módulo `secrets`** para gerar chaves seguras

---

## 📝 Como rodar o script?


### **1️⃣ Clonar o repositório**
```bash
git clone https://github.com/rikosoo/ransomware-simulado.git
cd ransomware-simulado
```

## Instalar dependências
pip install pyaes

##  Criar um arquivo de teste
echo "Este é um arquivo de teste para criptografia." > foto.txt

## Executar o script
python3 ransomware_simulado.py




