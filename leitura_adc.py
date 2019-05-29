from machine import Pin, PWM
import time
import network
from umqtt.simple import MQTTClient
#Função para leitura do ADC através do pino D3 do NodeMCU
 
def readADC():
    adc = machine.ADC(0)
    var= adc.read()
    c.publish(topic = 'semeca/leds', msg = str(var)) #publica o valor ADC lido na porta analogica da ESP. 
    
    print('ADC VALUE.. = %.2f' % var)
 
#Loop infinito chamando leitura do ADC c/ delay de 1s

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

while(True):
    readADC()
    time.sleep_ms(1000)
