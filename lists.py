from sense_hat import SenseHat

sense = SenseHat()

# define colours
g = (0,255,0)
b = (255,255,255)

# setup matrix variable
image_pixels = [
    g,g,g,g,g,g,g,g,
    g,g,g,g,g,g,g,g,
    g,b,b,g,g,b,b,g,
    g,b,b,g,g,b,b,g,
    g,g,g,b,b,g,g,g,
    g,g,g,b,b,g,g,g,
    g,g,b,b,b,b,g,g,
    g,g,b,g,g,b,g,g,
    ]

sense.set_pixels(image_pixels)
    