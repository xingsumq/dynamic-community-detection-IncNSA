# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:02:05 2018

@author: Xing Su
"""

def read_change_nodes(filename, start, end):
    changed_nodes = []
    recording = False
    
    with open(filename) as f1:
        for line in f1:
            line = line.strip()
            
            if line == end:
                break
            if recording:
                changed_nodes.append(line)
            if line == start:
                recording = True
    return changed_nodes