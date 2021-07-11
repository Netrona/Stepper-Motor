import RPi.GPIO as GPIO
import spidev
import time
import thread
import os

def input_thread(L):
  while True:
    raw_input()
    L.append(None)
    
    
def print_thread(L):
  while True:
    print('\033[0;0HIntegration Project')
    print("----------------------------------------- ")
    print("Press Enter to change direction of motor: ")
    print("----------------------------------------- ")
    if (not change_direction and detect_left(HE_value)) or (change_direction and detect_right(HE_value)):
      print("Current direction is: LEFT")
    elif (not change_direction and detect_right(HE_value)) or (change_direction and detect_left(HE_value)):
      print("Current direction is: RIGHT")
    else:
      print("Current direction is: NONE")
    print("Reading on HE sensor: {0:4d}".format(HE_value))
    print("Reading on IR sensor: {0:4d}".format(IR_value))
    time.sleep(.1)
    
def adc_return_value(chan):
  response = spi.xfer2([1,128+(chan<<4),0])
  return (response[1] &3)*256 + response[2]


def detect_left(value):
  return True if value < 500 else False


def detect_right(value):
  return True if value > 900 else False


spi = spidev.SpiDev()
spi.open(0,1)
GPIO.setmode(GPIO.BCM)

stepper_pins=[13,16,26,21]
LED_all=[19,20,12,25,24,23,18]
LED_left=[18,12,20]
LED_right=[18,20,18,23]
GPIO.setup(stepper_pins,GPIO.OUT)
GPIO.setup(LED_all,GPIO.OUT)

stepper_lower = 0.001
stepper_upper = 0.01
IR_lower = 200
IR_upper = 900
scale = float((stepper_upper - stepper_lower)/(IR_upper - IR_lower))


stepper_sequence=[]
stepper_sequence.append([GPIO.HIGH, GPIO.LOW, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.HIGH, GPIO.HIGH, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.HIGH, GPIO.LOW,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.HIGH, GPIO.HIGH,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.HIGH,GPIO.LOW])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.HIGH,GPIO.HIGH])
stepper_sequence.append([GPIO.LOW, GPIO.LOW, GPIO.LOW,GPIO.HIGH])
stepper_sequence.append([GPIO.HIGH, GPIO.LOW, GPIO.LOW,GPIO.HIGH])
change_direction = False


try:
  os.system('clear')
  L = []
  thread.start_new_thread(input_thread, (L,))
  thread.start_new_thread(print_thread, (L,))
  
  while True:
    if L:
      change_direction = not change_direction
      L[:] = []
      IR_value = adc_return_value(chan = 0)
      HE_value = adc_return_value(chan = 1)
      IR_valueFIX = IR_value
      
    if IR_value < IR_lower: IR_valueFIX = IR_lower
      elif IR_value > IR_upper: IR_valueFIX = IR_upper
      sleep_time = (IR_valueFIX - IR_lower)*scale + stepper_lower
      sleep_time = stepper_upper - sleep_time + stepper_lower
      
    if sleep_time < stepper_lower: sleep_time = stepper_lower
      
    elif sleep_time > stepper_upper: sleep_time = stepper_upper
      
    if (detect_left(HE_value) and not change_direction) or (change_direction and detect_right(HE_value)):
      for row in stepper_sequence:
        GPIO.output(stepper_pins,row)
        time.sleep(sleep_time)
      for value in LED_right:
        GPIO.output(value,GPIO.LOW)
      for value in LED_left:
        GPIO.output(value,GPIO.HIGH)
        
    elif (detect_right(HE_value) and not change_direction) or (change_direction and detect_left(HE_value)) :
      for row in reversed (stepper_sequence):
        GPIO.output(stepper_pins,row)
        time.sleep(sleep_time)
      for value in LED_left:
        GPIO.output(value, GPIO.LOW)
      for value in LED_right:
        GPIO.output(value, GPIO.HIGH)
     else:
       for value in LED_all:
         GPIO.output(value, GPIO.LOW)
  
except KeyboardInterrupt:
  GPIO.cleanup()
