import socket 
import sys
import time
from datetime import datetime

if len(sys.argv) == 1:
  print ('Server hostname not present, exiting. Usage: python client.py <server hostname>')
  sys.exit(1)
# Connect the socket to the port where the server is listening
server_address = (sys.argv[1], 10000) 

while True:
  # Create a TCP/IP socket
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

  print ('connecting to %s port %s' % server_address )
  sock.connect(server_address) 

  try:
    # Send data
    message = 'PING'
    print ('sending "%s"' % message)
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    
    while amount_received < amount_expected:
        data_bytes = sock.recv(16)
        data = data_bytes.decode()
        amount_received += len(data)
        print ('received "%s"' % data) 
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    f = open("/tmp/ping-pong.log", "a")
    f.write(timestamp +'  : ' + data + '\n')
    f.close()     
    time.sleep(1)
  finally:
    print ('closing socket')
    sock.close()
