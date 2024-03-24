"""
robot.py
    
A file argument can be used i.e.:  robot.py inputfile.txt
Or pipe stdin:  cat input.txt | robot.py
    
Example INSTRUCTIONS:
UP 1
RIGHT 10
DOWN 5
LEFT 2

% cat input.txt | python3 robot.py
(8,-4)    

% chmod +x ./robot.py    
% ./robot.py input.txt 
(8,-4)
    
docstring
print(robot_def.__doc__)
    
"""

import fileinput

def robot():
    """returns "(x,y)" str from input (stdin or filename as arguement) of <INSTRUCTIONS>
    
    Example <INSTRUCTIONS>:
    ----------------------
    
    UP 1
    RIGHT 10
    DOWN 5
    LEFT 2
    
    Returns
    -------
    "(x,y)" str  Coordinates of robot after executing <INSTRUCTIONS>
    
    """
    
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
            
    print(f"({x},{y})")
