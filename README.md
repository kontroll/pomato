# Pomato

A (currently) naive implementation of a Pomodoro style timer, written in Python.


![Work, you peon!](screenshot.png)

## Usage
This script uses `paplay` to play a sound file after each Pomodoro stage finishes. This is optional; edit line 35 to better suit your system.


```bash
python pomato [-w 25] [-p 5] [-l 15]
-w    Specify a work period (in minutes)
-p    Specify a pause period
-l    Specify a long pause period
```