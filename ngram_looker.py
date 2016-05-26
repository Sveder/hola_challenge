import json
import functools

two_freq = json.load(open("two_gram.txt", 'r'))
two_to_freq_dict = dict(two_freq)

three_freq = json.load(open("three_gram.txt", 'r'))
three_to_freq_dict = dict(three_freq)


def ngram_looker(word, max_len=13, min_sum=0.01, long_sum=0.1):
    word = "^%s$" % word
    sum = 0.0
    try:
        for i in xrange(0, len(word) - 1):
            tf = float(two_to_freq_dict[word[i:i+2]])
            sum += tf

        for i in xrange(0, len(word) - 2):
            tf = float(three_to_freq_dict[word[i:i+3]])
            sum += tf

    except KeyError:
        return False

    if len(word) > max_len and sum < long_sum:
        return False


    return sum > min_sum

def meta_looker(word_len, sum_min, long_sum=0.1):
    return functools.partial(ngram_looker, max_len=word_len, min_sum=sum_min, long_sum=long_sum)
