import random

games = [
    "TDM",
    "Demo",
#    "Hardcore",
    "S&D",
#    "FFA",
    "HQ",
    "CTF",
    "Sabo",
    "Dom",
]



maps = [
"Afghan",
"Derail",
"Estate",
"Favela",
"Highrise",
"Invasion",
"Karachi",
"Quarry",
"Rundown",
"Rust",
"Scrapyard",
"Skidrow",
"Sub Base",
"Terminal",
"Underpass",
#"Wasteland"
]


random.shuffle(maps)
print(maps[0])

def random_teams(players):
    random.shuffle(players)
    return players[:4]

def random_map():
    return random.choice(maps)

def random_game():
    return random.choice(games)


print(random_game())

random.shuffle(maps)
random.shuffle(games)
m,M = 0,len(maps)
g,G = 0,len(games)
r = 0
for r in range(7):
    print('BEGINGAME 02/16/2018')
    print('TEAMS: Joe Eric, James Geoff')
    while g < G:
        print(games[g],maps[m],"|")
        g += 1
        m += 1
        if m == M:
            random.shuffle(maps)
            m = 0
    print('ENDGAME')
    g = 0
    random.shuffle(games)




"""
game1 = list((i,j) for i,j in zip(games,maps))
random.shuffle(maps)
random.shuffle(games)
game2 = list((i,j) for i,j in zip(games,maps))
random.shuffle(maps)
random.shuffle(games)
game3 = list((i,j) for i,j in zip(games,maps))

for i in game1:
    print(i)
print('')
for i in game2:
    print(i)
print('')
for i in game3:
    print(i)
print('')




players = ["drew","jax","james","geoff","joe"]
t1 = ['james', 'geoff', 'joe']
t2 = ['drew', 'dish', 'jax']
t1 = random_teams(t1)
t2 = random_teams(t2)
teams = [(i,j) for i,j in zip(t1,t2)]

print(random_teams(teams))
print(random_map())
print(random_game())
"""
