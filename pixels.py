from sense_hat import SenseHat
sense = SenseHat()
sense.clear()

blue = (0,0,255)
red = (255,0,0)

sense.set_pixel(3,2,blue)
sense.set_pixel(5,4,red)
sense.set_pixel(3,3,blue)
sense.set_pixel(3,4,blue)
sense.set_pixel(5,3,red)
sense.set_pixel(5,2,red)
sense.set_pixel(5,7,blue)
sense.set_pixel(3,7,blue)
sense.set_pixel(1,6,blue)
sense.set_pixel(6,6,red)
sense.set_pixel(5,7,red)
sense.set_pixel(4,7,red)