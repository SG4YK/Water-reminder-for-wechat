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
        imgs = config['pics']
        groups = config['groups']
#       print(imgs)
#       print(groups)
        for i in range(0,len(groups)):
            groups[i] = ensure_one(bot.groups().search(groups[i]))
            for j in range(0,len(imgs)):
                groups[i].send_image(imgs[i])


if __name__ == "__main__":  
    while(True):
        checkTime()
        sleep(60)
