import socket 
import sys
from datetime import datetime

if len(sys.argv) == 1:
  print ('Server hostname not present, exiting. Usage: python server.py <server hostname>')
  sys.exit(1)
# Connect the socket to the port where the server is listening# Create a TCP/IP socket
server_address = (sys.argv[1], 10000) 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
print ('starting up on %s port %s' % server_address )
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1) 
while True:
    # Wait for a connection
    print ('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print ('connection from', client_address)
        # Receive the data in small chunks and retransmit it
        while True:
            data_bytes = connection.recv(16)
            data = data_bytes.decode()
#            print ('received "%s"' % data)
            if data:
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                f = open("/tmp/ping-pong.log", "a")
                f.write(timestamp +' : ' + data + '\n')
                f.close()                     
              
                print ('sending data back to the client')
                ans = "PONG"
                connection.sendall(ans.encode())
            else:
                print ('no more data from', client_address )
                break
            
    finally:
        # Clean up the connection
        connection.close()
