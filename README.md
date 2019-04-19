# telegram-username-grabber

telegram cli app based on telethon python library. it's listening to special username that is already taken by another person to be released and immediately set it on your own telegram account.


# usage

first install telethon and requests

```
  pip3 install telethon
  pip install requests
```  
  
then get your own api_id and api_hash from [telegram](https://my.telegram.org) and put them in the source code.
now run the script it will ask you for target username , your phone number and retriving code from telegram to confirm login.
