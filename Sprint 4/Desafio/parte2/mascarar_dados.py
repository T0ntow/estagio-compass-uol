import hashlib

while True:
    user_input = input("Digite uma string para gerar o hash (ou 'exit' para sair): ")
    if user_input.lower() == 'exit':
        break
    hash_object = hashlib.sha1(user_input.encode())
    print(f"Hash SHA-1: {hash_object.hexdigest()}")
