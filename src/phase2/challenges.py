from collections import Counter

import heapq

def most_frequent(lst):
    return Counter(lst).most_common(1)[0][0]
def top_n_sum(lst, n):
    return sum(heapq.nlargest(n, lst))

def is_palindrome(s):
    s = ''.join(s.lower().split())
    return s == s[::-1]

def flatten(lst):
    for x in lst:
        if isinstance(x, list):
            yield from flatten(x)
        else:
            yield x

        # acrobatique & plus gourmand
        [item for sublist in lst for item in sublist]
        [item for sublist in lst for item in (flatten(sublist) if isinstance(sublist, list) else [sublist])]


from collections import defaultdict

def group_anagrams(words):
    d = defaultdict(list)
    for word in words:
        d[''.join(sorted(word))].append(word)
    return list(d.values())

def merge_sorted(l1:list, l2):
    from heapq import merge
    return list(merge(l1, l2))


def longest_word(sentence):
    return max(sentence.split(), key=len)

def char_histogram(s):
    return dict(Counter(s))
def all_indices(lst, value):
    return [i for i, x in enumerate(lst) if x == value]