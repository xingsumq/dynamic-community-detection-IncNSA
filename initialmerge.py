# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:02:05 2018

@author: Xing Su
"""

import similarity as simi

def initial_merge(graph, comm_cores):
    remain_nodes = [] 
    nodes_degree = dict(graph.degree())
    sorted_degree = sorted(nodes_degree.items(),key=lambda deg:deg[1],reverse=True)

    for i in range(len(sorted_degree)):
        remain_nodes.append(sorted_degree[i][0])

    for group in comm_cores:
        for v in group:
            if v in remain_nodes:
                remain_nodes.remove(v)

    for v in remain_nodes:
        max_similarity = 0
        max_node = ''
        for u in graph.neighbors(v):
            if graph.has_edge(v,u):
                similarity = simi.similarities(graph,v,u)

                if similarity >= max_similarity:
                    max_similarity = similarity
                    max_node = u

        if max_node == '':
            max_degree = 0
            for u in graph.neighbors(v):
                if graph.degree(u) > max_degree:
                    max_degree = graph.degree(u)
                    max_node = u
        else:
            merge_index = -1
            for i in range(len(comm_cores)):
                if max_node in comm_cores[i]:
                    merge_index = i  
                    break
            if merge_index== -1:
                comm_cores.extend([v.split() + max_node.split()])
                remain_nodes.remove(max_node)
            else:    
                comm_cores[merge_index] = comm_cores[merge_index] + v.split()
    global initial_comm
    initial_comm = comm_cores
    return initial_comm