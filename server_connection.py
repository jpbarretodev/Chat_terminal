import socket

print("""
  _____        _               _           _____  _             _   
 |  __ \      (_)             | |         / ____|| |           | |  
 | |__) |_ __  _ __   __ __ _ | |_  ___  | |     | |__    __ _ | |_ 
 |  ___/| '__|| |\ \ / // _` || __|/ _ \ | |     | '_ \  / _` || __|
 | |    | |   | | \ V /| (_| || |_|  __/ | |____ | | | || (_| || |_ 
 |_|    |_|   |_|  \_/  \__,_| \__|\___|  \_____||_| |_| \__,_| \__|
(server)                                               by BarretoDev
""")

def start_server():
    #get ip
    hostname = socket.gethostname()
    host_ip = socket.gethostbyname(hostname)

    #user enter port
    port = int(input("Please enter the server port: "))
    print("\nYour connection creating in:\nIp: {}\nPort: {}\n".format(host_ip, port))

    #create a connection
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((host_ip, port))
    server.listen(1)
    client_socket, client_ip_addres = server.accept()
    print("\nClient connected! (ip: {})".format(client_ip_addres[0]))
    print("\nWaiting for messages...")

    while True:
        message = client_socket.recv(1024).decode("utf-8")
        if not message:
            print("\nNot messages!\nClose connection")
            break
        print("User (ip: {})\nsay: {}".format(client_ip_addres[0], message))
        ask = input("\nDo you want response? (y/n): ")
        if ask in ["Y", "y"]:
            response = input("\nYour message: ")
            client_socket.send(response.encode("utf-8"))
            print("Waiting for message...")
        elif ask in ["N", "n"]:
            print("\nChat stopped!")
            break

    client_socket.close()
    server.close()

if __name__ == "__main__":
    start_server()