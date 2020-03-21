import hashlib
import app

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

def hashfile(bouton_cryptage):
    if select == "SHA1":
        with open(filename,'rb') as file:
            blk = file.read()    
            SHA1.update(blk)
        file.close()
        message_hache = SHA1.hexdigest()
        print(message_hache)
    if select == "SHA-256":
        with open(filename,'rb') as file:
            blk = file.read()    
            SHA256.update(blk)
        file.close()
        message_hache = SHA256.hexdigest()
        print(message_hache)
    if select == "SHA-512":
        with open(filename,'rb') as file:
            blk = file.read()    
            SHA512.update(blk)
        file.close()
        message_hache = SHA512.hexdigest()
        print(message_hache)
    if select == "MD5":
        with open(filename,'rb') as file:
            blk = file.read()    
            MD5.update(blk)
        file.close()
        message_hache = MD5.hexdigest()
        print(message_hache)
    if select == "Blake2b":
        with open(filename,'rb') as file:
            blk = file.read()    
            BLAKE.update(blk)
        file.close()
        message_hache = BLAKE.hexdigest()
        print(message_hache)