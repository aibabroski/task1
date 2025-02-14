import socket

def client():

    host = '127.0.0.1'  # server's IP (localhost)
    port = 8080         # server's port

    # Create TCP client socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the server
    client_socket.connect((host, port))
    print(f"Connected to server {host}:{port}")

    # Prompt the user for input
    message = input("Enter your message (type 'end' to exit): ")

    # Keep sending messages until the user types 'end'
    while message.lower().strip() != 'end':
        # Send the message to the server
        client_socket.send(message.encode())

        # Wait for the response from the server (up to 1024 bytes)
        data = client_socket.recv(1024).decode()
        print(f"Received from server: {data}")

        # Prompt the user for the next message
        message = input("Enter your message (type 'end' to exit): ")

    # Close the connection
    client_socket.close()

if __name__ == '__main__':
    client()