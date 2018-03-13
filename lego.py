from time   import time, sleep
from ev3dev.auto import *

lewy = LargeMotor(outA)  #sprawdzic lewy
prawy = LargeMotor(outD) #sprawdzic prawy
collewy= ColorSensor(in1)
colprawy= ColorSensor(in4)

def kalibracja(czarny,bialy, silniklewy,silnikprawy,predkosc, czas):
  lewy.runtimed(time_sp = czas, speed_sp = predkosc)
  prawy.runtimed(time_sp = czas, speed_sp = (predkosc * (-1)))
  collewy.mode = 'COL-REFLECT'
  colprawy.mode = 'COL-REFLECT'
  max = 0
  min = 100
  
  czaskonc = time.time() + czas
  while time.time() < czaskonc :
    if 
