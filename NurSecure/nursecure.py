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
		self.conditions = set()

	def train(self, use_ubuntu_corpus=False):
		self._train_english_corpus()
		if use_ubuntu_corpus:
			self._train_ubuntu_corpus()

		self._train_medical_dialogues()

	def _train_english_corpus(self):
		logger.info("Training English dialogue...")
		trainer = ChatterBotCorpusTrainer(self.chatbot)
		trainer.train("chatterbot.corpus.english")

	def _train_ubuntu_corpus(self):
		trainer = UbuntuCorpusTrainer(self.chatbot)
		trainer.train()

	def _train_medical_dialogues(self):
		logger.info("Training custom medical dialogues")
		trainer = ChatterBotCorpusTrainer(self.chatbot)
		trainer.train("data.medical")

	def get_response(self, string):
		chat_response = self.chatbot.get_response(string)
		med_condition = Comprehend().query(string)
		# FIXME: How to get conditions? (*** AttributeError: 'Condition' object has no attribute '__entities')

		# TODO: Parse med_condition into class state, output at last recommendation
		return chat_response

