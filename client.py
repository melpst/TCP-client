import socket
import sys
from Crypto.PublicKey import RSA

#def binToHex(str):
#    return binascii.hexlify(str)

#def hexToBin(str):
#    return binascii.dehexlify(str)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('158.108.34.100', 8000)
print >> sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    pub_key = open('../.ssh/id_rsa.pub', 'rb').read()
    pri_key = open('../.ssh/id_rsa', 'rb').read()
    publicKey = RSA.importKey(pub_key)
    privateKey = RSA.importKey(pri_key)

    message = 'hello, world'
    cipher = publicKey.encrypt(message, 32)[0]
    print 'message is %s' % privateKey.decrypt(cipher)
    amount_received = 0
    amount_expected = len(cipher)
    
    print >> sys.stderr, 'sending'
    sock.sendall(cipher)

    data = ''
    while amount_received < amount_expected:
        data += sock.recv(16)
        amount_received = len(data)
    data = privateKey.decrypt(data)
    print >> sys.stderr, 'receive "%s"' % data

finally:
    print sys.stderr, 'closing socket'
    sock.close()
