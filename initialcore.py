# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:02:05 2018

@author: Xing Su
"""

import edge_differ as ed

def initial_comm_core(graph, inherited_comm):
    comm_cores = []
    dic_inherite = {}
    for i in range (len(inherited_comm)):
        for node in inherited_comm[i]:
            dic_inherite.update({node:i})

    for group in inherited_comm:
        dic_v_edge = {}
        for v in group:
            edgediffer = ed.edge_difference(graph,group,v)
            dic_v_edge.update({v:edgediffer})

        maxdifer = max(dic_v_edge.values())
        maxnode = max(dic_v_edge,key=dic_v_edge.get)

        while maxdifer >=0:
            group.remove(maxnode)
            if group==[]:
                break
            del dic_v_edge[maxnode]

            maxnode_belong = dic_inherite[maxnode]
            for u in graph.neighbors(maxnode):
#                if u==maxnode: continue
                if dic_inherite.__contains__(u)==True and dic_inherite[u]==maxnode_belong:

                    newdiffer = ed.edge_difference(graph,inherited_comm[maxnode_belong],u)
                    dic_v_edge[u] = newdiffer
                else:
                    continue
            dic_inherite[maxnode] = -1
                
            maxdifer = max(dic_v_edge.values(),default=0)
            maxnode = max(dic_v_edge,key=dic_v_edge.get,default=0)

    for group in inherited_comm:
        if len(group)!=0:
            comm_cores.append(group)
      
    return comm_cores