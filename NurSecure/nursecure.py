import logging
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, UbuntuCorpusTrainer
from aws.comprehend import Comprehend

logger = logging.getLogger("NurSecure")
import pdb

class NurSecure:
	'''
	NurSecure is a chatbot for health-care consultancy under total privacy.
	'''

	def __init__(self):
		self.chatbot = ChatBot('NurSecure') # ChatterBot class
		self.history = []

	def train(self, use_ubuntu_corpus=False):
		self._train_english_corpus()
		if use_ubuntu_corpus:
			self._train_ubuntu_corpus()

		self._train_custom_medical_corpus()

	def _train_english_corpus(self):
		logger.info("Training English dialogue...")
		trainer = ChatterBotCorpusTrainer(self.chatbot)
		trainer.train("chatterbot.corpus.english")

	def _train_ubuntu_corpus(self):
		trainer = UbuntuCorpusTrainer(self.chatbot)
		trainer.train()

	def _train_custom_medical_corpus(self):
		logger.info("Training custom medical dialogues")
		trainer = ChatterBotCorpusTrainer(self.chatbot)
		trainer.train("data.medical")

	def get_response(self, string):
		chat_response = str(self.chatbot.get_response(string))
		self.history.append(string)

		if 'NurSecure Recommends' in chat_response: # Final state
			med_condition = Comprehend().query('. '.join(self.history))
			paired_condition = tuple(med_condition.organs.union(med_condition.symptoms))
			if len(paired_condition) > 0:
				med_response = ":\n\t\tDetected conditions: " + str(paired_condition)
				return chat_response + med_response
			else:
				return "No medical issues detected."
		else:
			return chat_response
