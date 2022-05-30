from datetime import datetime
def sample_response(input_text):
    user_message =str(input_text).lower()

    if user_message in ("hello", "hi","good morning","hey", "hi you",):
        return "hey! how are you?"
    if user_message in ("Salut", "coucou",):
        return "Salut! vous allez bien?"  
    if user_message in ("iam fine","nice", "fine", "good",):
        return "I'm glad to hear that from you"
    if user_message in ("and you? how are you?", "what about you?",):
        return "when i talk to you i am always happy"
    if user_message in ("my name?",):
        return "TERRACHET Katia"
    if user_message in ("what is the name of my partner?", ):
        return "TAMANI Tiziri"
    if user_message in ("what's your name?","do you have a name?"):
        return "my name is GTR"
    if user_message in ("good bye"):
        return "byeeee!!!"
    if user_message in ("time?","time","what time is it?",):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")
        return str(date_time)
    return "Sorry, I don't understand you."
