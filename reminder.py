# -*- coding: UTF-8 -*-
from time import *
from wxpy import *
from json import *

bot=Bot(console_qr=True, logout_callback=None)

def checkTime():
    if localtime(time()).tm_min == 0:
        remind()

def remind():
    with open('config.json', 'r') as config_file:
        config = load(config_file)
#       print(imgs)
#       print(groups)
        for i in range(0,len(config['groups'])):
            names=config['groups'][i]['names']
            messages=config['groups'][i]['messages']
            images=config['groups'][i]['images']
            current_groups=[]
            #search for groups
            for j in range(0,len(names)):
                current_groups.append(ensure_one(bot.groups().search(names[j])))
#                current_groups.append(config['groups'][i]['names'][j])
            #send messages
            for j in range(0,len(current_groups)):
                for k in range(0,len(messages)):
#                    print(current_groups[j],' messages:',messages[k])
                    current_groups[i].send(messages[k])
                for l in range(0,len(images)):
#                    print(current_groups[j],' images:',images[k])
                    current_groups[i].send_image(images[k])
        config_file.close()

if __name__ == "__main__":  
    while(True):
        checkTime()
        sleep(60)