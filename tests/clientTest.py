#encoding:utf8
#Testes unitários para a classe Client

import sys
#Caminho para as classes
sys.path.append('/home/leon/dev/ClientHost')

from client import Client

class ClientTest:

  def __init__(self):
    print("---ClientTest---")
    #Para testes com clientInfo
    self.clientInfo = {'name':'Peter Quill', 'location':'Knowhere'}

    #Para testes com testClient
    self.testClient = Client('Peter Quill', 'Knowhere')
    

  def newClientShouldHaveNameandLocation(self):
    name = self.clientInfo['name']
    location = self.clientInfo['location']
    try:
      testClient = Client(self.clientInfo['name'], self.clientInfo['location'])
      print(testClient.getName())
      print(testClient.getLocation())
      print("PASS: Um client correto foi gerado")
    except Exception as e:
      print(str(e))
      print('FAILED: Client deve ter nome e local')
      return False

    return True

  def newClientWithoutNameShouldReturnError(self):
    try:
      testClient = Client(None, self.clientInfo['location'])
      print("PASS: Não foi possível gerar um client sem nome")
    except:
      print('FAILED: Client deve ter nome')
      return False

    return True   

  def newClientWithoutLocationShouldReturnError(self):
    try:
      testClient = Client(self.clientInfo['name'], None)
      print("PASS: Não foi possível gerar um client sem location")
    except:
      print('FAILED: Client deve ter local')
      return False
      
    return True   

  def ClientCanPlaceValidDefaultOrder(self):
    try:
      assert self.testClient.adicionarPedido({'id': 123456,'client': self.testClient.getName()}) == True
      print("PASS: Foi possível gerar um pedido padrão")
    except AssertionError:
      print("FAILED: Não foi posssível gerar um pedido padrão válido")
      raise

  def ClientCanPlaceValidOrderWithPriority(self):
    try:
      assert self.testClient.adicionarPedido({'id': 123456,'client': self.testClient.getName(),'priority':'Alta'}) == True
      print("PASS: Foi possível gerar um pedido padrão com prioridade")
    except AssertionError:
      print("FAILED: Não foi posssível gerar um pedido com prioridade válido")

  def ClientCantPlaceInvalidOrder(self):

    try:
      assert self.testClient.adicionarPedido({}) == False
      assert self.testClient.adicionarPedido({'id':123456}) == False
      assert self.testClient.adicionarPedido({'client':self.testClient.getName(),'priority':5}) == False
      print("PASS: Não foi possível gerar um pedido inválido")
    except AssertionError:
      print("FAILED: Não deveria ser possível gerar um pedido inválido")

  def ClientCantPlaceInvalidPriority(self):
    try:
      assert self.testClient.adicionarPedido({'client':self.testClient.getName(),'priority':9}) == False
      print("PASS: Não foi possível gerar um pedido com prioridade inválida")
    except AssertionError:
      print("FAILED: Não deveria ser possível gerar um pedido com prioridade inválida")


#Here be tests
testInstance = ClientTest()
testInstance.newClientShouldHaveNameandLocation()
testInstance.newClientWithoutLocationShouldReturnError()
testInstance.newClientWithoutNameShouldReturnError()
testInstance.ClientCanPlaceValidDefaultOrder()
testInstance.ClientCanPlaceValidOrderWithPriority()
testInstance.ClientCantPlaceInvalidOrder()
testInstance.ClientCantPlaceInvalidPriority()