import os
import unittest
from src.validacpf_marco import Validator


cpf_formatado = '44194517857'


class Tester(unittest.TestCase):

	def test_formatacao(self):
		self.assertEqual(Validator().retira_formatacao('441-945-178-57'), cpf_formatado)
		pass

	def test_validacao(self):
		self.assertTrue(Validator().retira_formatacao('441.945.178-57'))
		pass


if __name__ == '__main__':
	unittest.main()
