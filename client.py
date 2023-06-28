import rpyc
from constRPYC import * #-

class Client:
  print(SERVER);
  print(PORT);
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  print (conn.root.exposed_value())
  # conn.root é um objeto que representa o serviço remoto fornecido pelo servidor RPC
  # O prefixo root é usado para acessar os métodos expostos pelo servidor.
  conn.root.exposed_append(5) # Call an exposed operation
  conn.root.exposed_append(6) # and append two elements
  # conn.root.exposed_append(valor) chama o método exposed_append que irá adicionar "valor" à lista e retorná-la
  print (conn.root.exposed_value()) # Print the result
  # conn.root.exposed_value() retorna a lista
