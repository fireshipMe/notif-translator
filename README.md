# Notification translator

Translates anything you highlight and shows translate in bubble notification!

# Basic usage

1. Download both notificator.py and pyxhook.py files.
2. In terminal :
   > python notification.py 
3. Highlight text anywhere and press button 5 ( on a little square keyboard with nums a.k.a numpad )
4. :grey_question::grey_question::grey_question:
5. If you are using Ubuntu 14.04 ( as i do ) you will see little nice bubble with translated text
   ( from English to Russian by default)
 I haven't tested this script on another OS's(:clap:), and will never do. But you may.

# How to run script in a background

1. Make script executable:
   > chmod +x notificator.py
2. Use nohup linux command!
   > nohup /path/to/notificator.py & 
   ( And dont forget about **&** )
3. It will be nice idea to add nohup to autorun.

# Changing translation languages.

 Change translate() function parameter langPair='FROM-TO' to any lang you want.
 I've used Yandex.Translator API, so [here](https://tech.yandex.com/translate/doc/dg/concepts/api-overview-docpage/) you can find all supported languages.
 
# And, just in case
  If my API key will be blocked for any reason, [here](https://tech.yandex.com/keys/get/?service=trnsl) you can get a new key, then insert it insted of my ( notificator.py, 28 line )
