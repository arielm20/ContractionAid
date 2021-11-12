from sensor_library import *
import time
import os
from gpiozero import LED
red = LED(19)
green = LED(13)

muscle_sensor = Muscle_Sensor(0)

def average_value(data_point, data_list):
    data_list.insert(0, data_point)

    avg_value = sum(data_list)/len(data_list)

    return avg_value


def notification(avg_current_contaction, avg_longterm_contaction):
    if (avg_current_contaction > avg_longterm_contaction*1.1): #if current data point is 10 percent above avg
        red.on()

        print("red light is on")

def escalation(current_sensor_data, avg_sensor_data):
    if(current_sensor_data <= avg_sensor_data*1.1):
        green.on()

        print("green light is on")

def timer(count):
 

    if (count >= 240 || count <= 300)
  
        print ("go to hospital")

def main():
    current_contraction_data = []
    longterm_contraction_data = []
    contraction = false
    count = 0
    
    data = True
    while data:
        #read sensor
        current_sensor_data = int(muscle_sensor.muscle_raw())

        print(current_sensor_data)

        if (current_sensor_data > 100):
            contraction = true
            avg_current_contaction = average_value(current_sensor_data, current_contraction_data)
 
            
            
        else:

            if (contraction = true):
                current_contraction_data.clear()
 
                avg_longterm_contaction = average_value(avg_current_contaction, longterm_contraction_data)
            
                if (len(longterm_contraction_data) > 3):
                    notification(avg_current_contaction, avg_longterm_contaction)
                
                    if (redlight = off):
                        escalation(avg_current_contaction, avg_longterm_contaction)
                    else
                        count = 0
           
                    
            
                

                contration = false
            else
                if (redlight = on)
                    count += 1
                    timer(count) #need to figure out where to place timer function

        time.sleep(1)   
main()

