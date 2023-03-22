from fila import FilaNormal
from fila_prioritaria import FilaPrioritaria

fila_teste2 = FilaPrioritaria()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
fila_teste2.atualiza_fila()
print(fila_teste2.chama_cliente(10))
print(fila_teste2.chama_cliente(20))
print(fila_teste2.chama_cliente(15))
print(fila_teste2.estatistica('11/01/1998', 190  , 'detail'))