#!/usr/bin/env python
# encoding: utf-8

# OBS: o uso do '_' (underline) antes do nome da variavel é uma conveção
# indica que essa variavel é privada (EX: _ponto = (1,1))

from math import sqrt

class Ponto(object):
	def __init__(self, x, y):
		self.x = x
		self.y = y
	
	def __repr__(self):
		return "P(%s, %s)" % (self.x, self.y)
		
	def distancia(self, p2):
		return sqrt( pow(p2.x - self.x, 2) + pow(p2.y - self.y, 2))
		
class Linha(object):
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		
	def __repr__(self):
		return "L(%s, %s)" % (self.p1, self.p2)
		
	def comprimento(self):
		return self.p1.distancia(self.p2)
		
class Figura(object):
	pass
		
class Retangulo(Figura):
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
		
	def __repr__(self):
		return "R(%s, %s)" % (self.p1, self.p2)
	
#	@property	
#	def altura(self):
#		return self.p2.y - self.p1.y
#	@property	
#	def largura(self):
#		return self.p2.x - self.p1.x

	def _get_altura(self):	
		return self.p2.y - self.p1.y
		
	def _set_altura(self, altura):
		if altura < 0:
			raise ValueError("A altura deve ser positiva")
		self.p2.y = self.p1.y + altura
			
	altura = property(_get_altura, _set_altura)
	
	def _get_largura(self):	
		return self.p2.x - self.p1.x
		
	def _set_largura(self, largura):
		if largura < 0:
			raise ValueError("A largura deve ser positiva")
		self.p2.x = self.p1.x + largura
			
	largura = property(_get_largura, _set_largura)
		
	def area(self):
		return self.altura * self.largura
		
# OBS: quando colocamos o decorator "@property"	em um metodo ele passa
# a se comportar como atributo
if __name__ == "__main__":			
	p1 = Ponto(10, 10)
	p2 = Ponto(20, 15)

	print p1, p2
	print "d(P1, P2):", p1.distancia(p2)

	l1 = Linha(p1, p2)
	print "L1:", l1

	r1 = Retangulo(p1, p2)
	print "R1:", r1
	print "Area(R1)", r1.area()

	r1.altura = 10
	print "R1:", r1
	print "Area(R1)", r1.area()

	r1.largura = 5
	print "R1:", r1
	print "Area(R1)", r1.area()

	#r1.altura = -5
	#r1.largura = -5
	#print "R1:", r1
