training_list = [
    [1,2,3,4,5,6,7,8,9,10,11,12,13,'<50k'],
    [1,2,3,4,5,6,7,8,9,10,11,12,13,'<50k'],
    [1,2,3,4,5,6,7,8,9,10,11,12,13,'>50k'],
    [1,2,3,4,5,6,7,8,9,10,11,12,13,'>50k'],
    [1,2,3,4,5,6,7,8,9,10,11,12,13,'<50k'],
    [1,2,3,4,5,6,7,8,9,10,11,12,13,'>50k']
]

over_50k = []
under_50k = []
for row in training_list:
    if row[-1] == "<50k":
        under_50k.append(row[:-1])
    elif row[-1] == ">50k":
        over_50k.append(row[:-1])

print "training_list"
for itr in training_list:
    print itr
print
print "over 50k list"
for itr in over_50k:
    print itr
print
print "under 50k list"
for itr in under_50k:
    print itr
print


over_50k_sum = [i for i in over_50k[0]]  # initialize with the first one
for i in range(1,len(over_50k)):         # skips the first one
    for j in range(len(over_50k[i])):
        over_50k_sum[j] += over_50k[i][j]

under_50k_sum = [i for i in under_50k[0]]  # initialize with the first one
for i in range(1,len(under_50k)):          # skips the first one
    for j in range(len(under_50k[i])):
        under_50k_sum[j] += under_50k[i][j]


print "over 50k sum"
print over_50k_sum
print
print "under 50k sum"
print under_50k_sum

