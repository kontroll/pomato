#!/usr/bin/env python

import curses, time, sys, os
from shutil import which

try:
    kwargs          = {sys.argv[i]: sys.argv[i + 1] for i in range(1, len(sys.argv), 2)}
except:
    sys.exit("Usage: pomato.py [-w 25] [-p 5] [-l 15]")

work_duration   = int(kwargs.get("-w", "25"))*60+1 # We're adding the extra seconds just for appearances' sake
duration        = work_duration
pause           = int(kwargs.get("-p", "5" ))*60+1
long_pause      = int(kwargs.get("-l", "15"))*60+1
time_format     = "%M:%S"

def main(screen):
    global duration, messages
    stage = 0
    xpad = curses.COLS//2-17
    ypad = curses.LINES//2-2
    screen.keypad(True)

    curses.curs_set(0)

    while duration:
        duration -= 1
        screen.clear()
        screen.addstr(1, 2, messages[stage])
        screen.addstr(ypad, 0, draw_timestamp(time.strftime(time_format, time.gmtime(duration)), 1, xpad))
        screen.refresh()

        time.sleep(1)

        if not duration and stage == 7: stage = -1

        while not duration:
            if which("paplay"): # Let's not just assume every system has `paplay`
                os.system("paplay " + os.path.dirname(os.path.realpath(__file__)) + "/alert.ogg")
            action = screen.getkey()
            if action == "q":
                break
            else:
                stage +=1
                if   stage in [1, 3, 5]:
                    duration = pause
                elif stage % 2 == 0:
                    duration = work_duration
                elif stage == 7:
                    duration = long_pause

messages = {0: "First work period!", 1: "Short break!", 2: "More work", 3: "Take a break!",
            4: "Work work!", 5: "Break time", 6: "Worky", 7: "Long break! :)"}

number = [ # Stolen from tty-clock -- Could have been widened programmatically.
     ["██████", "██  ██", "██  ██", "██  ██", "██████"], # 0
     ["    ██", "    ██", "    ██", "    ██", "    ██"], # 1
     ["██████", "    ██", "██████", "██    ", "██████"], # 2
     ["██████", "    ██", "██████", "    ██", "██████"], # 3
     ["██  ██", "██  ██", "██████", "    ██", "    ██"], # 4
     ["██████", "██    ", "██████", "    ██", "██████"], # 5
     ["██████", "██    ", "██████", "██  ██", "██████"], # 6
     ["██████", "    ██", "    ██", "    ██", "    ██"], # 7
     ["██████", "██  ██", "██████", "██  ██", "██████"], # 8
     ["██████", "██  ██", "██████", "    ██", "██████"], # 9
     ["  ",     "██",     "  ",     "██",     "  "    ], # :
     ["  ",     "  ",     "  ",     "  ",     "  "    ], # :, but empty.
]

def draw_timestamp(timestamp="00:00", padding=0, lpadding=0):
    rval = ""
    for i in range(5):
        rval += " "*lpadding
        for character in timestamp:
            if character == ":":
                character = 10 + int(timestamp[-1])%2
            else:
                character = int(character)
            rval += " "*padding + number[character][i]
        rval += "\n"
    return rval


try:
    curses.wrapper(main)
except KeyboardInterrupt:
    print("Time left when exiting:", time.strftime(time_format, time.gmtime(duration)))
    pass
finally:
    pass
