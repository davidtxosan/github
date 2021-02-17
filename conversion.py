
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
diccionario = {}
def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print('------------------------------')
        lecturas =(f'temperatura {msg.payload.decode()} topic {msg.topic} fecha {time.strftime("%b-%d-%Y")} hora {time.strftime("%H:%M:%S")}')
        print(lecturas)
        print(type(lecturas))# tipo str
    
        datosSplit = lecturas.strip('][').split(' ')
        print(datosSplit)
        print(type(datosSplit))#tipo list con cada elemento como un str

        datos.append(datosSplit)#tipo list añadiendo las listas en cada iteracion
        print(datos)
        print(type(datos))
        """
        for line in datosSplit:
            valores=line.split(" ",1)
            diccionario[valores[0].strip()]=(valores[1].strip()
        for k,v in diccionario.items():
            print(f"Clave:{k}valor:{v}")
        """
    client.subscribe(topic)
    client.on_message = on_message

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()