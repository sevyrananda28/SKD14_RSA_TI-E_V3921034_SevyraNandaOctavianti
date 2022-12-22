from cryptography.fernet import Fernet

#DEKRIPSI

key = open('pubKey.key', 'rb').read()
# pakai kunci yang tadi
fernet = Fernet(key)

# buka file hasil enkrpisi
with open('hasil_enc.json', 'rb') as enc_file:
	encrypted = enc_file.read()

# langsung di dekripsi 
decrypted = fernet.decrypt(encrypted)

# cek hasil dekripsi cocok apa tidak ??
with open('hasil_dec.json', 'wb') as dec_file:
	dec_file.write(decrypted)