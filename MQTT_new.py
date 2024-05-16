from umqtt.simple import MQTTClient
import machine,dht,utime,time,network
from time import sleep
from machine import SoftI2C,Pin
from esp8266_i2c_lcd import I2cLcd
import dht
import network
import urequests
dht_sensor = dht.DHT11(Pin(26))
i2c = SoftI2C(scl=Pin(22),sda=Pin(21),freq=400000)
#lcd = I2cLcd(i2c,0x27,2,16)

mq_user='Ben'
mq_pass='0932776126'  #thingspeak mqtt key
wifi= network.WLAN(network.STA_IF)
wifi.active(True)
write_URL = 'https://api.thingspeak.com/update?api_key=FHUXOPQBEOIT91FU&field1=0'
print('---------------------')

ssid = 'Ben'
pw = '0932776126'

if wifi.isconnected() == False:
    wifi.connect(ssid,pw)
    print('---------------------')
    print('start to connect wifi')
    print('---------------------')
while wifi.isconnected() == False:
    pass
print('connected')

iteration = 0
tic = time.time()
while(True):
    iteration = iteration + 1
    info_get = False
    time.sleep(15)
    try:
        dht_sensor.measure()
        H = dht_sensor.humidity()
        T = dht_sensor.temperature()
        print('Humidity =', H, ' %')
        print('Temperature =', T, ' c')
        
        info_get = True
    except:
        print('DHT is fucking not available')
    
    if(info_get):
        conn = urequests.get(write_URL + '&field1=' + str(H) + '&field2=' + str(T))
        conn.close()
        print('request sent')
            
    print('#####################################sent iteration = ' + str(iteration))
