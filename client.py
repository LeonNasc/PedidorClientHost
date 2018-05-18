#encoding: utf-8
#Cliente que gera e monitora pedidos
from order import Order

class Client:

  def __init__(self, name, location):
    
    self.__name = name
    self.__location = location

  def getName(self):
    return self.__name

  def getLocation(self):
    return self.__location

  def adicionarPedido(self, pedidoInfo):
    #PedidoInfo é dict
    if(self.__validarPedido(pedidoInfo)):
      pedido = Order(pedidoInfo)
      print("Pedido gerado")
      return True    
        
    return False

  def listarPedidos(self,id):
    #definir depois
    print("Pedidos visualizados")

  def __validarPedido(self,pedidoInfo):
    try:
      if 'id' not in pedidoInfo.keys():
        raise Exception('Pedido deve ter um id')
      if 'client' not in pedidoInfo.keys():
        raise Exception('Pedido deve ter um client')
    except Exception as e:
      print(">Erro: " + str(e))
      return False

    return True