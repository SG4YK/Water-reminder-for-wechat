# Just a simple water reminder for WeChat.
Inspired by [this image](https://github.com/SG4YK/Water-reminder-for-wechat/blob/master/img/reminder.jpg)
## Dependencies
+ python  
+ pillow
+ pip
+ [wxpy](https://github.com/youfou/wxpy)  
## Usage
Install dependencies
```
$ pip install wxpy
$ pip install pillow
```
Clone this repo
```
$ git clone https://github.com/SG4YK/Water-reminder-for-wechat.git
$ cd Water-reminder-for-wechat
```
Edit `config.json`, make sure the file name and the group names are exact. Here's the example
```
{
    "groups": [
        {
            "names": ["gp00","gp01"],
            "messages": ["msg00"],
            "images" :["./img/reminder.jpg","./img/alternative/1.png"]
        },
        {
            "names": ["gp10"],
            "messages": ["messages10"],
            "images": ["./img/alternative/2.png"]
        }
    ],
    "friends": [
        {
            "names": [],
            "messages": [],
            "images" :[]
        }
    ]
}
```
Run the script, and scan the QR code using WeChat on iOS or Android.  
```
$ python reminder.py
```
To run in the script in the background, you can use [screen](https://www.gnu.org/software/screen/)   
```
$ screen -S reminder  
$ python reminder.py
```
Then you can end your terminal process, but don't use Ctrl+D to quit.  
Using `screen -R reminder` to reattach to the session.