import datetime

SIG_FIGS = 2

class Player(object):
    def __init__(self,name):
        self.name = name
        self.games = []
        self.matches = []
        self.match_win = []
        self.match_loss = []
        self.game_win = []
        self.game_loss = []
        self.game_stats = []
        
    def add_match(self,match):
        self.matches.append(match)
        if self in match.winner:
            self.match_win.append(match)
        else:
            self.match_loss.append(match)

    def add_game(self,game):
        self.games.append(game)
        if self in game.winner:
            self.game_win.append(game)
        else:
            self.game_loss.append(game)
        for match in game:
            self.add_match(match)

    def add_game_stat(self,stat):
        self.game_stats.append(stat)

    def stats(self):
        min_level,max_level,min_mode,max_mode = self.get_game_stats()
        worst_teammate_match,best_teammate_match,worst_teammate_game,best_teammate_game = self.get_teammate_stats()
        kill,assist,death = 0,0,0
        for stat in self.game_stats:
            k,a,d,m = stat
            kill    += k
            assist  += a
            death   += d
        m_win = len(self.match_win)
        m_loss = len(self.match_loss)
        m_total = len(self.matches)
        g_win = len(self.game_win)
        g_loss = len(self.game_loss)
        g_total = len(self.games)
        print(self.game_stats)
        return {
            'match' : {
                'order':['wins','losses','win/loss ratio','kill','death','assist','kd','kill/match','best level','worst level','best game mode','worst game mode','best teammate','worst teammate'],
                'wins':str(m_win) + ' (' + str(round(m_win/m_total*100,SIG_FIGS)) + '%)',
                'losses':str(m_loss) + ' (' + str(round(m_loss/m_total*100,SIG_FIGS)) + '%)',
                'win/loss ratio':round(m_win/m_loss,SIG_FIGS) if m_loss != 0 else 'inf',
                'kill':kill,
                'death':death,
                'assist':assist,
                'kd':kill/death if death != 0 else 'inf',
                'kill/match':kill/len(self.game_stats) if len(self.game_stats) != 0 else 'inf',
                'best level':max_level,
                'worst level':min_level,
                'best game mode':max_mode,
                'worst game mode':min_mode,
                'best teammate':best_teammate_match,
                'worst teammate':worst_teammate_match,
            },
            'series' : {
                'order':['wins','losses','best teammate','worst teammate'],
                'wins':str(g_win) + ' (' + str(round(g_win/g_total*100,SIG_FIGS)) + '%)',
                'losses':str(g_loss) + ' (' + str(round(g_loss/g_total*100,SIG_FIGS)) + '%)',
                'win/loss ratio':round(g_win/g_loss,SIG_FIGS) if g_loss != 0 else 'inf',
                'best teammate':best_teammate_game,
                'worst teammate':worst_teammate_game,
            }
        }

    def get_game_stats(self):
        levels = {}
        modes = {}
        for match in self.match_win:
            if match.level in levels:
                levels[match.level] += 1
            else:
                levels[match.level] = 1
            if match.mode in modes:
                modes[match.mode] += 1
            else:
                modes[match.mode] = 1
        for match in self.match_loss:
            if match.level in levels:
                levels[match.level] -= 1
            else:
                levels[match.level] = -1
            if match.mode in modes:
                modes[match.mode] -= 1
            else:
                modes[match.mode] = -1
        levels = sorted(levels.items(),key=lambda x: x[1])
        min_level_score = levels[0][1]
        min_level = tuple(level for level in levels if level[1] == min_level_score)
        max_level_score = levels[-1][1]
        max_level = tuple(level for level in levels if level[1] == max_level_score)
        modes = sorted(modes.items(),key=lambda x: x[1])
        min_mode_score = modes[0][1]
        min_mode = tuple(mode for mode in modes if mode[1] == min_mode_score)
        max_mode_score = modes[-1][1]
        max_mode = tuple(mode for mode in modes if mode[1] == max_mode_score)
        return ', '.join(t[0] +' (' + str(t[1]) + ')' for t in min_level),\
            ', '.join(t[0] +' (' + str(t[1]) + ')' for t in max_level),\
            ', '.join(t[0] +' (' + str(t[1]) + ')' for t in min_mode),\
            ', '.join(t[0] +' (' + str(t[1]) + ')' for t in max_mode)

    def get_teammate_stats(self):
        teammates_match = {}
        for match in self.match_win:
            for player in match.winner:
                if player != self:
                    if player not in teammates_match:
                        teammates_match[player] = 1
                    else:
                        teammates_match[player] += 1
        for match in self.match_loss:
            for team in match.teams:
                if self in team:
                    for player in team:
                        if player != self:
                            if player not in teammates_match:
                                teammates_match[player] = -1
                            else:
                                teammates_match[player] += -1
        teammates_match = sorted(teammates_match.items(),key=lambda x:x[1])
        min_match_teammate_score = teammates_match[0][1]
        min_match_teammate = tuple(teammate for teammate in teammates_match if teammate[1] == min_match_teammate_score)
        max_match_teammate_score = teammates_match[-1][1]
        max_match_teammate = tuple(teammate for teammate in teammates_match if teammate[1] == max_match_teammate_score)
        teammates_game = {}
        for game in self.game_win:
            for player in game.winner:
                if player != self:
                    if player not in teammates_game:
                        teammates_game[player] = 1
                    else:
                        teammates_game[player] += 1
        for game in self.game_loss:
            for team in game.teams:
                if self in team:
                    for player in team:
                        if player != self:
                            if player not in teammates_game:
                                teammates_game[player] = -1
                            else:
                                teammates_game[player] += -1
        teammates_game = sorted(teammates_game.items(),key=lambda x:x[1])
        min_game_teammate_score = teammates_game[0][1]
        min_game_teammate = tuple(teammate for teammate in teammates_game if teammate[1] == min_game_teammate_score)
        max_game_teammate_score = teammates_game[-1][1]
        max_game_teammate = tuple(teammate for teammate in teammates_game if teammate[1] == max_game_teammate_score)
        return ', '.join(t[0].name +' (' + str(t[1]) + ')' for t in min_match_teammate),\
            ', '.join(t[0].name +' (' + str(t[1]) + ')' for t in max_match_teammate),\
            ', '.join(t[0].name +' (' + str(t[1]) + ')' for t in min_game_teammate),\
            ', '.join(t[0].name +' (' + str(t[1]) + ')' for t in max_game_teammate)
    
    def __hash__(self):
        return self.name.__hash__()

    def __eq__(self,other):
        return other.name == self.name

    def __lt__(self,other):
        return self.name < other.name

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<Player: ' + self.name + '>'

