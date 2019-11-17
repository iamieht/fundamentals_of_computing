# "Stopwatch: The Game"
import simplegui
# define global variables
time = 0
WIDTH = 200
HEIGHT = 200

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    pass
    
# define event handlers for buttons; "Start", "Stop", "Reset"


# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(str(time), [(HEIGHT / 2), (WIDTH / 2)], 24, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)
frame.set_draw_handler(draw)

# register event handlers
timer = simplegui.create_timer(100, tick)

# start frame
timer.start()
frame.start()


