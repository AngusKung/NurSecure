import logging
import pdb

from NurSecure.core import NurSecure

LOGFORMAT = '%(asctime).19s %(levelname)s %(filename)s Line %(lineno)s: %(message)s'
logging.basicConfig(format=LOGFORMAT)
logger = logging.getLogger('main')
logger.setLevel(logging.INFO)

if __name__ == '__main__':
    nursecure = NurSecure()
    nursecure.train()

    test_sentences = ["I've been having some pain in my joints.",
                      "Pain in the knees.",
                      "Four months ago and getting worse recently",
                      "Well I've certainly felt under the weather",
                      "Some. I like to play tennis about once a week. I take my dog on a walk every morning",
                      "My right knee hurts",
                      "Ouch",
                      'Should I see a doctor for a thorough check?']

    for sent in test_sentences:
        print(f'Human:\t\t{sent}')
        print(f'NurSecure:\t{nursecure.get_response(sent)}')

    print(f'\nStart your own chat here:')
    while True:
        user_input = input(f'You:\t\t')
        print(f'NurSecure:\t{nursecure.get_response(user_input)}')
