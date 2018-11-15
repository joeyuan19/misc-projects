import random

"""
SPADES = 1
HEARTS = 2
DIAMONDS = 3
CLUBS = 4

JACK = 11
QUEEN = 12
KING = 13
ACE = 14

HIGH CARD       = 1
ONE PAIR        = 2
TWO PAIR        = 3
THREE OF A KIND = 4
STRAIGHT        = 5
FLUSH           = 6
FULL HOUSE      = 7
4 OF A KIND     = 8
STRAIGHT FLUSH  = 9
"""

class Deck(object):
    def __init__(self):
        self.deck = [(i,j) for i in range(1,5) for j in range(1,15)]
        random.shuffle(self.deck)

    def draw(self):
        return self.deck.pop()

def high(h):
    return (1,) + tuple(sorted([c[1] for c in h])[::-1])

def pair(h):
    for i,c in enumerate(h):
        for j,_c in enumerate(h[i+1:]):
            if _c[1] == c[1]:
                return (2,c[1]) + tuple(sorted([c[1] for k,c in enumerate(h) if k not in (i,i+j+1)])[::-1])
    return None

def twopair(h):
    m1 = -1
    for i,c in enumerate(h):
        for _c in h[i+1:]:
            if _c[1] == c[1]:
                if m1 < 0:
                    m1 = c[1]
                else:
                    return (3,max(m1,c[1]),min(m1,c[1]),[_c for _c in h if _c[1] not in (m1,c[1])][0][1])
    return None

def threekind(h):
    m = -1
    for i,c in enumerate(h):
        for j,_c in enumerate(h[i+1:]):
            for __c in h[i+j+1:]:
                if c[1] == _c[1] == __c[1]:
                    return (4,c[1]) + tuple(sorted([_c[1] for _c in h if _c[1] != c[1]])[::-1])
    return None

def straight(h):
    _h = sorted(h,key=lambda x: x[1])
    for i,c in enumerate(_h[1:]):
        if c[1]-1 != _h[i][1]:
            return None
    return (5,_h[0][1])

def flush(h):
    s = h[0][0]
    for c in h[1:]:
        if s != c[0]:
            return None
    return (6,) + tuple(sorted([c[1] for c in h])[::-1])

def fullhouse(h):
    m = -1
    r = threekind(h)
    if r is not None:
        if r[2] == r[3]:
            return (7,r[1],r[2])
    return None

def fourkind(h):
    _h = [c[1] for c in h]
    for i in _h[:2]:
        if _h.count(i) == 4:
            return (8,i)
    return None

def straightflush(_h):
    f = flush(_h)
    s = straight(_h)
    if f is not None and s is not None:
        return (9,s[1])

def get_hand(h):
    for f in [straightflush,fourkind,fullhouse,flush,straight,threekind,twopair,pair,high]:
        _h = f(h)
        if _h is not None:
            break
    return _h

def compare_hands(_h1,_h2):
    h1 = get_hand(_h1)
    h2 = get_hand(_h2)
    return _compare_hands(h1,h2)

def _compare_hands(h1,h2):
    for i in range(max(len(h1),len(h2))):
        if h1[i] > h2[i]:
            return 1
        elif h2[i] > h1[i]:
            return 2
    return 0

def play_hand(_players,dealer):
    deck = Deck()
    idx = _players.index(dealer)
    _players = _players[idx+1:] + _players[:idx+1]
    hands = [[] for p in _players]
    for c in range(5):
        for p in range(len(hands)):
            hands[p].append(deck.draw())
    results = sorted([(get_hand(h),p) for h,p in zip(hands,_players)])
    if _compare_hands(results[0][0],results[1][0]) == 0:
        r = -1
    else:
        r = results[0][1]
    return r

def play_game(n_players,start_dealer):
    dealer = start_dealer 
    players = [9 for i in range(n_players)]
    left = [i for i,j in enumerate(players) if j > 0]
    while len(left) > 1:
        loser = play_hand(left,dealer)
        if loser < 0:
            pass # Tie
        else:
            players[loser] -= 1
            left = [i for i,j in enumerate(players) if j > 0]
        dealer = (dealer+1)%n_players
        while dealer not in left:
            dealer = (dealer+1)%n_players
    return left[0], start_dealer

def stats(players,trials=1000,start_dealer_mode=False):
    wins = [0 for i in range(players)]
    dealer = [0 for i in range(players)]
    for trial in range(trials):
        if start_dealer_mode == 0:
            start_dealer = random.randint(0,players-1)
        elif start_dealer_mode == 1:
            start_dealer = 0
        elif start_dealer_mode == 2:
            start_dealer = random.randint(0,players-2)
        winner,start_dealer = play_game(players,start_dealer)
        wins[winner] += 1
        dealer[start_dealer] += 1
    data = []
    for player,win_dealer in enumerate(zip(wins,dealer)):
        win,dealer = win_dealer
        data.append((player,win/trials,dealer/trials))
    return tuple(data)

S = [0,1,2]
P = [2,3,4,5]
N = [10,100,1000,10000,100000]
for s in S:
    for p in P:
        for n in N:
            print(s,p,n)
            data = stats(p,n,s)
            with open('stud_data.txt','a') as f:
                for player in data:
                    f.write(','.join(str(i) for i in (s,p,n)+player)+'\n')


