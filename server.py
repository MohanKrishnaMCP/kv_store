#write server code here - to handle CRUD operations
#implement server using socket for better data streaming

import socket

class KeyValueServer:

    def __init__(self, host="localhost", port=1234):
        self.host = host
        self.port = port
        self.kv_store = PersistentKeyValueStore()
        self.command_parser = CommandParser()
    
    def start(self):
        #with commands helps in maintaining opening and closing of file/connection
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            socket.bind(self.host, self.port)
            socket.listen()
            print("socket connection openend. host: ", self.host, ", port: ", self.port)

            while True:
                conn, addr = s.accept()
                with conn:
                    print("socket connected with. client: ", addr)
                    while True:
                        data = conn.recv(1024)
                        
                        if not data:
                            break

                        command, args = self.command_parser.parse(data.decode())
                        response = self.handle_command(command, args)
                        conn.sendAll(response.encode())
    
    def handle_command(self, command, args):
        if(command == "get"):
            return self.kv_store.get(args[0])

        elif(command == "set"):
            key, value = args[0], args[1]
            self.kv_store.setval(key, value)
            return "SUCCESS"
        elif(command == "del"):
            self.kv_store.delete(args[0])
            return "SUCCESS"
        else:
            return "ERROR: UNKNOWN COMMAND"
                    