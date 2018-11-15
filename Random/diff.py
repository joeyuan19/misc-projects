from sys import argv
l1 = []
l2 = []

fname1 = argv[1]
fname2 = argv[2]

with open(argv[1],'r') as f1:
    l1 = [i for i in f1]

with open(argv[2],'r') as f2:
    l2 = [i for i in f2]

for i in range(0,len(l1)-len(l2)):
    l2.append('-\n')

for i in range(0,len(l2)-len(l1)):
    l1.append('-\n')

line = 1
for a,b in zip(l1,l2):
    if not a == b:
        print('line',line,'['+fname1+']',a)
        print('line',line,'['+fname2+']',b)
    line += 1

