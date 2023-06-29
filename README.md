# Client-Server Com RPyC

Sistema cliente-servidor usando RPyC (Remote Python Call) para realizar chamadas remotas a um serviço RPC.

O cliente se conecta ao servidor e interage com o serviço RPC, executando as operações desejadas e obtendo os resultados de volta. Isso permite que a manipulação de dados seja feita de forma remota, em um ambiente distribuído.

O projeto é composto por dois arquivos principais:

#### `server.py`
Contém a implementação do serviço RPC contendo métodos que podem ser acessados remotamente. Esses métodos permitem manipular uma lista de dados, como adicionar, remover, ordenar e substituir elementos da lista.

#### `client.py`
Contém a implementação de um cliente que se conecta ao servidor RPC e faz chamadas aos métodos do serviço remoto.


## Métodos implementados

| Método   | Parâmetro       | Descrição                           |
| :---------- | :--------- | :---------------------------------- |
| `exposed_value` |  | Retorna a lista |
| `exposed_element` | idx | Retorna o elemento da lista correspondente ao índice idx passado |
| `exposed_append` | val | Insere na lista o valor val1 passado |
| `exposed_replace_all` | val1, val2 | Substitui todas as ocorrências de um valor val1 por um valor val2 |
| `exposed_remove` | val | Remove da lista todos os elementos de valor val |
| `exposed_reset_list` |  | Esvazia a lista |
| `exposed_sort_asc` |  | Ordena a lista em ordem crescente |
| `exposed_sort_desc` |  | Ordena a lista em ordem decrescente |

## Autores

- Luis Guilherme Barbosa [@lguilhermebarbosa](https://github.com/lguilhermebarbosa)
- Bianca Pereira de Carvalho [@biancarvalhoufg](https://github.com/biancarvalhoufg)