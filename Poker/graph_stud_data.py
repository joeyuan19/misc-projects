import matplotlib.pyplot as plt

with open('stud_data.txt','r') as f:
    rawdata = [tuple(conv(i) for conv,i in zip((int,int,int,int,float,float),line.split(','))) for line in f]

data = {}
for mode, players, rounds, player, win, dealer in rawdata:
    if mode not in data:
        data[mode] = {players:{player:[[rounds],[win]]}}
    else:
        if players not in data[mode]:
            data[mode][players] = {player:[[rounds],[win]]}
        else:
            if player not in data[mode][players]:
                data[mode][players][player] = [[rounds],[win]]
            else:
                data[mode][players][player][0].append(rounds)
                data[mode][players][player][1].append(win)

fig = plt.figure()
ax = []
M = len(data)
P = len(data[0])
i = 1
c = ['b','r','g','y','k']
for m in data:
    for p in data[m]:
        ax.append(fig.add_subplot(M,P,i))
        ax[-1].set_title("Mode = " + str(m) + " Players = " + str(p))
        ax[-1].set_xscale('log')
        for player,xy in data[m][p].items():
            ax[-1].plot(xy[0],xy[1],c[player]+'o')
        i += 1

fig2 = plt.figure()
ax2 = []
i = 1
for m in data:
    ax2.append(fig2.add_subplot(M,1,i))
    ax2[-1].set_title("Mode = " + str(m))
    for p in data[m]:
        for player,xy in data[m][p].items():
            idx = xy[0].index(10000)
            ax2[-1].plot(p,xy[1][idx],c[player]+'o')
    i += 1

fig3 = plt.figure()
ax3 = []
i = 1
for m in data:
    for p in data[m]:
        ax3.append(fig.add_subplot(M,P,i))
        ax3[-1].set_title("Mode = " + str(m) + " Players = " + str(p))
        for player,xy in data[m][p].items():
            idx = xy[0].index(10000)
            ax3[-1].plot(p,xy[1][idx],c[player]+'o',label='P'+str(player))
        i += 1
        ax3[-1].legend()

plt.show()




