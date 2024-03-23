#!/usr/bin/env python3

"""robot.py
    
A file argument can be used i.e.:  robot.py inputfile.txt
Or pipe stdin:  cat input.txt | robot.py
    
Example input:
UP 1
RIGHT 10
DOWN 5
LEFT 2

% cat input.txt | python3 robot.py
(8,-4)    
    
    
"""

from robot_def import *

robot()
