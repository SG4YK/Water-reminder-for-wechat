# Just a simple water reminder for WeChat.

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
    "groups": ["group1","group2"], 
    "friends": [], 
    "pics": ["./img/reminder.jpg"],
    "messages": []
}
```
Run the script, and scan the QR code using WeChat on iOS or Android.  
```
$ python reminder.py
```
To run in the script as a deamon, you can use [screen](https://www.gnu.org/software/screen/)   
```
$ screen -S reminder  
$ python reminder.py
```
Then you can end your terminal process, but don't use Ctrl+D to quit.  
Using `screen -R reminder` to reattach to the session.