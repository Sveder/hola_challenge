import json
from collections import defaultdict

words = open("words.txt").read().lower().split("\n")


def ngram(word, how_much):
    ngrams = []
    for i in xrange(len(word) - how_much + 1):
        ngrams.append(word[i:i + how_much])

    return ngrams


def ngram_list_of_words(words, how_much):
    en_gram_to_appearance_count = defaultdict(lambda: 0)

    for word in words:
        with_start_and_end = "^%s$" % word
        en_grams = ngram(with_start_and_end, how_much)

        for i in en_grams:
            en_gram_to_appearance_count[i] += 1

    return en_gram_to_appearance_count

def save_formatted_list(appearance_count, fobj):
    #First calculate percentages:
    item_count = float(sum(appearance_count.values()))

    for item in appearance_count:
        appearance_count[item] = float(appearance_count[item]) / item_count

    json.dump(appearance_count, fobj)


two_gram = ngram_list_of_words(words, 3)
two_gram_file = open("formatted_three.txt", 'w')
save_formatted_list(two_gram, two_gram_file)
two_gram_file.close()

import ipdb;ipdb.set_trace()

