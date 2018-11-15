import random
import string

# INPUT

TEST_INPUT = 'Hello, world!'


# Helper methods

def randchar():
    return random.choice(string.printable)

def randstr(length):
    return ''.join(randchar() for i in range(length))

# String fitness measure

def fitness(target,test): 
    return sum(abs(ord(i) - ord(j)) for i,j in zip(target,test))

# Randomly guesses once on each character keeping the best guess for the next round

def _guess(target,guess,_fitness,gen=0):
    children = []
    for i in range(len(guess)):
        child = guess
        child = guess[:i] + randchar() + guess[i+1:]
        children.append(child)
    best_child = min(children,key=_fitness)
    # print("Gen:",gen,"Fitness:",_fitness(best_child),"Best:",best_child)
    if _fitness(best_child) == 0:
        return best_child,gen
    else:
        return _guess(target,best_child,_fitness,gen+1)

def guess(target):
    def _fitness(test):
        return fitness(target,test)
    return _evolve(target,randstr(len(target)),_fitness)

# print(guess('The world at large is not so small'))


# Evolutionary attempt
# Begin with N parents


def initial_population(target,population_size=100):
    L = len(target)
    return [randstr(L) for i in range(population_size)] 

def breed(*args,**kwargs):
    return outbreed_paired(*args,**kwargs)

def inbreed_paired(population,_fitness,mutation_rate=0.5):
    L = len(population)
    for i in range(0,L,2):
        population.append(make_child(population[i],population[i+1],mutation_rate))
    return sorted(population,key=_fitness)[:L]

def inbreed_everyone(population,_fitness,mutation_rate=0.5):
    L = len(population)
    for i in range(L):
        for j in range(i+1,L):
            population.append(make_child(population[i],population[j],mutation_rate))
    return sorted(population,key=_fitness)[:L]

def outbreed_paired(population,_fitness,mutation_rate=0.5):
    L = len(population)
    other = initial_population(population[0],L)
    for i in range(L):
        population.append(make_child(population[i],other[i],mutation_rate))
    return sorted(population,key=_fitness)[:L]

def make_child(*args,**kwargs):
    return make_child_inherit(*args,**kwargs)

def make_child_average(parent1,parent2,mutation_rate=0.5):
    _child = ''.join(chr((ord(ch1)+ord(ch2))//2) for ch1,ch2 in zip(parent1,parent2))
    child = ''
    for ch in _child:
        if random.random() < mutation_rate:
            child += randchar()
        else:
            child += ch
    return child

def make_child_inherit(parent1,parent2,mutation_rate=0.5):
    L = len(parent1)
    p1 = L//2
    p2 = L - p1
    genes = [0]*p1 + [1]*p2
    random.shuffle(genes)
    child = ""
    parents = (parent1,parent2)
    for i in range(L):
        if random.random() < mutation_rate:
            child += randchar()
        else:
            child += parents[genes[i]][i]
    return child

def evolve(target):
    def _fitness(test):
        return fitness(target,test) 
    population = initial_population(target)
    population = sorted(population,key=_fitness)
    gen = 1
    mutation_rate = .1#1/len(target)
    while _fitness(population[0]) > 0:
        best = population[0]
        print("Gen:",gen,"Fitness:",_fitness(population[0]),"Best:",population[0])
        population = breed(population,_fitness,mutation_rate)
        gen += 1
    best = population[0]
    print("Gen:",gen,"Fitness:",_fitness(best),"Best:",best)
    return best,gen

#print(evolve(TEST_INPUT))
print(evolve("This land is your land! This land is my land! From california to Jenny's cellphone 867-5309"))

