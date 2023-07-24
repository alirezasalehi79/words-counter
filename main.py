from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import wordnet as wn
from PyDictionary import PyDictionary

dictionary = PyDictionary()

def counter(x):

    z = x.replace("."," ")
    d = z.replace(',','')
    lst = d.split(' ')

    y = []
    i = 0
    counter = 0
    while i < len(lst):
        if lst[i] not in y:
            y.append(lst[i])
        i += 1

    for j in y:
        counter += 1
    return counter

def sentences(text):
    x = text.split(".")
    counter = 0
    i = 0
    while i < len(x):
        counter += 1
        i += 1

    return counter

def remove_stop_words(x):

    z = x.replace('.', ' ')
    d = z.replace(',', '')

    stopWords = set(stopwords.words('english'))
    words = word_tokenize(d)

    wordsFiltered = []

    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)

    return len(wordsFiltered)

def number_of_words(text):

    x = text.replace(".", " ")
    z = x.replace(',', '')
    y = z.split(' ')
    g = ' '.join(y)

    h = []
    for i in y:
        if i != '':
            h.append(i)

    stopWords = set(stopwords.words('english'))
    words = word_tokenize(g)
    wordsFiltered = []

    for w in words:
        if w not in stopWords:
            wordsFiltered.append(w)

    z = []
    for i in wordsFiltered:
        x = dictionary.meaning(i)
        y = list(x.keys())
        z.append(y)

    g = []

    for i in range(len(z)):
        g.append(z[i][0])

    counterAdv = 0
    counterAdj = 0
    counterVerb = 0
    counterNoun = 0

    for k in g:

        if k == 'Noun':
            counterNoun += 1
        elif k == 'Verb':
            counterVerb += 1
        elif k == 'Adjective':
            counterAdj += 1
        else:
            counterAdv += 1

    return counterAdj,counterAdv,counterVerb,counterNoun

def characters(text):

    x = text.replace(".", " ")
    z = x.replace(',', '')
    y = z.split(' ')
    g = ' '.join(y)

    counter = 0

    for i in g:

        if  ((ord(i) >= 65 and ord(i) <= 90) or (ord(i) >= 97 and ord(i) <= 122)):
            counter += 1

    return counter

def short_or_long(text):

    x = text.replace(".", " ")
    z = x.replace(',', '')
    y = z.split(' ')

    i = 0
    counterMedium = 0
    counterLong = 0
    counterShort = 0

    while i < len(y):

        if (len(y[i]) >= 5 and len(y[i]) < 10):
            counterMedium += 1
        elif (len(y[i]) >= 10):
            counterLong += 1
        else:
            counterShort += 1
        i += 1

    return counterShort,counterMedium,counterLong

text = input('enter your text : ')
print(f'number of words : {counter(text)}')
print(f'number of sentences : {sentences(text)}')
print(f'number of meaningful words : {remove_stop_words(text)}')

adjectives,adverbs,verbs,nouns = number_of_words(text)

print(f'adjectives : {adjectives}')
print(f'adverbs : {adverbs}')
print(f'verbs : {verbs}')
print(f'nouns : {nouns}')
print(f'number of characters : {characters(text)}')

short,medium,long = short_or_long(text)

print(f'short words : {short} ')
print(f'medium words : {medium} ')
print(f'long words : {long} ')


