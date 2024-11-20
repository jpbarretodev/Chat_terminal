import socket

print("""
  _____        _               _           _____  _             _   
 |  __ \      (_)             | |         / ____|| |           | |  
 | |__) |_ __  _ __   __ __ _ | |_  ___  | |     | |__    __ _ | |_ 
 |  ___/| '__|| |\ \ / // _` || __|/ _ \ | |     | '_ \  / _` || __|
 | |    | |   | | \ V /| (_| || |_|  __/ | |____ | | | || (_| || |_ 
 |_|    |_|   |_|  \_/  \__,_| \__|\___|  \_____||_| |_| \__,_| \__|
(client)                                               by BarretoDev
""")


def start_connection_server():
  #ip and port
  ip_connection, port = input("Please enter the server ip: "), int(input("Please enter the server port: "))
  #print(ip_connection, port)

  #create a connection
  client_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client_connection.connect((ip_connection, port))
  print("Connected to server {}:{}\n".format(ip_connection, port))

  while True:
      try:
        message = input("\nPlease enter a message: ")
      except KeyboardInterrupt:
          print("\nDesconected!")
          break
      client_connection.send(message.encode("utf-8"))
      print("\nmessage sent\nWait for message...")
      #received message
      response = client_connection.recv(1024).decode("utf-8")
      if not response:
          print("\nConnection stopped")
          break
      print("\nUser (ip: {}): {}".format(ip_connection, response))

  client_connection.close()

if __name__ == "__main__":
    start_connection_server()