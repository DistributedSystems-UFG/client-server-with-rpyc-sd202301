import rpyc
from constRPYC import * #-

class Client:
  conn = rpyc.connect(SERVER, PORT) # Connect to the server
  # esvaziar a lista
  conn.root.exposed_reset_list()
  print ("Lista vazia: ", conn.root.exposed_value())

  # conn.root é um objeto que representa o serviço remoto fornecido pelo servidor RPC
  # O prefixo root é usado para acessar os métodos expostos pelo servidor.
  conn.root.exposed_append(5) # Call an exposed operation
  conn.root.exposed_append(6) # and append two elements
  conn.root.exposed_append(5)
  # conn.root.exposed_append(valor) chama o método exposed_append que irá adicionar "valor" à lista e retorná-la
  print ("Lista com novos elementos", conn.root.exposed_value())
  # conn.root.exposed_value() retorna a lista

  # ordenar decrescentemente
  conn.root.exposed_sort_desc(5)
  print ("Lista ordenada (desc)", conn.root.exposed_value())

  # ordenar crescentemente
  conn.root.exposed_sort_asc()
  print ("Lista ordenada (asc)", conn.root.exposed_value())

  # retornar primeiro elemento da lista
  print("Primeiro elemento da lista",conn.root.exposed_element(0))

  # substituir os elementos de valor 5 por 10
  conn.root.exposed_replace_all(5, 10)
  print ("Lista alterada", conn.root.exposed_value())
