import random
import itertools

class Person(object):
    def evaluate(self,statement):
        pass
    def ask(self,statement):
        return self.evaluate(statement)

class Liar(Person):
    def evaluate(self,statement):
        return not statement
    def check(self,_type):
        return _type == 'F'

class Random(Person):
    def evaluate(self,statement):
        return random.choice([True,False])
    def check(self,_type):
        return _type == 'R'

class Truth(Person):
    def evaluate(self,statement):
        return statement
    def check(self,_type):
        return _type == 'T'

class Group(object):
    def __init__(self,g=None):
        if g is not None:
            self.people = g
        else:
            self.random_setup() 

    def random_setup(self):
        R = Random()
        T = Truth()
        F = Liar()
        
        self.people = [R,T,F]
        random.shuffle(self.people)

    def ask(self,person,statement):
        return self.people[person].ask(statement)

    def get_others(self,exception):
        return self.people[:exception]+self.people[exception+1:]

    def get(self,person):
        return self.people[person]

    def guess(self,types):
        return all(i.check(_type) for i,_type in zip(self.people,types))

class AllGroups(object):
    def __init__(self):
        R = Random()
        T = Truth()
        F = Liar()
        
        self.groups = tuple(Group(i) for i in itertools.permutations((R,T,F)))

    def check(self,f):
        c = 0
        for g in self.groups:
            c += g.guess(f(g))
        return c

def guess(g):
    idx = 0
    if g.ask(idx,any(i.check('F') for i in g.get_others(idx))):
        idx += 1
        if g.ask(idx,any(i.check('F') for i in (g.get(idx),g.get(idx+1)))):
            return ('A','A','A')
        else:
            return ('','','')
    if g.ask(idx+1,g.people[idx].check('R')):
        return ('R','T','F')
    else:
        return ('R','F','T')

def guess1(g):
    idx = 0
    if g.ask(idx,any(i.check('F') for i in g.get_others(idx))):
        idx += 1
        if g.ask(idx,any(i.check('F') for i in g.get_others(idx))):
            return ('A','A','A')
    if g.ask(idx+1,g.people[idx].check('R')):
        return ('R','T','F')
    else:
        return ('R','F','T')
            

ag = AllGroups()

N = 1e4
N = int(N)
c = 0.
for n in range(N):
    c += ag.check(guess)
print(c,'/',N,'=',c/N)
