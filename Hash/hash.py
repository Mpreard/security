import hashlib
 
# Création du HASH en SHA-1
SHA1 = hashlib.sha1() 

# Création du HASH en SHA-256
SHA256 = hashlib.sha256()

# Création du HASH en SHA-512
SHA512 = hashlib.sha512()

# Création du HASH en MD5
MD5 = hashlib.md5()

# Création du HASH en Blake2b
BLAKE = hashlib.blake2b()

#Option de choix
print("Choississez votre option de hash : SHA-1 = 1 / SHA-256 = 2 / SHA-512 = 3 / MD5 = 4 / Blake2b = 5")
option = input()

if option == "1" :
    with open('file.txt','rb') as file:
        blk = file.read()    
        SHA1.update(blk)
    file.close()
    message_hache = SHA1.hexdigest()
    print(message_hache)
if option == "2":
    with open('file.txt', 'rb') as file:
        blk = file.read()
        SHA256.update(blk)
    file.close()
    message_hache = SHA256.hexdigest()
    print(message_hache)
if option == "3":
    with open('file.txt', 'rb') as file:
        blk = file.read()
        SHA512.update(blk)
    file.close()
    message_hache = SHA512.hexdigest()
    print(message_hache)
if option == "4":
    with open('file.txt', 'rb') as file:
        blk = file.read()
        MD5.update(blk)
    file.close()
    message_hache = MD5.hexdigest()
    print(message_hache)
if option == "5":
    with open('file.txt', 'rb') as file:
        blk = file.read()
        BLAKE.update(blk)
    file.close()
    message_hache = BLAKE.hexdigest()
    print(message_hache)