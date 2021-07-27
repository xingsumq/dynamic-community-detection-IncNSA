# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:02:05 2018

@author: Xing Su
"""

def edge_difference(graph,comm,node):
    in_edge = 0
    out_edge = 0
    
    neibor_v = graph.neighbors(node)
    if neibor_v==[]:
        edge_differ = -1
    for u in neibor_v:
        if u in comm: in_edge +=1
        else: out_edge +=1
    edge_differ = out_edge - in_edge
    
    return edge_differ


