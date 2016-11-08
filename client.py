import socket
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('158.108.34.100', 8000)
print >> sys.stderr, 'connecting to %s port %s' % server_address
sock.connect(server_address)

try:
    message = 'hello, world'
    print >> sys.stderr, 'sending %s' % message
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        print >> sys.stderr, 'receive "%s"' % data

finally:
    print sys.stderr, 'closing socket'
    sock.close()
