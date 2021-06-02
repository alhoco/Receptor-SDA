# Receptor module: 
# Irene Abad Londoño & Alejandro Hoyos Correa


import paho.mqtt.client as mqtt
import json

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("sda/sensorIA")

def on_message(client, userdata, msg): 
    messageencoded = msg.payload
    messagedecoded = messageencoded.decode()
    message_dict = json.loads(messagedecoded)

    for key, value in message_dict.items():
        print(f"{key}, {value}")
    
    with open('Database.txt', 'a+') as f: 
        f.write('Power: '+str(message_dict))
        f.write('\n')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)


client.loop_forever()