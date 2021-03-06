# coding: utf-8 -*-

from impressao import Impressao

class Subtracao(object):
	def __init__(self, expressao_esquerda, expressao_direita):
		self.__expressao_esquerda = expressao_esquerda
		self.__expressao_direita = expressao_direita

	def avalia(self):
		return (self.__expressao_direita.avalia() - 
			self.__expressao_esquerda.avalia()
		) 

	@property
	def expressao_esquerda(self):
		return self.__expressao_esquerda

	@property
	def expressao_direita(self):
		return self.__expressao_direita

	
	def aceita(self, visitor):
		visitor.visita_subtracao(self)

class Soma(object):
	def __init__(self, expressao_esquerda, expressao_direita):
		self.__expressao_esquerda = expressao_esquerda
		self.__expressao_direita = expressao_direita

	def avalia(self):
		return (self.__expressao_direita.avalia() + 
			self.__expressao_esquerda.avalia()
		) 

	@property
	def expressao_esquerda(self):
		return self.__expressao_esquerda

	@property
	def expressao_direita(self):
		return self.__expressao_direita
	
	
	def aceita(self, visitor):
		visitor.visita_soma(self)
		# chamando o proprio objecto instanciado

class Numero(object):

	def __init__(self, numero):
		self.__numero = numero

	def avalia(self):
		return self.__numero

	def aceita(self, visitor):
		visitor.visita_numero(self)


if __name__ == '__main__':

	from impressao import Impressao
	from prefixa_visitor import Prefixa_visitor


	expressao_esquerda = Soma(Numero(10), Numero(20))
	expressao_direita = Soma(Numero(5), Numero(2))
	expressao_conta = Soma(expressao_esquerda, expressao_direita)
	
	impressao = Impressao()
	prefixa_visitor = Prefixa_visitor()
	
	expressao_conta.aceita(impressao)	
	print '\nResultado = ', expressao_conta.avalia()
	expressao_conta.aceita(prefixa_visitor)

	#print expressao_conta.avalia()
	#expressao_conta2 = Subtracao(Numero(100), Numero(70))
	#print expressao_conta2.avalia()

