# 1
soccor_team = {}

# 2
soccor_team['team_name'] = 'lazy_lizards'

# 3
soccor_team['team_ranking'] = 1

# 4
soccor_team['player_names'] = ['ilanna', 'liv', 'liz']

# 5
soccor_team['team_ranking'] += 1

# 6
soccor_team['player_names'].append('David Beckham')
print (soccor_team)

# 7
if soccor_team['team_ranking'] <= 3:
    print('Hooray!')
elif 3 < soccor_team['team_ranking'] < 12:
    print ('Better luck next time')
else:
    print ('That\'s not a ranking!')

# 8
for player in soccor_team['player_names']:
    print (player)

# 9
if 'team_color' in soccor_team:
    print (soccor_team['team_color'])
else:
    print ('The team is colorless!')

# 10
soccor_team['team_color'] = 'Chartruse'

if 'team_color' in soccor_team:
    print (soccor_team['team_color'])
else:
    print ('The team is colorless!')
    
# 11
for team_attribute in soccor_team:
    print (team_attribute,",", soccor_team[team_attribute])
