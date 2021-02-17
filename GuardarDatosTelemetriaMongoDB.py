
import time
from paho.mqtt import client as mqtt_client
import pymongo
#datos conexion mqtt

broker = 'mqttdashboard.com'
port = 1883
topic = "/44550153g/moduloD2"
client_id = 'david'
#datos conexion MongoDB , base de datos y colección

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["Usal"]
mycol = mydb["medidas"]
datos = []
#funcion conectar al broker
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

#funcion de suscripcion al topic y descarga de datos a tiempo real

def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        print('------------------------------')
        lecturas ={'temperatura' : msg.payload.decode(), "topic" :msg.topic,  "fecha": time.strftime("%b-%d-%Y"), "hora" :time.strftime("%H:%M:%S")}
        print(lecturas)
        #insercion de los datos del array en la colecion especificada al principio.
        x= mycol.insert_one(lecturas)
        
    client.subscribe(topic)
    client.on_message = on_message
#funcion de ejecución de funciones anteriores en un bucle infinito  

def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

if __name__ == '__main__':
    run()