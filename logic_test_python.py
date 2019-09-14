#=============================================#
# deeper systems python challenge
# @ claudio
#=============================================#

#=========================#
# loading
#=========================#

# import packages
import json
import time 
from datetime import datetime

# import data
with open('U1ZQR43RB.json') as json_data:
    data = json.load(json_data)

# create data user 
users = {}
for i in range(len(data)):
    user = data[i]['user']
    users[user] = {}

#===================================================# 
# indetify timestamp 2 min between and group text
#==================================================#

keyts = float(data[0]['ts'])
listext = []
for i in range(len(data)):
    if i+1 >= len(data):
        break
    # eval 2 min
    difloat = float(data[i+1]['ts']) - float(data[i]['ts']) 
    difdate = datetime.fromtimestamp(difloat)
    difsec = time.mktime(difdate.timetuple())
    if difsec < 120:
        listext.append(data[i+1]['text'])
        dic = {keyts: listext}
        users[data[i+1]['user']].update(dic)
    # create other group
    else:
        keyts = float(data[i+1]['ts'])
        listext = []

# save data in json
with open('grouped_data.json', 'w') as fp:
    json.dump(users, fp)

