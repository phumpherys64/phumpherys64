# robot.py
# $ python3 robot.py input.txt
# or
# cat input.txt | python3 robot.py
# TODO use format string
# TODO use def
# BUG no bugs
# FIXME issue goes here

import fileinput

x = 0
y = 0
decimals = ['0','1','2','3','4','5','6','7','8','9']
offset = 0

for line in fileinput.input():
    direction_str = ""
    offset_str = ""
    for ch in line:
        if ch in decimals:
            offset_str += ch
        else:
            direction_str += ch    
    offset = int(offset_str)   
    
    if direction_str[0] == "U":
        y += offset
    elif direction_str[0] == "L":
        x -= offset
    elif direction_str[0] == "R":
        x += offset
    else:
        y -= offset
        
print("(", x, ",", y, ")")
