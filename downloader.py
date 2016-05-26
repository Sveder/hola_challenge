import os
import requests

TEST_CASE_URL = "https://hola.org/challenges/word_classifier/testcase/%s" # % (number_of_test_case, )
OUTPUT_DIR = "outputs"

for test_case in xrange(1, 100000):
    response = requests.get(TEST_CASE_URL % test_case)
    f = open(os.path.join(OUTPUT_DIR, "%s.json" % test_case), 'w')
    f.write(response.text)
    f.close()

