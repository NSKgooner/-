import numpy as np
with open('speeches.txt', 'r') as f:
    trump = f.read()

corpus = trump.split()

print(len(corpus))


def make_pairs(corpus):
    for i in range(len(corpus) - 1):
        yield (corpus[i], corpus[i+1])


pairs = make_pairs(corpus)

word_dict = {}

for word_1, word_2 in pairs:
    if word_1 in word_dict.keys():
        word_dict[word_1].append(word_2)
    else:
        word_dict[word_1] = [word_2]

print(word_dict['so'])

first_word = np.random.choice(corpus)

chain = [first_word]

n_words = 30

for i in range(n_words):
    chain.append(np.random.choice(word_dict[chain[-1]]))

print(' '.join(chain))
