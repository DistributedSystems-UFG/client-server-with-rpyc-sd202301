import rpyc
from constRPYC import *
from rpyc.utils.server import ThreadedServer

class DBList(rpyc.Service): # implementa o serviço RPC
  value = [] # os dados serão armazenados aqui

  def exposed_append(self, val): # adiciona o argumento à lista e a retorna
    print('execute exposed_append')
    self.value = self.value + [val]
    return self.value

  def exposed_remove(self, val): # remove da lista os elementos com valor de val1
    print('execute exposed_remove')
    while val in self.value:
      self.value.remove(val)
    return self.value

  def exposed_reset_list(self): # esvazia a lista
    print('execute exposed_reset_list')
    self.value = []
    return self.value
  
  def exposed_sort_asc(self): # ordena a lista em ordem crescente
    print('execute exposed_sort_asc')
    self.value.sort()
    return self.value

  def exposed_sort_desc(self): # ordena a lista em ordem decrescente
    print('execute exposed_sort_desc')
    self.value.sort()
    self.value.reverse()
    return self.value

  def exposed_value(self): # retorna a lista
    print('execute exposed_value')
    return self.value

  def exposed_element(self, idx): # retorna um elemento da lista pelo índice
    print('execute exposed_element')
    return self.value[idx]

  def exposed_replace_all(self, val1, val2): # substitui todos os elementos com valor val1 pro valor val2
    print('execute exposed_replace_all')
    while val1 in self.value:
      idx = self.value.index(val1)
      self.value[idx] = val2
    return self.value

# inicialização do servidor
if __name__ == "__main__":
  server = ThreadedServer(DBList(), port = PORT) # cria um objeto ThreadedServer, que representa o servidor RPC
  # > DBList representa o serviço que o servidor fornecerá
  # > port=PORT especifica a porta em que o servidor será executado
  print('starting server')
  server.start() # inicia o servidor RPC