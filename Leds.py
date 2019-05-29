"""
Led 0 - Amarelo
Led 1 - Azul
Led 2 - Verde
Led 3 - Vermelho
"""


import network
import machine
from umqtt.simple import MQTTClient
import utime
import time



led=machine.Pin(13,machine.Pin.OUT)#semeca/led2
led1=machine.Pin(12,machine.Pin.OUT)#semeca/led1
led2=machine.Pin(15,machine.Pin.OUT)#semeca/led3
led3=machine.Pin(14,machine.Pin.OUT)#semeca/led4

def msg_callback(topic, msg):

    print(topic, msg)
 
    t=msg.decode('utf-8') #convertendo a mensagem em byte para string
    print(t)
  


    if topic == b'semeca/led1':


        if t== '1':
            print('Digitou 1')
            c.publish(topic='semeca/led1',msg=b"Ligado")
            led1.value(1)
        elif t=='0':
            print("Digitou 0")
            c.publish(topic='semeca/led1',msg=b"Desligado")
            led1.value(0)
        else:
            print('ops')

    if topic == b'semeca/led3':
        if t== '1':
            print('Digitou 1')
            c.publish(topic='semeca/led3',msg=b"Ligado")
            led2.value(1)
        elif t=='0':
            print("Digitou 0")
            c.publish(topic='semeca/led3',msg=b"Desligado")
            led2.value(0)
        else:
            print('ops')

    if topic == b'semeca/led4':
        if t== '1':
            print('Digitou 1')
            c.publish(topic='semeca/led4',msg=b"Ligado")
            led3.value(1)
        elif t=='0':
            print("Digitou 0")
            led3.value(0)
            c.publish(topic='semeca/led4',msg=b"Desligado")
        else:
            print('ops')

    if topic == b'semeca/led2':


        if t== '1':
            print('Digitou 1')
            c.publish(topic='semeca/led2',msg=b"Ligado")
            led.value(1)
        elif t=='0':
            print("Digitou 0")
            c.publish(topic='semeca/led2',msg=b"Desligado")
            led.value(0)
        else:
            print('ops')
            #c.publish(topic='faixa',msg="Ops")


sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('SEMECA-IOT', 'mecatronica') #Conexão WIFI
print('Tentando conexão...')
while not sta_if.isconnected(): #Verificação da conexão
    pass
print('Conectado!')

c = MQTTClient("Ledzinhos", '192.168.0.33',  port=1883) #broker
c.connect()
c.publish(topic='Conexao',msg=b"ESP8266 Conectada!")
c.publish(topic='Conexao',msg=b"Conexao OK")

c.set_callback(msg_callback)
c.subscribe('semeca/led1')
c.subscribe('semeca/led2')
c.subscribe('semeca/led3')
c.subscribe('semeca/led4')

while True:
    c.wait_msg()
    








