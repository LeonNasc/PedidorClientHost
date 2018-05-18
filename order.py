#encoding: utf-8
#Estrutura de dados que armazena um pedido
class Order:
  #Prioridade vai de 0(Menor) até 5(Maior)

  statusList = ['Pendente', 'Separando', 'Liberado']
  priorityList = ['Baixa', 'Normal','Alta','Urgente']


  def __init__(self, params):
    #params é dict
    self.__id = params['id']
    self.__client = params['client']
    self.__status = self.__setDefaultStatus()  

    if not 'priority' in params.keys(): 
      self.__setDefaultPriority()
    else:
      self.setPriority(params['priority'])

  def __setDefaultStatus(self):
    self.__status = 0 #Equivale a priorityList[0] .: 'Pendente'  
    
  def __setDefaultPriority(self):
    self.__priority = 2 #Equivale a priorityList[2] .: 'Normal'

  def setStatus(self, newStatus):
    if newStatus in Order.statusList:
      self.__status = Order.statusList.index(newStatus)
    else:
      raise Exception("Não existe este grau de prioridade")

  def setPriority(self, newPriority):
    if newPriority in Order.priorityList:
      self.__priority = Order.priorityList.index(newPriority)
    else:
      raise Exception("Não existe este grau de prioridade")
  
  def getId(self):
    return self.__id

  def getClient(self):
    return self.__id

  def getStatus(self):
    return Order.statusList[self.__id]

  def getPriority(self):
    return Order.priorityList[self.__id]
    
  def delete(self):
     self.__del__(self)