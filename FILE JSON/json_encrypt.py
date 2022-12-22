# import modul
from cryptography.fernet import Fernet

# key generation
key = Fernet.generate_key()
 
# read string kunci
with open('pubkey.key', 'wb') as filekey:
   filekey.write(key)


# pakai kunci
fernet = Fernet(key)
 
# buka file csv
with open('FILE JSON/samplefilejson.json', 'rb') as file:
    original = file.read()
     
# enkripsi csv
encrypted = fernet.encrypt(original)
 
# simpan file enkripsi
with open('hasil_enc.json', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)



