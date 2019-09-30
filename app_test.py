import os,sys
from flask import Flask,request
from pymessenger import  Bot
from wit import Wit
from post import *
acess_token="2P5AWUHZ3R55RZOQXB45FHH5OA6BU6VE"
page_acess_token="EAANOjUZBozU8BAKHeDNKJHaNqnBqnjyktGn7LTSQ1CaREL6ipqSqfoRFre4eGJ9VBrIZBsZBYAZBGejUYjqREM45xRvzJlCzbAV7YsLzZBR2zy3ftsEtGYZCGpg4otO9lZC5ITBmmzbpA3yKpagkRxZBTacxNHP3lRAdiWawxke2ud2Q8EJEFJlf0LCDmeUnt0EZD"
client=Wit(access_token=acess_token)
bot=Bot(page_acess_token)
app=Flask(__name__)
@app.route('/',methods=['GET'])
def verify():
	# Webhook verification
    if request.args.get("hub.mode") == "subscribe" and request.args.get("hub.challenge"):
        if not request.args.get("hub.verify_token") == "Shiva":
            return "Verification token mismatch", 403
        return request.args["hub.challenge"], 200
    return "Hello World",200
@app.route('/',methods=['POST'])
def  webhook():
 data = request.get_json()
 log(data)
 if data['object']=='page':
    for a in data['entry']:#toscanthroughmessageJson
       for b in a['messaging']:
          sender_id=b['sender']['id']#togetsenderid
          reciever_id=b['recipient']['id']#togetrecieverid
          if b.get('message'):
              if 'text' in b['message']:
                   test_text=b['message']['text']
                   my_text=test_text
                   resp=client.message(my_text)#storing client message in a varaible
                   entity=None# get entity#in case entity is none
                   value=None
                   intent=None#in case value is none
                   print(test_text)
                   try:
                       entity=list(resp['entities'])[0]# get entity
                       value=resp['entities'][entity][0]['value']# to get value of 
                       intent=resp['entities'][list(resp['entities'])[1]][0]['value']#to get value of intent
                   except:
                      pass
                   response=None
                   #print(entity)
                   print(value)
                   #print(intent)
                   if value=="Job_Search":
                       post.reply()    
                   if entity=='post':
                      v_text="Which Location do you want"
                      bot.send_text_message(sender_id,v_text)
                   if entity=='place':
                     m_text="Are you Sure you want to proceed"
                     bot.send_text_message(sender_id,m_text)
                   if  entity==None:
                      z_text="Sorry I dont Understand"
                      bot.send_text_message(sender_id,z_text)
                   if (test_text=="Yes") or (test_text=="YES"):
                      y_text="Hello jedi"
                      bot.send_text_message(sender_id,y_text)
                   elif (test_text=="No") or (test_text=="NO"):
                      t_text="Hello luke"
                      bot.send_text_message(sender_id,t_text)
              else:
                  test_text="no text"
                  response=test_text
                  bot.send_text_message(sender_id,test_text)
                   
              
 return "ok", 200
def log(message):
    print(message)
    sys.stdout.flush()
 
if __name__ == "__main__":
 app.run(debug = True,port=80)
    
