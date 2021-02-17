import time
from paho.mqtt import client as mqtt_client
import pymongo
import itertools

broker = 'mqttdashboard.com'
port = 1883
topic = "/44550153g/taller2"
client_id = 'david'

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Usal"]
mycol = mydb["Lecturas"]

def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Conectado a HiveMQ!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client
datos = []
diccionario = []
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print('------------------------------')
        lecturas =(f'temperatura {msg.payload.decode()} topic {msg.topic} fecha {time.strftime("%b-%d-%Y")} hora {time.strftime("%H:%M:%S")}')
        #print(lecturas)
        datos.append(lecturas)
        mylistIterable = iter(datos)
        mylistObjeto = itertools.zip_longest(mylistIterable, mylistIterable, fillvalue=None)
        mylistDict = dict(mylistObjeto)
        print(mylistDict)
        print(type(mylistDict))
        diccionario.append(mylistDict)
        print(diccionario)
        print(type(diccionario))

        """
        x= mycol.insert_many(mylist)
        print(x.inserted_ids)
        """
    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()