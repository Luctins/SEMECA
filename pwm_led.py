from machine import Pin, PWM
from time import sleep
import network
from umqtt.simple import MQTTClient



def msg_callback(topic, msg):
    print(topic, msg)
    #msg = str(msg)
    t=msg.decode('utf-8') #convertendo a mensagem em byte para string
    
    if topic == b'semeca/leds':
        frequency = 5000
        led = PWM(Pin(5), frequency)
        pwm = int(msg)
        
        led.duty(pwm)
        c.publish(topic='semeca/led/intensidade', msg=msg)




sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect('SEMECA-IOT', 'mecatronica') #Conexão WIFI
print('Tentando conexao...')
while not sta_if.isconnected(): #Verifica莽茫o da conex茫o
    pass
print('Conectado!')

c = MQTTClient("Ledzinhos", '192.168.0.33',  port=1883) #broker
c.connect()
c.publish(topic='Conexao',msg=b"ESP8266 Conectada!")
c.publish(topic='Conexao',msg=b"Conexao OK")

c.set_callback(msg_callback)
c.subscribe('semeca/leds')
while True:
    c.wait_msg()
