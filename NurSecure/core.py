import logging

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, UbuntuCorpusTrainer

from .aws.comprehend import Comprehend

logger = logging.getLogger('NurSecure')


class NurSecure:
    '''
    NurSecure is a chatbot for health-care consultancy under total privacy.
    '''

    def __init__(self):
        self.chatbot = ChatBot('NurSecure')  # ChatterBot class
        self.history = []
        self.comprehend = Comprehend()

    def __train_english_corpus(self):
        logger.info('Training English dialogue...')
        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer.train('chatterbot.corpus.english')

    def __train_ubuntu_corpus(self):
        trainer = UbuntuCorpusTrainer(self.chatbot)
        trainer.train()

    def __train_custom_medical_corpus(self):
        logger.info('Training custom medical dialogues')
        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer.train('data.medical')

    def train(self, use_ubuntu_corpus=False):
        self.__train_english_corpus()
        if use_ubuntu_corpus:
            self.__train_ubuntu_corpus()

        self.__train_custom_medical_corpus()

    def get_response(self, user_input: str):
        chat_response = str(self.chatbot.get_response(user_input))
        self.history.append(user_input)

        if 'NurSecure Recommends' in chat_response:  # Final state
            med_condition = self.comprehend.query('. '.join(self.history))
            paired_condition = tuple(
                med_condition.organs.union(med_condition.symptoms))
            if paired_condition:
                med_response = f':\n\t\tDetected conditions: {paired_condition}'
                return chat_response + med_response
            return 'No medical issues detected.'
        return chat_response
