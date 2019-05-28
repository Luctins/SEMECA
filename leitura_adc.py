import machine
import time
 
#Função para leitura do ADC através do pino D3 do NodeMCU
 
def readADC():
    adc = machine.ADC(0)
    var= adc.read()
    print('ADC VALUE.. = %.2f' % var)
 
#Loop infinito chamando leitura do ADC c/ delay de 1s
 
while(True):
    readADC()
    time.sleep_ms(1000)
