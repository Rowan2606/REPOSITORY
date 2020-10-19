from sense_hat import SenseHat

sense = SenseHat
sense.clear()

for x in range(0,7):
    ect.cell(image,[0,x],[randint(0,255), randint(0,255), randint(0,255)],0.1)
    ect.cell(image,[0,x],e,0.1)
    
for x in range(7,0, -1):
    ect.cell(image,[0,x],[randint(0,255), randint(0,255), randint(0,255)],0.1)
    ect.cell(image,[0,x],e,0.1)