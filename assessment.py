from sense_hat import SenseHat
sense=SenseHat()
sense.clear()
w = (255,255,255)
n = 1

while True:
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            if event.direction == 'right': 
                n == 1
            if event.direction == 'left':
                n == n+1
    for event in sense.stick.get_events():
        if event.action == 'pressed':
            if event.direction == 'right':
                temp=sense.get_temperature()
                temp = round(temp,2)
                if temp < 20:
                    sense.show_message("TEMP TOO LOW", text_colour=(255,0,0), back_colour=(0,0,0))
                if temp > 40:
                    sense.show_message("TEMP TOO HIGH", text_colour=(255,0,0), back_colour=(0,0,0))
                else:
                    sense.show_message(str(temp), text_colour=(100,0,0), back_colour=(0,0,0))
                    
            elif event.direction == 'left':
                pressure=sense.get_pressure()
                pressure = round(pressure,2)
                if pressure < 1000:
                    sense.show_message("PRESSURE TOO LOW", text_colour=(255,0,0), back_colour=(0,0,0))
                if pressure > 1020:
                    sense.show_message("PRESSURE TOO HIGH", text_colour=(255,0,0), back_colour=(0,0,10))
                else:
                    sense.show_message(str(pressure), text_colour=(255,255,0), back_colour=(0,0,0))
             

                        
                
                        

