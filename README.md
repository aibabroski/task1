# Task A: Basic TCP Server and Client

## Description
This project demonstrates a simple **TCP client-server communication** using Python's `socket` library. The server listens for incoming connections and responds to messages sent by the client.

## Files
- **`Aibek_Murat_task1_server.py`** - Implements the server that listens for connections and responds to client messages.
- **`Aibek_Murat_task1_client.py`** - Implements the client that connects to the server and sends messages.

## Prerequisites
Ensure you have **Python 3.x** installed on your system.

## How to Run

### Step 1: Start the Server
1. Open a terminal or command prompt.
2. Navigate to the directory where `Aibek_Murat_task1_server.py` is located.
3. Run the following command:
   ```sh
   python Aibek_Murat_task1_server.py
   ```
4. The server will start listening on `127.0.0.1:8080`.

### Step 2: Start the Client
1. Open another terminal or command prompt.
2. Navigate to the directory where `Aibek_Murat_task1_client.py` is located.
3. Run the following command:
   ```sh
   python Aibek_Murat_task1_client.py
   ```
4. Enter messages when prompted. The server will respond to each message.
5. To terminate the client, type `end` and press Enter.

## Expected Output
- **Server Side:**
  ```sh
  Server listening on 127.0.0.1:8080
  Connection from: ('127.0.0.1', 54321)
  Received from client: Hello Server!
  ```
- **Client Side:**
  ```sh
  Connected to server 127.0.0.1:8080
  Enter your message (type 'end' to exit): Hello Server!
  Received from server: Hello user!
  ```

## Notes
- Ensure that `Aibek_Murat_task1_server.py` is running **before** starting `Aibek_Murat_task1_client.py`.
- Only **one client** can connect at a time since the server listens for a single connection.
- Modify the `host` and `port` variables if you want to run the server on a different IP or port.


## Author
Aibek Murat

