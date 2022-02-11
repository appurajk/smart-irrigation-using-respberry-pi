import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(19,GPIO.OUT)


GPIO.setup(24,GPIO.IN)

GPIO.setwarnings(False)
sensor= Adafruit_DHT.AM2302
print(' ......Well come to Smart Agriculture System........')
print('____________________________________________________')
print(' START INITIALIZATION....')
humidity, temperature = Adafruit_DHT.read_retry(sensor,4)
print('Temp={0:0.1f}*  Humidity={1:0.1f}%'.format(temperature, humidity))



if temperature > 20:
    print('Temperature is High')
    GPIO.output(19,1)
    print('Motor Turns on')
    sleep(5)
    print('Motor Turns off')
    GPIO.output(19,0)
    print('Moisture detected')
else:
    GPIO.output(19,0)
    print('Motor turns off')
    

def callback(channel):
    if GPIO.input(24):
        print("Moisture level is Low")
        GPIO.output(19,1)   
        print("driper turns on")
        print("----------------")    
    else:
        print("water detected")
        GPIO.output(19,0)
        print("driper turns off")
        print("___________________")
GPIO.add_event_detect(24, GPIO.BOTH, bouncetime=10)
GPIO.add_event_callback(24, callback)

while True:
    sleep(1)
GPIO.clearup()


    
