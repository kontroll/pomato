# Pomato

A simple and straight-forward implementation of a Pomodoro style timer for the terminal.


![Work, you peon!](screenshot.png)

## Usage
Quit out of Pomato using Ctrl+C any time while it is running, or by pressing `q` at the interval switch-over. Press any other key to proceed to the next interval. Your terminal window needs to be at least 8 rows tall and 34 columns wide.

This script optionally uses `paplay` to play a sound file after each Pomodoro stage finishes.


```bash
$ python pomato [-w 25] [-p 5] [-l 15] [-f tty-clock]
-w    Specify a work period (in minutes)
-p    Specify a pause period
-l    Specify a long pause period
-f    Choose a font; tty-clock (default) or braille-y
```

The command line arguments and default values are presented if you run Pomato with `-h` or `--help`.
