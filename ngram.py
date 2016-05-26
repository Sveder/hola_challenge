from collections import defaultdict

words = open("words.txt").read().lower().split("\n")

two_gram_to_appearance_count = defaultdict(lambda: 0)

def ngram(word, how_much):
    ngrams = []
    for i in xrange(len(word) - how_much + 1):
        ngrams.append(word[i:i + how_much])

    return ngrams

for word in words:
    with_start_and_end = "^%s$" % word
    two_grams = ngram(with_start_and_end, 3)

    for i in two_grams:
        two_gram_to_appearance_count[i] += 1

import ipdb;ipdb.set_trace()

