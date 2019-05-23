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
        for i in range(0,len(config['groups'])):
            current_groups=[]
            for j in range(0,len(config['groups'][i]['names'])):
                current_groups.append(ensure_one(bot.groups().search(config['groups'][i]['names'][j])))
            for j in range(0,len(current_groups)):
                for k in range(0,len(config['groups'][i]['messages'])):
                    current_groups[i].send(config['groups'][i]['messages'][k])
                for l in range(0,len(config['groups'][i]['images'])):
                    current_groups[i].send_image(config['groups'][i]['images'][k])
        config_file.close()

if __name__ == "__main__":  
    while(True):
        checkTime()
        sleep(60)
