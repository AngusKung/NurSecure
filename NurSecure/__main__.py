import logging
from nursecure import NurSecure

import pdb

LOGFORMAT = "%(asctime).19s %(levelname)s %(filename)s Line %(lineno)s: %(message)s"
logging.basicConfig(format=LOGFORMAT)

logger = logging.getLogger("NurSecure")
logger.setLevel(logging.INFO)


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

