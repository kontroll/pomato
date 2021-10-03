numbers = {
     "tty-clock": {                 # Adapted from tty-clock!
     "0": ["██████", "██  ██", "██  ██", "██  ██", "██████"],
     "1": ["    ██", "    ██", "    ██", "    ██", "    ██"],
     "2": ["██████", "    ██", "██████", "██    ", "██████"],
     "3": ["██████", "    ██", "██████", "    ██", "██████"],
     "4": ["██  ██", "██  ██", "██████", "    ██", "    ██"],
     "5": ["██████", "██    ", "██████", "    ██", "██████"],
     "6": ["██████", "██    ", "██████", "██  ██", "██████"],
     "7": ["██████", "    ██", "    ██", "    ██", "    ██"],
     "8": ["██████", "██  ██", "██████", "██  ██", "██████"],
     "9": ["██████", "██  ██", "██████", "    ██", "██████"],
     ":": ["  ",     "██",     "  ",     "██",     "  "    ],
     " ": ["  ",     "░░",     "  ",     "░░",     "  "    ],
     },
     "braille-y": {
     "0": ["⣴⣿⣿⣿⣿⣦", "⣿⣿  ⣿⣿", "⣿⣿  ⣿⣿", "⣿⣿  ⣿⣿", "⠻⣿⣿⣿⣿⠟"],
     "1": ["    ⣴⣿", "    ⣿⣿", "    ⣿⣿", "    ⣿⣿", "    ⣿⣿"],
     "2": [ "⣴⣿⣿⣿⣿⣦", "    ⣿⣿", "⣾⣿⣿⣿⣿⠟", "⣿⣿    ", "⣿⣿⣿⣿⣿⣿"],
     "3": ["⣿⣿⣿⣿⣿⣦", "    ⣿⣿", "⢸⣿⣿⣿⣿⣯", "    ⣿⣿", "⣿⣿⣿⣿⣿⠟"],
     "4": ["⣼⣿  ⣿⣿", "⣿⣿  ⣿⣿", "⣿⣿⣿⣿⣿⣿", "    ⣿⣿", "    ⣿⣿"],
     "5": ["⣿⣿⣿⣿⣿⣿", "⣿⣿    ", "⠻⣿⣿⣿⣿⣦", "    ⣿⣿", "⣿⣿⣿⣿⣿⠟"],
     "6": ["⣴⣿⣿⣿⣿⣷", "⣿⣿    ", "⣿⣿⣿⣿⣿⣦", "⣿⣿  ⣿⣿", "⠻⣿⣿⣿⣿⠟"],
     "7": ["⣿⣿⣿⣿⣿⣿", "    ⣿⣿", "    ⣿⣿", "    ⣿⣿", "    ⣿⣿"],
     "8": ["⣴⣿⣿⣿⣿⣦", "⣿⣿  ⣿⣿", "⣽⣿⣿⣿⣿⣯", "⣿⣿  ⣿⣿", "⠻⣿⣿⣿⣿⠟"],
     "9": ["⣴⣿⣿⣿⣿⣦", "⣿⣿  ⣿⣿", "⠻⣿⣿⣿⣿⣿", "    ⣿⣿", "⠻⣿⣿⣿⣿⠟"],
     ":": ["  ",     "⣿⣿",     "  ",     "⣿⣿",     "  "    ],
     " ": ["  ",     "⡪⡪",     "  ",     "⡪⡪",     "  "    ],
     },
}

# Aliases
numbers["b"] = numbers["braille-y"]
