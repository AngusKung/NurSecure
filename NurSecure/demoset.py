import os
import yaml

test_dialogues = []

dialogue_path = 'data/medical/'
for filename in os.listdir(dialogue_path):
    with open(os.path.join(dialogue_path + filename)) as stream:
        data_loaded = yaml.load(stream)
        dialogue = data_loaded['conversations'][0]
        # Take only sentences from one of the speaker
        test_dialogues.append([sent for idx, sent in enumerate(dialogue) if idx%2 == 0])
