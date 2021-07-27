# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:02:05 2018

@author: Xing Su
"""

import math

def similarities(gh, node1, node2):
    s1 = set(gh.neighbors(node1))
    s1.add(node1)
    s2 = set(gh.neighbors(node2))
    s2.add(node2)
    s12 = len(s1 & s2)
    degree_node1 = gh.degree(node1)
    degree_node2 = gh.degree(node2)
    result = s12 / math.sqrt(degree_node1*degree_node2)
    return result
