import socket

def port_scan():
    link = input("Enter link to perform scan ports on: ")
    host = socket.gethostbyname(link)
    res = "a"
    
    while(res != "bye"):
        min = input("Enter the lowest limit of range: ")
        max = input("Enter the highest limit of range: ")
        for port in range(int(min), int(max)):
            try:
                client_socket = socket.socket()
                print("Trying connection to", host, "on port", port, "...")
                if client_socket.connect_ex((host, port)) == 0:
                    print("Connection to", host, "on port", port, "was SUCCESSFUL")
                else:
                    print("Connection to", host, "on port", port, "was A FAILURE")
                client_socket.close()
            except socket.error:
                print("Connection to", host, "on port", port, "was A FAILURE")
                client_socket.close()
                
        res = input("Scan has ended, To Exit press 'bye', To continue search with different inputs press 'y'")
    
    print("Scanner Exited.")

if __name__ == "__main__":
    port_scan()
