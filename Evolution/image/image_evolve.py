from sys import argv
from PIL import Image
import random
import os

def clear_out():
    for root, dirs, files in os.walk('out', topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))

def write_improvement(data,i):
    with open("out/img-evolve-"+str(i)+".txt",'w') as f:
        f.write(','.join(str(i) for i in data)+',')

def load_target(image_file):
    image = Image.open(image_file)
    im = image.getdata()
    pixdata = [x for pix in im for x in pix]
    del(im)
    with open('out/dimensions.txt','w') as f:
        f.write("WIDTH  : "+str(image.width)+"\n")
        f.write("HEIGHT : "+str(image.height))
        print("WIDTH  : "+str(image.width))
        print("HEIGHT : "+str(image.height))
    image.close()
    return pixdata

def fitness(target,test):
    return sum(abs(target_i-test_i) for target_i,test_i in zip(target,test))

def randpix():
    return random.randint(0,255)

def randinit(N):
    return [randpix() for i in range(N)]

def initial_population(target,population_size=100):
    L = len(target)
    return [randinit(L) for i in range(population_size)] 

def breed(population,_fitness,mutation_rate=0.5):
    L = len(population)
    for i in range(L):
        for j in range(i+1,L):
            population.append(make_child(population[i],population[j],mutation_rate))
    return sorted(population,key=_fitness)[:L]

def make_child(parent1,parent2,mutation_rate=0.5):
    child = [(p1 + p2)//2 for p1,p2 in zip(parent1,parent2)]
    if random.random() < mutation_rate:
        child[random.randint(0,len(child)-1)] = randpix() 
    return child
    """
    L = len(parent1)
    p1 = L//2
    p2 = L - p1
    genes = [0]*p1 + [1]*p2
    random.shuffle(genes)
    child = []
    parents = (parent1,parent2)
    for i in range(L):
        child.append(parents[genes[i]][i])
    return child
    """

def make_child_increment(parent1,parent2):
    pass

def evolve(target,population_size=100):
    def _fitness(test):
        return fitness(target,test) 
    population = initial_population(target,population_size)
    population = sorted(population,key=_fitness)
    gen = 1
    mutation_rate = .5
    best = population[0]
    clear_out()
    i = 0
    write_improvement(best,i)
    f = _fitness(best)
    lf = f
    while f > 0:
        print("Gen:",gen,"Fitness:",f)
        population = breed(population,_fitness,mutation_rate)
        best = population[0]
        gen += 1
        lf = f
        f = _fitness(best)
        if lf > f:
            i += 1
            write_improvement(best,i)
    print("Gen:",gen,"Fitness:",f)
    return best,gen

print(evolve(load_target(argv[1]),20))
