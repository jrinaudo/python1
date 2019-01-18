# template for "Stopwatch: The Game"
import simplegui

# define global variables
tenths = 0
stops = 0
successful_stops = 0
running = False

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    A = t / 600
    B = (t / 100) % 6
    C = (t / 10) % 10
    D = t % 10
    return str(A) + ":" + str(B) + str(C) + "." + str(D)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def startb_handler():
    global running
    if (not running):
        timer.start()
        running = True
    
def stopb_handler():
    global stops, successful_stops, running
    timer.stop()
    if (running):
        stops += 1
        if (tenths % 10 == 0):
            successful_stops += 1
    running = False

def resetb_handler():
    global tenths, stops, successful_stops, running
    if (running):
        timer.stop()
    tenths = 0
    stops = 0
    successful_stops = 0
    running = False

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tenths
    tenths += 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(format(tenths), (50, 115), 40, 'White')
    canvas.draw_text(str(successful_stops) + "/" + str(stops), (145, 30), 30, 'Lime')
    
# create frame
frame = simplegui.create_frame('Stopwatch: The Game', 200, 200, 120)
startButton = frame.add_button('Start', startb_handler, 100)
stopButton = frame.add_button('Stop', stopb_handler, 100)
resetButton = frame.add_button('Reset', resetb_handler, 100)

# register event handlers
frame.set_draw_handler(draw_handler)
timer = simplegui.create_timer(100, timer_handler)

# start frame
frame.start()