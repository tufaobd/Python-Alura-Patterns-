# coding: utf-8 -*-

class Impressao(object):

	def visita_soma(self, soma):
		print '(',
		soma.expressao_esquerda.aceita(self)
		# visita expressão esquerda
		print '+',
		# visita expressao direita
		soma.expressao_direita.aceita(self)
		print ')',

	def visita_subtracao(self, subtracao):
		print '(',
		subtracao.expressao_esquerda.aceita(self)
		# visita expressão esquerda
		print '-',
		subtracao.expressao_direita.aceita(self)
		# visita expressao direita
		print ')',


	def visita_numero(self, numero):
		print numero.avalia(),