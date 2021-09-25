# Pomato

A (currently) naive implementation of a Pomodoro style timer, written in Python.


![Work, you peon!](screenshot.png)

## Usage
This script optionally uses `paplay` to play a sound file after each Pomodoro stage finishes.


```bash
python pomato [-w 25] [-p 5] [-l 15]
-w    Specify a work period (in minutes)
-p    Specify a pause period
-l    Specify a long pause period
```