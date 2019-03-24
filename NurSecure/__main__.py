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

    from NurSecure.demoset import *
    # Load demoset and iterate through each demoset
    for idx, dialogue in enumerate(test_dialogues):
        print(f'\n=== Demo dialogues {idx+1} ===')
        for sent in dialogue:
            print(f'Human:\t\t{sent}')
            print(f'NurSecure:\t{nursecure.get_response(sent)}')

    print(f'\nStart your own chat here:')
    while True:
        user_input = input(f'You:\t\t')
        print(f'NurSecure:\t{nursecure.get_response(user_input)}')
