import time
import webbrowser
# import sys

def run_timer():
    # Wait for n seconds
    time.sleep(10)

def open_browser():
    # Open a link in the browser
    webbrowser.open('https://www.youtube.com/watch?v=3QTp9OqtYu8')

use_for_loop = True
# Run in while mode
# use_while_loop = not use_for_loop

total_breaks = 3

print "This program started on " + time.ctime()

if use_for_loop:
    for timesExecuted in range(0, total_breaks): # [0, 1, 2]
        # Executing number
        print "Running for the %d work period time" % (timesExecuted + 1)

        run_timer()
        open_browser()
else:
    break_count = 0

    while break_count < total_breaks:
        run_timer()
        open_browser()