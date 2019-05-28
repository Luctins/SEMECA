from random import randint
import paho.mqtt.client as paho
import time

client = paho.Client('Temperatura')
client.connect("192.168.0.33",1883,60)
client.loop_start()

while True:
    msg = randint(10,36) #Gerador de numeros aleatorios
    client.publish('semeca/temperatura3', str(msg - 7))
    time.sleep(0.05)
    client.publish('semeca/temperatura', str(msg))
    client.publish('semeca/temperatura2', str(msg + 0.4))
    time.sleep(1.5)
    client.publish('semeca/temperatura3', str(msg - 2))
    print(str(msg))

    time.sleep(2.5)
