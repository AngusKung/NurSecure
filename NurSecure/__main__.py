import logging
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, UbuntuCorpusTrainer

import pdb

LOGFORMAT = "%(asctime).19s %(levelname)s %(filename)s Line %(lineno)s: %(message)s"
logging.basicConfig(format=LOGFORMAT)

logger = logging.getLogger("fastGraph")
logger.setLevel(logging.INFO)

class NurSecure:
	'''
	NurSecure is a chatbot for health-care consultancy under total privacy.
	'''

	def __init__(self):
		logger.info("Hello world!")
		self.chatbot = ChatBot('NurSecure')

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
		# NOTE: Yet to be fixed.
		trainer = UbuntuCorpusTrainer(self.chatbot)
		trainer.train()

	def _train_medical_dialogues(self):
		logger.info("Training custom medical dialogues")
		trainer = ChatterBotCorpusTrainer(self.chatbot)
		trainer.train("data.medical")

	def get_response(self, string):
		return self.chatbot.get_response(string)

if __name__ == "__main__":
	nursecure = NurSecure()
	nursecure.train()

	test_sentences = [
		"How do you do?",
		"Are you a real human?",
		"I'm not feeling well",
		"My right knee hurts",
		"Ouch!",
		"Should I see a doctor for a thorough check?"
	]

	for sent in test_sentences:
		print("Human:\t\t"+sent)
		print("NurSecure:\t"+str(nursecure.get_response(sent)))

	pdb.set_trace()

