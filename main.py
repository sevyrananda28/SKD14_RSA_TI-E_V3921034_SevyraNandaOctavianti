from Crypto.PublicKey import RSA

key = RSA.generate(2048)
pubKey = key.publickey().exportKey("PEM")
privKey = key.exportKey("PEM")
print(pubKey)
print(privKey)

#untuk mendapatkan public dan private key