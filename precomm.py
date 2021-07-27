# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:02:05 2018

@author: Xing Su
"""

# obtain community structure of previous timestampt. 
def read_pre_comm(filename):
    previous_comm = []
    
    with open(filename) as f2:
        for line in f2:
            line = line.strip()
            line = line.split(' ')
            previous_comm.append(line)
    return previous_comm