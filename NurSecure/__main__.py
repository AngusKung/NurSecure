from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

import pdb

class NurSecure:
	'''
	NurSecure is a chatbot for health-care consultancy under total privacy.
	'''

	def __init__(self):

		self.chatbot = ChatBot('NurSecure')

	def train_english_dialogue(self):
		trainer = ChatterBotCorpusTrainer(self.chatbot)
		trainer.train("chatterbot.corpus.english")

	def get_response(self, string):
		return self.chatbot.get_response(string)

if __name__ == "__main__":
	nursecure = NurSecure()
	nursecure.train_english_dialogue()

	print(nursecure.get_response("How do you do?"))
	print(nursecure.get_response("Are you a real human?"))

	pdb.set_trace()

