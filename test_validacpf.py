import os
import unittest
from src.validacpf_marco import Validator


cpf_formatado = '44194517857'


class Tester(unittest.TestCase):

	def test_formatacao(self):
		self.assertEqual(Validator().retira_formatacao('441.945.178-57'), cpf_formatado)
		self.assertFalse(Validator().retira_formatacao('oi'))
		self.assertTrue(Validator().retira_formatacao('441-945-178-57'),cpf_formatado)
		self.assertTrue(Validator().retira_formatacao('009.449.081-36'))
		self.assertTrue(Validator().retira_formatacao('003516559-64'))
		self.assertTrue(Validator().retira_formatacao('00034452915'))
		pass


	def test_validacao(self):
		self.assertTrue(Validator().valida_cpf('441.945.178-57'))
		self.assertTrue(Validator().valida_cpf('009.449.081-36'))
		self.assertTrue(Validator().valida_cpf('003516559-64'))
		self.assertTrue(Validator().valida_cpf('00034452915'))
		self.assertFalse(Validator().valida_cpf('feijoada'))
		self.assertFalse(Validator().valida_cpf('111.111.111-11'))
		self.assertFalse(Validator().valida_cpf('-------------'))
		pass


if __name__ == '__main__':
	unittest.main()
