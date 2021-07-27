# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:02:05 2018

@author: Xing Su
"""

# obtain the initial community structure after removing disappeared nodes.

def delete_prenodes(previous_comm, disappeared_nodes):
    inherited_comm = []
    for group in previous_comm:
        inherited_group = []
        for node in group:
            if node not in disappeared_nodes:
                inherited_group.append(node)
#        print(inherited_group)
        if len(inherited_group)!=0:
            inherited_comm.append(inherited_group)

    return inherited_comm