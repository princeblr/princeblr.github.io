# template for "Stopwatch: The Game"

import simplegui
import random
import time

# define global variables


t = 0
x = 0
y = 0
s = 0
success = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    if t < 600:
        mins = 0
        sec = t / 10
        msec = t % 10
        if sec < 10:
            return str(0) + ":0" + str(sec) + "." + str(msec)
        else:
            return str(0) + ":" + str(sec) + "." + str(msec)
    elif t >= 600:
            mins = t / 600
            secs = t % 600
            sec = secs / 10
            msec = secs % 10
            if sec < 10:
                return str(mins) + ":0" + str(sec) + "." + str(msec)
            else:
                return str(mins) + ":" + str(sec) + "." + str(msec)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"

def Start():
    timer.start()
    
        
    
    
def Stop():
    timer.stop()
    global t, y, success, s, x
    y += 1
    print t
    if t % 10 == 0:
        x = x + 1
    s = str(x) + "/" + str(y)
    return s
    
    
    
    
    

def Reset():
    global t, x, y ,s
    t = 0
    x = 0
    y = 0
    s = 0
    

# define event handler for timer with 0.1 sec interval

def timer_handler():
    global t
    t += 1
    return t
        
    

# define draw handler

def draw(canvas):
    global t, x, y
    canvas.draw_text(str(format(t)),[100,100], 40, "Red")
    canvas.draw_text(str(s),[250,30], 30, "Green")
    
# create frame

frame = simplegui.create_frame("Stopwatch", 300, 200)
timer = simplegui.create_timer(100, timer_handler)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", Start, 200)
frame.add_button("Stop", Stop, 200)
frame.add_button("Reset", Reset, 200)


# start frame

frame.start()
timer.start()
timer.stop()
 
# Please remember to review the grading rubric
