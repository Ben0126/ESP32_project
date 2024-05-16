from umqtt.simple import MQTTClient
import machine,dht,utime,time,network
from time import sleep
from machine import SoftI2C,Pin
from esp8266_i2c_lcd import I2cLcd
import dht
import network

dht_sensor = dht.DHT11(Pin(26))
i2c = SoftI2C(scl=Pin(22),sda=Pin(21),freq=400000)
lcd = I2cLcd(i2c,0x27,2,16)

mq_server = 'mqtt.thingspeak.com'
mq_id = 'esp00001' 
mq_topic = "channels/" + "2532033" + "/publish/" + "T6HQWW866WPQGBIU" #id + write_api  
mq_user='FW'
mq_pass='12345678'  #thingspeak mqtt key
wifi= network.WLAN(network.STA_IF)
wifi.active(False)
wifi.active(True)

ssid = 'Ben'
pw = '12345678'
if wifi.isconnected() == False:
    wifi.connect(ssid,pw)
    print('---------------------')
    print('start to connect wifi')
    print('---------------------')
while wifi.isconnected() == False:
    pass
print('connected')

# while(True):
#     try:
# 
#     except:
# #         print('DHT is not avilable')
# #        lcd.putstr('DHT is not avilable');
# #         print(' ')
#         sleep(5)
#         print('no data')

dht_sensor.measure()
H = dht_sensor.humidity()
T = dht_sensor.temperature()
print('Humidity =', H, ' %')
print('Temperature =', T, ' c')
print(' ')
h = str(H)
t = str(T)
h_str = str('Humidity =') + h + str(' %')
t_str = str('Temperature =') + t + str(' c')
s = h_str +"\n"+ t_str
lcd.putstr(s);
sleep(5)
lcd.clear()


mqClient0 = MQTTClient(mq_id, mq_server, user=mq_user, password=mq_pass)
mqClient0.connect()
i=0
while True:
    i=i+1
    dht_sensor.measure()
    mq_message='field1={}&field2={}'.format(dht_sensor.temperature(),dht_sensor.humidity())
    mqClient0.publish(mq_topic, mq_message)
    print("message publish {}".format(i))
    time.sleep(18)         

