# Fichier de test pour chiffré et déchiffré

from cryptography.fernet import Fernet

print("Quelle est votre message ?")
i = input()
key = Fernet.generate_key()
f = Fernet(key)
final_key = key.decode()
j = i.encode()
token = f.encrypt(bytes(j))
print("Message chiffré : ", token)
print("Message déchiffré : ",f.decrypt(token))
print("La clé ressemble à : ", final_key)