from random import randint
import paho.mqtt.client as paho
import time

client = paho.Client('Agua')
client.connect("192.168.0.33",1883,60)
client.loop_start()

while True:
    for msg in range(1000,10000): #Gerador de numeros aleatorios
        client.publish('semeca/agua', str(msg))
        print(msg)
        time.sleep(0.05)