class Stat(object):
    def __init__(self,player,score,kills,assists,deaths):
        self.player = player
        self.score = score
        self.kills = kills
        self.assists = assists
        self.deaths = deaths

class Match(object):
    def __init__(self,level,mode,teams,winner):
        self.level = level
        self.mode = mode
        self.teams = tuple(team if isinstance(team,Team) else Team(team) for team in teams)
        self.winner = winner if isinstance(winner,Team) else Team(winner)
        self.loser  = tuple(team for team in self.teams if team != self.winner)[0]

    def __repr__(self):
        return '<Match '+self.mode +' on ' + self.level + ' Winner='+str(self.winner)+' Loser='+str(self.loser)+'>'

class Game(object):
    def __init__(self,matches,teams,date,winner,game_stats):
        self.matches = matches
        self.game_stats = game_stats
        self.teams = tuple(team if isinstance(team,Team) else Team(team) for team in teams)
        self.date = date
        self.winner = winner if isinstance(winner,Team) else Team(winner)

    def __iter__(self):
        for match in self.matches:
            yield match

    def __repr__(self):
        return '<Game: Teams=[' + ', '.join(str(t) for t in self.teams) + '] Winner=[' + str(self.winner)  + ']>'

class Team(object):
    def __init__(self,players):
        self.players = tuple(player if isinstance(player,Player) else Player(player) for player in players)
        self.games = []
        self.game_win = []
        self.game_loss = []
        self.matches = []
        self.match_win = []
        self.match_loss = []
        
    def add_match(self,match):
        self.matches.append(match)
        if self == match.winner:
            self.match_win.append(match)
        else:
            self.match_loss.append(match)

    def add_game(self,game):
        self.games.append(game)
        if self == game.winner:
            self.game_win.append(game)
        else:
            self.game_loss.append(game)
        for match in game:
            self.add_match(match)

    def stats(self):
        min_level,max_level,min_mode,max_mode = self.get_game_stats()
        m_win = len(self.match_win)
        m_loss = len(self.match_loss)
        m_total = len(self.matches)
        g_win = len(self.game_win)
        g_loss = len(self.game_loss)
        g_total = len(self.games)
        return {
            'match' : {
                'order' : ['wins','losses','win/loss ratio','best level','worst level','best game mode','worst game mode'],
                'wins' : str(m_win) + ' (' + str(round(m_win/m_total*100,SIG_FIGS)) + '%)',
                'losses' : str(m_loss) + ' (' + str(round(m_loss/m_total*100,SIG_FIGS)) + '%)',
                'win/loss ratio' : round(m_win/m_loss,SIG_FIGS) if m_loss != 0 else 'inf',
                'best level' : max_level,
                'worst level' : min_level,
                'best game mode' : max_mode,
                'worst game mode' : min_mode,
            },
            'series' : {
                'order':['wins','losses','win/loss ratio'],
                'wins':str(g_win) + ' (' + str(round(g_win/g_total*100,SIG_FIGS)) + '%)',
                'losses':str(g_loss) + ' (' + str(round(g_loss/g_total*100,SIG_FIGS)) + '%)',
                'win/loss ratio':round(g_win/g_loss,SIG_FIGS) if g_loss != 0 else 'inf',
            }
        }       
    
    def get_game_stats(self):
        levels = {}
        modes = {}
        for match in self.match_win:
            if match.level in levels:
                levels[match.level] += 1
            else:
                levels[match.level] = 1
            if match.mode in modes:
                modes[match.mode] += 1
            else:
                modes[match.mode] = 1
        for match in self.match_loss:
            if match.level in levels:
                levels[match.level] -= 1
            else:
                levels[match.level] = -1
            if match.mode in modes:
                modes[match.mode] -= 1
            else:
                modes[match.mode] = -1
        levels = sorted(levels.items(),key=lambda x:x[1])
        min_level_score = levels[0][1]
        min_level = tuple(level for level in levels if level[1] == min_level_score)
        max_level_score = levels[-1][1]
        max_level = tuple(level for level in levels if level[1] == max_level_score)
        modes = sorted(modes.items(),key=lambda x:x[1])
        min_mode_score = modes[0][1]
        min_mode = tuple(mode for mode in modes if mode[1] == min_mode_score)
        max_mode_score = modes[-1][1]
        max_mode = tuple(mode for mode in modes if mode[1] == max_mode_score)
        return ', '.join(t[0] +' (' + str(t[1]) + ')' for t in min_level),\
            ', '.join(t[0] +' (' + str(t[1]) + ')' for t in max_level),\
            ', '.join(t[0] +' (' + str(t[1]) + ')' for t in min_mode),\
            ', '.join(t[0] +' (' + str(t[1]) + ')' for t in max_mode)


    def mode_stats(self):
        modes = {}
        for match in self.match_win:
            if match.mode not in modes:
                modes[match.mode] = [1,0]
            else:
                modes[match.mode][0] += 1
        for match in self.match_loss:
            if match.mode not in modes:
                modes[match.mode] = [1,0]
            else:
                modes[match.mode][1] += 1
        return modes 

    def level_stats(self):
        levels = {}
        for match in self.match_win:
            if match.level not in levels:
                levels[match.level] = [1,0]
            else:
                levels[match.level][0] += 1
        for match in self.match_loss:
            if match.level not in levels:
                levels[match.level] = [1,0]
        return levels

    def __contains__(self,other):
        return other in self.players

    def __iter__(self):
        for player in self.players:
            yield player

    def __eq__(self,other):
        return sorted(self.players) == sorted(other.players)

    def __hash__(self):
        return self.players.__hash__()

    def __lt__(self,other):
        return self.players < other.players

    def __repr__(self):
        return '<TEAM: ('+', '.join(str(p) for p in self.players) + ')>'

