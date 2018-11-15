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
    with open('out/dimensions.txt','w') as f:
        f.write("WIDTH  : "+str(image.width)+"\n")
        f.write("HEIGHT : "+str(image.height))
        print("WIDTH  : "+str(image.width))
        print("HEIGHT : "+str(image.height))
    del(im)
    image.close()
    return pixdata

def fitness(target,test):
    return sum(abs(target_i-test_i) for target_i,test_i in zip(target,test))

def randpix():
    return random.randint(0,255)

def randinit(N):
    return [randpix() for i in range(N)]

def breed(guess,_fitness,f):
    L = len(guess)
    f = _fitness(guess)
    for i in range(L):
        _guess = [j for j in guess]
        _guess[i] = randpix()
        _f = _fitness(_guess)
        if _f < f:
            f = _f
            guess = _guess
    return guess,f 

def breed_increment(guess,_fitness,f):
    min_guess = [i for i in guess]
    min_f = f 
    for p in range(5):
        _guess = []
        for i,pix in enumerate(guess):
            _guess.append((pix + random.choice([-1,1]))%255)
        if _fitness(_guess) < min_f:
            min_f = f
            min_guess = [i for i in _guess]
    return min_guess, min_f 

def evolve(target):
    def _fitness(test):
        return fitness(target,test) 
    guess = randinit(len(target))
    gen = 1
    clear_out()
    i = 0
    write_improvement(guess,i)
    f = _fitness(guess)
    lf = f
    while f > 0:
        print("Gen:",gen,"Fitness:",f)
        lf = f
        guess,f = breed_increment(guess,_fitness,f)
        gen += 1
        if lf > f:
            i += 1
            write_improvement(guess,i)
    print("Gen:",gen,"Fitness:",f)
    return guess,gen

print(evolve(load_target(argv[1])))
