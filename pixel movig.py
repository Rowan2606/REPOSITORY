from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

red = (255,0,0)

sense.set_pixel(red)
x = 4
y = 4

while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            elif event.direction == 'up'
            sense.clear()
            y = y+1
                  sense.set_pixel(x,y,red)
            elif event.direction == 'down':
                sense.clear()
                 y = y-1
                 sense.set_pixel(x,y,red)
            elif event.direction == 'left':
                sense.clear()
                 x = x-1
                 sense.set_pixel(x,y,red)
            elif event.direction == 'right':
                 sense.clear()
                 sense.set_pixel(x,y,red)
                 x = x+1
                
            elif event.action == 'released':
