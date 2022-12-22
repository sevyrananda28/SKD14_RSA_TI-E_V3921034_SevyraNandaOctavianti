import binascii

from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA

file_enc = open("FILE TXT/sevyra.txt", "r")

# baca isi file
baca = file_enc.readlines()
print (baca)
#print (baca[1])

teks = str(baca[0])
teks_binary = teks.encode()
print(teks_binary)
# tutup file


keyPair = RSA.generate(2048)

pubKey = keyPair.publickey()
#print(f"Public key:  (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
key2 = pubKeyPEM.decode('ascii')
#print(pubKeyPEM.decode('ascii'))

#print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
#print(privKeyPEM.decode('ascii'))

encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(teks_binary)
print("Encrypted:", binascii.hexlify(encrypted))
cipher_ascii = binascii.hexlify(encrypted)
cipherteks = cipher_ascii.decode()

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
plainteks = decrypted.decode()
print('Decrypted:', plainteks)

file_dec = open("pkey.txt", "a")
file_dec.write(key2)