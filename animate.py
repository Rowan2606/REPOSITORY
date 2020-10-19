from sense_hat import SenseHat
from time import sleep

sense = SenseHat
sense.clear()


sense.set_pixel(0,3,(255,0,0))
sleep(.5)
sense.set_pixel(1,5,(255,0,0))
sleep(.5)
sense.set_pixel(2,7,(255,0,0))
sleep(.5)
sense.set_pixel(2,8,(255,0,0))

