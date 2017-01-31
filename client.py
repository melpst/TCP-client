import socket
import sys
import time
from Crypto.PublicKey import RSA

#def binToHex(str):
#    return binascii.hexlify(str)

#def hexToBin(str):
#    return binascii.dehexlify(str)

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 8000)
print >> sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    pub_key = open('../.ssh/id_rsa.pub', 'rb').read()
    pri_key = open('../.ssh/id_rsa', 'rb').read()
    publicKey = RSA.importKey(pub_key)
    privateKey = RSA.importKey(pri_key)

    cipher = sock.recv(2048)
    print "receiving encrypt message " + cipher

    message = privateKey.decrypt(cipher)
    print 'message is %s' % message

    print >> sys.stderr,'sending message to server'
    sock.sendall(message)

finally:
    print sys.stderr, 'closing socket'
    sock.close()
