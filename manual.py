from blynkapi import Blynk
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(19, GPIO.OUT)

p = GPIO.PWM(19, 50)
p1 = GPIO.PWM(18, 50)
p.start(0)
p1.start(0)

auth = "f1f169ef17fa45b0824b085f42c1e4ec"
Blynk(auth,)

print(Blynk(auth).app_status())
print(Blynk(auth).hw_status())

def SetAngle1(angle):
    print("Angle: ")
    print(angle)
    duty_cycle = (angle/18)+2
    GPIO.output(19, True)
    p.ChangeDutyCycle(duty_cycle)
    GPIO.output(19, False)
    
def SetAngle2(angle):
    print("Angle: ")
    print(angle)
    duty_cycle = (angle/18)+2
    GPIO.output(18, True)
    p1.ChangeDutyCycle(duty_cycle)
    GPIO.output(18, False)

while 1:
    value0 = Blynk(auth, pin = "V0").get_val()
    print('v0        ',value0)
    value2 = Blynk(auth, pin = "V2").get_val()
    print('v2        ',value2[0])
    if int(value2[0]) == 1:
        
        print("0 degree")
        SetAngle1(90)
        SetAngle2(0)
        time.sleep(5)
        GPIO.output(17,True)
        GPIO.output(23,True)
        
        GPIO.output(27,False)
        GPIO.output(24,False)

        print('forward')
        time.sleep(5)
        GPIO.output(17,False)
        GPIO.output(23,False)
        
        GPIO.output(27,False)
        GPIO.output(24,False)
        time.sleep(1)
        print("90 degree")
        SetAngle1(0)
        SetAngle2(90)
        time.sleep(5)
    
    if int(value0[0])==1:
        GPIO.output(17,False)
        GPIO.output(23,True)
        
        GPIO.output(27,True)
        GPIO.output(24,False)
        print('right')
    
    elif int(value0[0])==-1:
        
        GPIO.output(17,True)
        GPIO.output(23,False)
        
        GPIO.output(27,False)
        GPIO.output(24,True)
        print('left')

    elif int(value0[1])==1:
        GPIO.output(17,True)
        GPIO.output(23,True)
        
        GPIO.output(27,False)
        GPIO.output(24,False)

        print('forward')
        
    elif int(value0[1])==-1:
        GPIO.output(17,False)
        GPIO.output(23,False)
        
        GPIO.output(27,True)
        GPIO.output(24,True)
        
        print('back')
    
    elif int(value0[0])==0 or int(value0[1]) == 0:
        GPIO.output(17,False)
        GPIO.output(23,False)
        GPIO.output(27,False)
        GPIO.output(24,False)

        print('center')

