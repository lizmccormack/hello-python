# 1 crate an empty dictionary
soccor_team = {}

# 2 add a key value pair for team name
soccor_team['team_name'] = 'lazy_lizards'

# 3 add a key value pair for team ranking
soccor_team['team_ranking'] = 1

# 4 add a key value pair for a list of player names
soccor_team['player_names'] = ['ilanna', 'liv', 'liz']

# 5 increase the team ranking by 1 :(
soccor_team['team_ranking'] += 1

# 6 add a new player to the team DAVID BECKHAM
soccor_team['player_names'].append('David Beckham')
print (soccor_team)

# 7 conditional if statement based on team ranking
if soccor_team['team_ranking'] <= 3:
    print('Hooray!')
elif 3 < soccor_team['team_ranking'] < 12:
    print ('Better luck next time')
else:
    print ('That\'s not a ranking!')

# 8 for loop to print all player names
for player in soccor_team['player_names']:
    print (player)

# 9 look for the key team color in the dictionary
if 'team_color' in soccor_team:
    print (soccor_team['team_color'])
else:
    print ('The team is colorless!')

# 10 since it's not there add a team color and try the for loop to look for key
soccor_team['team_color'] = 'Chartruse'

if 'team_color' in soccor_team:
    print (soccor_team['team_color'])
else:
    print ('The team is colorless!')

# 11 print all key value pairs in the dictionary soccor_team 
for team_attribute in soccor_team:
    print (team_attribute,",", soccor_team[team_attribute])
