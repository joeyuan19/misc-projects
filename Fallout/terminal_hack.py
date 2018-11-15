import sys


words = [
    'destructive',
    'devastation',
    'observation',
    'destruction',
    'radioactive',
    'radioactive',
    'rectangular',
    'reprimanded',
]

def common(a,b):
    return sum(i == j for i,j in zip(a,b))

def dmin(d):
    m = 1000000000
    _k = ''
    for k,v in d.items():
        if v < m:
            _k = k
            m = v
    return _k,m

def dmax(d):
    m = 0
    _k = ''
    for k,v in d.items():
        if v > m:
            _k = k
            m = v
    return _k,m

def get_matches(word,n,words):
    return [_word for _word in words if common(word,_word) == n]

def get_matches_multiple(guesses,words):
    a = set(words)
    for guess,n in guesses:
        a = a.intersection(set(get_matches(guess,n,words)))
    return a


for i,word in enumerate(words):
    words[i] = word.upper()
    if len(word) != len(words[0]):
        print(word,"is not correct length")
        sys.exit()

avg = {word:sum(common(word,_word)/(len(words)-1) for _word in words if _word != word) for word in words}

print('Averages')
print(avg)

print('Most commonality')
print(dmax(avg))

print('Least commonality')
print(dmin(avg))

gs = []
for i in range(1,5):
    while True:
        g = input('Word(' + str(i) + '):\n')
        if g in words:
            n = int(input('?/' + str(len(words[0])) + ' correct:\n'))
            gs.append((g,n))
            for item in get_matches_multiple(gs,words):
                print('\t',item,avg[item])
            break
        else:
            print('WORD NOT FOUND')



