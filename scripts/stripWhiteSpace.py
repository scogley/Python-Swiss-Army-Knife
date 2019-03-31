#! /usr/bin/env python3
# stripWhiteSpace.py - rstrip() method will remove whitespace characters from the right end

import pyperclip
text = pyperclip.paste()

# Separate lines and strip whitespace
lines = text.split('\n')
for i in range(len(lines)): #loop through all indexes in the "lines" list
    lines[i] = lines[i].rstrip() # remove trailing whitespace
text = '\n'.join(lines)
pyperclip.copy(text)