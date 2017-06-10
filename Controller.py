from time import sleep
import spidev
import curses
#import RPi.GPIO as GPIO
spi = spidev.SpiDev()
spi.open(0,1)

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

#spi.max_speed_hz = 1000000
speed = 250
forwards = 2
backwards = 3
left = 4
right = 5
stop = 6

number = 0


try:
    while True:
        
       
   
        char = screen.getch()
        if char == ord('q'):
            break
        elif char == curses.KEY_UP:
             resp = spi.xfer2([forwards])
            #sleep(0.1)
        elif char == curses.KEY_DOWN:
             resp = spi.xfer2([backwards])
            #sleep(0.1)
        elif char == curses.KEY_LEFT:
             resp = spi.xfer2([right])
            #sleep(0.1)
        elif char == curses.KEY_RIGHT:
             resp = spi.xfer2([left])
        elif char == ord('s'):
             resp = spi.xfer2([stop])
           # sleep(0.1)    
        elif char == ord('u'):
            speed += 1
            if speed > 255:
                speed=255            
            resp = spi.xfer2([0x01])
            sleep(0.01)
            resp = spi.xfer2([speed])
            print speed
        elif char == ord('j'):
            speed -= 1
            if speed <= 7:
                speed=7            
            resp = spi.xfer2([0x01])
            sleep(0.01)
            resp = spi.xfer2([speed])
            print speed
            
             
            
    
    
        
        
            
        
            
        
       # resp = spi.xfer2([forwards])
       # print resp
       # sleep(0.1)
    
        

finally:                # run on exit
    spi.close()         # clean up
    curses.nocbreak()
    screen.keypad(0)
    curses.echo()
    curses.endwin()
    print "All cleaned up."
