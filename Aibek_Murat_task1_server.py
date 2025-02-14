import socket

def server():

    # Define IP address and port
    host = '127.0.0.1'  # localhost
    port = 8080

    # Create TCP socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the socket to the host and port
    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    # Accept the connection
    conn, address = server_socket.accept()
    print(f"Connection from: {address}")

    # Continuously listen for messages from the connected client
    while True:
        # Receive up to 1024 bytes
        data = conn.recv(1024).decode()

        # If no data is received, the client has likely disconnected
        if not data:
            break

        print(f"Received from client: {data}")

        # Send a response back to the client
        response = 'Hello user!'
        conn.send(response.encode())

    # Close the connection when done
    conn.close()

if __name__ == '__main__':
    server()