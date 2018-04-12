import struct, socket, time

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define the port on which you want to connect

HOST = '127.0.0.1' #input("Enter HOST: ")
PORT = 1234 #input("Enter port: ")
RECV_BUFFER = 1024

# connect to the server on local computer
s.connect((HOST, PORT))
print ("Connected to the host: %s, port is: %d" %(HOST, PORT) )
attempts = input("Enter quantity of attempts: ")
seq_num = 0
while seq_num != int(attempts):

    ## create ping pat
    seq_num += 1
    pdata = struct.pack("!Hd", seq_num, time.time())
    s.send(pdata)
    # receive data from the server
    data = s.recv(RECV_BUFFER)

    current_time = time.time()
    (seq, timestamp) = struct.unpack("!Hd", data)
    rtt = current_time - timestamp
    rtt *= 1000

    print ("seq=%u, rtt=%.3f ms" % (seq, rtt))
    time.sleep(1)
# close the connection
s.close()