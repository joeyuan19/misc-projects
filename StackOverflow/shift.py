seed = 1

messageList = ['derp']

def numtolist(n):
    seedstring = str(n)
    numlist = []
    for digit in seedstring:
        numlist.append(int(digit))
    return numlist

currentnumber = seed^2
newmessage = str()
for letter in messageList:
    numtolist(currentnumber)
    num1 = numlist[0]
