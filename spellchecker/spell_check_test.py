import unittest
from spell_checker import spell_checker

class testSpell_checker(unittest.TestCase):
	def setUp(self):
		self.spell_checker = spell_checker()
		self.spell_checker.load_words('spell.words')
		
	def test_spell_checker(self):
		self.assertTrue(self.spell_checker.check_word('zygotic'))
		failed_words = self.spell_checker.check_words('zygotic mistasdas speelllining')
		self.assertEquals(2, len(failed_words))
		self.assertEquals('mistasdas', failed_words[0])
		self.assertEquals(0, len(self.spell_checker.check_words('our first correct sentence')))
		#handle case sensitivity
		self.assertEquals(0, len(self.spell_checker.check_words('our first correct sentence')))
		#handle full stop
		self.assertEquals(0, len(self.spell_checker.check_words('our first correct sentence')))
		failed_words = self.spell_checker.check_words('zygotic mistasdas speelllining elementary')
		self.assertEquals(2, len(failed_words))
		self.assertEquals('mistasdas', failed_words[0])
		self.assertEquals('speelllining', failed_words[1])
		self.assertEqual(0, len(self.spell_checker.check_document('spell.words')))
		
		#self.assertFalse(self.spell_checker.check_words('zygotic mistasdas'))
		##self.assertTrue(self.spell_checker.check_words('our first correct sentence'))
		#self.assertTrue(self.spell_checker.check_words('our first correct sentence.'))
		#self.assertTrue(self.spell_checker.check_words('Our first correct sentence'))
		#self.assertFalse(self.spell_checker.check_words('zygotic mistasdas speelllining'))
		
if __name__=='__main__':
	unittest.main()