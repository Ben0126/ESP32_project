from machine import SoftI2C, Pin
from esp8266_i2c_lcd import I2clcd
from machine import Pin
import urequests
import network
import time
import dht
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

#WIFI nameand its password
ssid = 'Ben'
pw = '0932776126'
if wlan.isconnected() == False:
    wlan.connect(ssid, pw)

#wait for connection
while wlan.isconnected() == False:
    pass
print('connected')

# LCD setting
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=400000)
lcd = I2cLcd(i2c, 0x27, 2, 16)

#Thing speak setting
myChannel = '2550464'
myReadAPI = 'QOIPHHOBWP92J6AG'
readField_1 = 'https://api.thingspeak.com/channels/2550464/fields/1.json?api_key=QOIPHHOBWP92J6AG&results=2'
readField_2 = 'https://api.thingspeak.com/channels/2550464/fields/2.json?api_key=QOIPHHOBWP92J6AG&results=2'
while(True):
    try:
        conn_1 = urequests.get(readField_1)
        H = conn_1.text.split(':')[-1].split('"')[1]
        conn_1.close()
        conn_2 = urequests.get(readField_2)
        H = conn_2.text.split(':')[-1].split('"')[1]
        conn_2.close()
        lcd.putstr('Humidity = '+str(H)+' %\n')
        lcd.putstr('Temperature =', T, ' C')
        prunt('')
        time.sleep(15)
    except:
        print("FUCK")
















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

