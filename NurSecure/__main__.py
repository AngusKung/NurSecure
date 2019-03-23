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

    print("\n=== First sample dialogues ===")
    test_dialogue1 = ["I've been having some pain in my joints.",
                      "Pain in the knees.",
                      "Four months ago and getting worse recently",
                      "Well I've certainly felt under the weather",
                      "Some. I like to play tennis about once a week. I take my dog on a walk every morning",
                      "My right knee hurts",
                      "Ouch",
                      'Should I see a doctor for a thorough check?']
    for sent in test_dialogue1:
        print(f'Human:\t\t{sent}')
        print(f'NurSecure:\t{nursecure.get_response(sent)}')

    print("\n=== Second sample dialogues ===")
    test_dialogue2 = ["It's quite hard for me to breathe normally lately",
                      "I felt like my lung is going to explode",
                      "Unbearable itchy. How should I solve this?"]
    for sent in test_dialogue2:
        print(f'Human:\t\t{sent}')
        print(f'NurSecure:\t{nursecure.get_response(sent)}')

    print("\n=== Third sample dialogues ===")
    test_dialogue3 = ["I felt quite dizzy lately",
                      "A feew weeks",
                      "Yes, fatique and some time my heart hurts.",
                      "Around 4 hours",
                      "What else can I do to solve this?"]
    for sent in test_dialogue3:
        print(f'Human:\t\t{sent}')
        print(f'NurSecure:\t{nursecure.get_response(sent)}')

    print(f'\nStart your own chat here:')
    while True:
        user_input = input(f'You:\t\t')
        print(f'NurSecure:\t{nursecure.get_response(user_input)}')