def parse_game(game):
    game = game.strip()
    game = game.strip('BEGINGAME')
    game = game.strip('ENDGAME')
    game = game.strip()
    date = None
    matches = []
    game_stats = []
    for line in game.split('\n'):
        if date is None:
            date = datetime.datetime.strptime(line.strip(),'%m/%d/%Y')
        elif line.startswith('TEAMS:'):
            teams = line.strip('TEAMS:').strip().split(',')
            teams = list(tuple(sorted(team.strip().split(' '))) for team in teams)
        else:
            data = line.split('|')
            if len(data) > 2:
                type_level,players,game_stat = data
                game_stats.append({player:tuple(map(int,(k,a,d)))+(match,) for player,k,a,d in game_stat.strip().strip(')').strip('(').split(' ')})
            else:
                type_level,players = data
            matches.append((tuple(type_level.strip().split(' ')),tuple(sorted(players.strip().split(' ')))))
            if len(matches[-1][-1][0]) == 0:
                matches = matches[:-1]
    score = {team:0 for team in teams}
    for i,team in enumerate(teams):
        players = tuple(Player(player) for player in team)
        teams[i] = Team(players)
    for i,match in enumerate(matches):
        matches[i] = Match(match[0][1],match[0][0],teams,Team(match[1]))
        if len(match[1][0]) > 0:
            score[match[1]] += 1
        else:
            break
        for t,s in score.items():
            if s > 3:
                winner = Team(t)
                break
    game = Game(matches,teams,date,winner,game_stats)
    return game

import sys
if len(sys.argv) > 1:
    fname = sys.argv[1]
else:
    fname = 'game.txt'

with open(fname,'r') as f:
    games = []
    in_game = False
    for line in f:
        if in_game:
            game += line
        if line.startswith('BEGINGAME'):
            in_game = True
            game = line 
        elif line.startswith('ENDGAME'):
            in_game = False 
            games.append(parse_game(game))

players = []
teams = []
for game in games:
    for team in game.teams:
        if team not in teams:
            team.add_game(game)
            teams.append(team)
        else:
            teams[teams.index(team)].add_game(game)
        for player in team:
            if player not in players:
                player.add_game(game)
                players.append(player)
            else:
                players[players.index(player)].add_game(game)
    for game_stat in game.game_stats:
        for player,stats in match_stats.items():
            players[players.index(player)].add_match_stat(game)

for player in players:
    print(player.name)
    for stat_cat,stats in player.stats().items():
        print('\t',stat_cat)
        for stat_name in stats['order']:
            print('\t\t',stat_name,':',stats[stat_name])

for team in teams:
    print(team)
    for stat_cat,stats in team.stats().items():
        print('\t',stat_cat)
        for stat_name in stats['order']:
            print('\t\t',stat_name,':',stats[stat_name])

for team in teams:
    print(team,team.mode_stats())
for team in teams:
    print(team,team.level_stats())
