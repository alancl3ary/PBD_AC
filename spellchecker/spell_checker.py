#spell_checker


class spell_checker:
	def __init__(self):
		self.words= []
	def load_words(self, file_name):
		self.words = open(file_name).readlines()
		self.words= map(lambda x: x.strip(), self.words)
		#return words


	def check_word(self, word):
		#return word in self.words
		return word.strip('.').lower() in self.words # line changed so test runs with capitals and full stops. 
	def check_words(self, sentence):
		words_to_check = sentence.split(' ')
		failed_words=[]
		for word in words_to_check:
			if not self.check_word(word):
				print ("Word is misspelt : " + word )
				failed_words.append(word)
			
		return failed_words
		
if __name__ =='__main__':
		
	spell_check = spell_checker()

	spell_check.load_words("spell.words")
	#print words[0]
	#print load_words("spell.words")[0]

	print spell_check.check_word("zygotic")
	print spell_check.check_word("mistasdas")
	print spell_check.check_words("zygotic mistasdas elementary")

