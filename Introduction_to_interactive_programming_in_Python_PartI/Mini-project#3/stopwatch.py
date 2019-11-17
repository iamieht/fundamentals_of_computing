# "Stopwatch: The Game"
import simplegui
# define global variables
time = 0
WIDTH = 200
HEIGHT = 200
total_stops = 0
points = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    min = t // 600
    secs = ((t // 10) % 60) // 10
    tenths = ((t // 10) % 60) % 10
    milisecs = t % 10
    return str(min) + ":" + str(secs) + str(tenths) + "." + str(milisecs)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    timer.start()
    
def stop():
    global total_stops, points
    
    if timer.is_running():
        total_stops += 1
    
        if time % 10 == 0:
            points += 1
    
    timer.stop()
        
    
def reset():
    global time, total_stops, points
    timer.stop()
    time = 0
    total_stops = 0
    points = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global time
    time += 1

# define draw handler
def draw(canvas):
    canvas.draw_text(format(time), [50, (WIDTH / 2)], 48, "White")
    canvas.draw_text(str(points) + "/" + str(total_stops), [150, 20], 18, "White")
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)
frame.set_draw_handler(draw)
frame.add_button("Start", start, 200)
frame.add_button("Stop", stop, 200)
frame.add_button("Reset", reset, 200)

# register event handlers
timer = simplegui.create_timer(100, tick)

# start frame
frame.start()


