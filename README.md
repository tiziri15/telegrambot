#  Telegramebot 

In this project we created a telegram bot for automatic replies.
### To run this bot
----
1. First of all you must have a telegram account then search for the official account of @Botfather then clic on "start".
You will be receiving a couple of commandes that you can use, including our important command which is `/newbot`.
Please send this last command to create a new telegram bot, then it asks for the bot name `(GTR)` and username `(GTRRo-bot)`.
After following these steps you will receive the message which conains the secret API Key which is the secret link to log in the bot.
----
2. After this we pass to coding with python:
  We make (3) scripts 
  #### key.py
   + In this script we save our API-key link to use it later in the other scripts.
  ####  response.py
   + This scripte contains all the messages that can be sent to our bot and all replies to send back by the bot.
  #### main.py
   + In this script we have impoted our two first scripts and we have defined some litte functions which generate some help messages to guide the user.
   + Then we create the last function named by "main" where we call the function defined befor and use an updater polling to get the messages simultaneously.
----
  3. Finally let's enjoy texting our Telegram bot by searching for @GTRRo-bot
----

Realized by : 

- TAMANI Tiziri (tamanitiziri@gmail.com)
- TERRACHET Katia (katiaterrachet@gmail.com)
