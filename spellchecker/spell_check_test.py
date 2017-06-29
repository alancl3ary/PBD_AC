import unittest
from spell_checker import spell_checker

class testSpell_checker(unittest.TestCase):
	def setUp(self):
		self.spell_checker = spell_checker()
		self.spell_checker.load_words('spell.words')
		
	def test_spell_checker(self):
		self.assertTrue(self.spell_checker.check_word('zygotic'))
		self.assertFalse(self.spell_checker.check_words('zygotic mistasdas'))
		self.assertTrue(self.spell_checker.check_words('our first correct sentence'))
		self.assertTrue(self.spell_checker.check_words('our first correct sentence.'))
		self.assertTrue(self.spell_checker.check_words('Our first correct sentence'))
		self.assertFalse(self.spell_checker.check_words('zygotic mistasdas speelllining'))
		
if __name__=='__main__':
	unittest.main()