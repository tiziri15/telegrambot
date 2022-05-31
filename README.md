#  Telegramebot 

In this project we create a telegram bot which can send and replay for messages that we need to in telegram. 
### To run this bot
   ```
1. we must have a telegram account then found the officiel account of @Botfather then we clic on "start"
   + we have a long message of commandes that we can send to botfather betwween them we find "/newbot"; 
   + we send that as request to create a new telegram bot;
   + then he ask for the bot name (GTR) and username GTRRo-bot) ;
   + after folowing this steps we will get message that contain the secret API Key which is the secret link to log in the bot.

2. After this we pass to coding with python:
  We make (3) scripts 
  #### key.py
      In this script we saved our API-key link use ot later in the other scripts.
  ####  response.py
      this scripte containe all the messages that can be sended to our bot and the responses that we want to replay to.
  #### main.py
      In this scripte we have impoterd ou two first scripts and we defined some litte function which generate somme help messages to show to the user how to use the bot
  in order not to get stucked in the error message.
  then we create the last function named by "main" where we all the function defined befor and used an updater polling to get the messages simultaneously.
  
  3.In the end we go to test our telegram bot, then to start we search for @GTRRo-bot then we start send messages.
   ```

Realized by : 

- TAMANI Tiziri (tamanitiziri@gmail.com)
- TERRACHET Katia (katiaterrachet@gmail.com)



