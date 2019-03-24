import logging
from collections import Counter

from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer, UbuntuCorpusTrainer

from NurSecure.specialty import SPECIALTIES
from .aws.comprehend import Comprehend

logger = logging.getLogger('NurSecure')
import pdb

class NurSecure:
    '''
    NurSecure is a chatbot for health-care consultancy under total privacy.
    '''

    def __init__(self):
        self.chatbot = ChatBot('NurSecure')  # ChatterBot class
        self.med_conditions = []
        self.comprehend = Comprehend()
        self.symptom_specialty_dict = {symptom: key for key, symptom_list in SPECIALTIES.items() for symptom in symptom_list}

    def train(self, use_ubuntu_corpus=False):
        self.__train_english_corpus()
        if use_ubuntu_corpus:
            self.__train_ubuntu_corpus()

        self.__train_custom_medical_corpus()

    def get_response(self, user_input: str):
        chat_response = str(self.chatbot.get_response(user_input))
        med_condition = self.comprehend.query(user_input)
        paired_condition = tuple(med_condition.organs.union(med_condition.symptoms))
        if len(paired_condition) > 0:
            med_response = f'\n\t\t - Detected medical conditions: '+ ' '.join(paired_condition)
            self.med_conditions.append(paired_condition)
        else:
            med_response = f'\n\t\t - No medical condition detected'

        if 'NurSecure Recommends' in chat_response:  # Final state
            return self.__final_statement(chat_response)
        return chat_response + med_response

    def reset(self):
        self.med_conditions = []

    def __train_english_corpus(self):
            logger.info('Training English dialogue...')
            trainer = ChatterBotCorpusTrainer(self.chatbot)
            trainer.train('chatterbot.corpus.english.greetings',
                          'chatterbot.corpus.english.conversations',
                          'chatterbot.corpus.english.health',
                          'chatterbot.corpus.english.humor',
                          'chatterbot.corpus.english.ai',
                          )

    def __train_ubuntu_corpus(self):
        trainer = UbuntuCorpusTrainer(self.chatbot)
        trainer.train()

    def __train_custom_medical_corpus(self):
        logger.info('Training custom medical dialogues')
        trainer = ChatterBotCorpusTrainer(self.chatbot)
        trainer.train('data.medical', 'data.state')

    def __final_statement(self, chat_response):
        if len(self.med_conditions) > 0:
            specialty_recommed = self.__get_specialty()
            self.reset()
            return chat_response + specialty_recommed
        else:
            return 'No medical conditions detected during chat. Please give more information about your discomfort.'

    def __get_specialty(self):
        all_specialty = []
        all_symptom = []
        for tup in self.med_conditions:
            for elem in tup:
                if elem in self.symptom_specialty_dict:
                    all_specialty.append(self.symptom_specialty_dict[elem])
                    all_symptom.append(elem)

        recommendations = [f'\t\t{idx+1}. "{specialty}" due to "{all_symptom[idx]}"' for idx, specialty in enumerate(all_specialty)]
        # TODO: Order by count, more appearance goes first

        return f' to go for:\n' + '\n'.join(recommendations)