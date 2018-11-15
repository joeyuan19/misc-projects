import random
#import matplotlib.pyplot as plt


class Die(object):
    def __init__(self,sides=6,*args,**kwargs):
        self.clear_history()
        if sides < 1:
            raise TypeError("Die must have at least one side")
        self.sides = sides

    def clear_history(self):
        self.roll_history = []

    def roll(self):
        self.roll_history.append(1 + int((self.sides-1)*random.random()))
        return self.roll_history[-1]

sides = 10
die_a = Die(sides)
die_b = Die(sides+1)

histo = {}

for i in range(1000000):
    roll_a = die_a.roll()
    roll_b = die_b.roll()
    if roll_a in histo:
        histo[roll_a].append(roll_b)
    else:
        histo[roll_a] = [roll_b]

for i in histo:
    print i,len([j for j in histo[i] if j > i])/float(len(histo[i])),float(sides-i)/sides



