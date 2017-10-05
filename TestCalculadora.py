import unittest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):

	def setUp(self):
		self.calc = Calculadora()

	def test_valor_de_inicio_igual_a_cero(self):
		self.assertEquals(self.calc.resultado(), 0)

"""	def test_sumar_2_mas_2_igual_4(self):
		self.calc.suma(2, 2)
		self.assertEquals(self.calc.resultado(), 4)

	def test_sumar_3_mas_3_igual_6(self):
		self.calc.suma(3, 3)
		self.assertEquals(self.calc.resultado(), 6)
		
	def test_sumar_negativo_mas_positivo_igual_4(self):
		self.calc.suma(-2, 6)
		self.assertEquals(self.calc.resultado(), 4)		

	def test_sumar_numero_mas_letra(self):
		self.calc.suma(2, L)
		self.assertEquals(self.calc.resultado(), 4)		"""	


if __name__ == '__main__':
	unittest.main()