import ssl
import sys
import pandas as pd
import time
import paho.mqtt.client
broker = 'mqttdashboard.com'
port = 1883
topic = "/44550153g/taller2"
client_id = 'david'
 
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Conectado a HiveMQ!")
    else:
        print("Failed to connect, return code %d\n", rc)
 
def on_message(client, userdata, message):
    print('------------------------------')
    print(f'topic: {message.topic}')
    print(f'Temperatura Raspberry:  {message.payload.decode()}')
    print (time.strftime("%c"))
    print(message.payload)
    datos = message.topic 
    return(datos)
    #print('qos: %d' % message.qos)
 
def main():
    client = paho.mqtt.client.Client(client_id='david', clean_session=False)
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(host='mqttdashboard.com', port=1883)
    client.loop_forever()
 
if __name__ == '__main__':
    main()
print(on_message)

"""
df = pd.DataFrame({})
print(df)
df.to_csv('mqtt.csv', index=False)
"""
sys.exit(0)