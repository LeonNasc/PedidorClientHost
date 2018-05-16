#Estrutura de dados que armazena um pedido
class Pedido:
  #Prioridade vai de 0(Menor) até 5(Maior)

  self.numero = 0
  self.client = False
  self.prioridade = 3

  def __init__(self, params):
    #definir resto depois
    self.status_list = ['Pendente', 'Separando', 'Liberado']