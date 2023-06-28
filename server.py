import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service): # implementa o serviço RPC
  value = [] # os dados serão armazenados aqui

  def exposed_append(self, data): # adiciona o argumento à lista e a retorna
    print('execute exposed_append')
    self.value = self.value + [data]
    return self.value

  def exposed_value(self): # retorna a lista
    print('execute exposed_value')
    return self.value

# inicialização do servidor
if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT) # cria um objeto ThreadedServer, que representa o servidor RPC
  # > DBList representa o serviço que o servidor fornecerá
  # > port=PORT especifica a porta em que o servidor será executado
  print('starting server')
  server.start() # inicia o servidor RPC

