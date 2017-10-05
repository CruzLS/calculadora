class Calculadora(object):
	def __init__(self):
		self.resultado = 0

	def suma(self, n1, n2):
		self.resultado = n1 + n2

	def resta(self, n1, n2):
		self.resultado = n1 - n2	

	def multiplicacion(self, num1, num2):
			self.resultado = num1 * num2

	def division(self, num1, num2):
		self.resultado = num1 / num2

	def pow(self, num1):
		self.resultado = num1 ** 2	

	def sqrt(self, num1):
		self.resultado = num1 ** 0.5

	def obtener_resultado(self):
		return self.resultado



	