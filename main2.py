# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 10:17:44 2018

@author: Xing Su
"""

import networkx as nx
import modularity as modu
import os
import preprocess
import changednodes as cnodes
import precomm
import delete_prenodes as delnodes
import initialcore
import initialmerge
import finalmerge
           

             
n_stampt = 10 # Please set the number of time steps. 
path = r'./syn_datasets/birth_death' # Please input the file directory. 
path_dataset = r'./syn_datasets/birth_death/birth_death_data' # Please input the file path of dataset. 

for i in range(1, n_stampt):    
    preprocess.preprocess(path, path_dataset, n_stampt)
    graph = nx.Graph(nx.read_edgelist(path_dataset+"/{}".format(i+1)))
    disappeared_nodes = cnodes.read_change_nodes(path+"/pre_inform/inform_{}_{}.txt".format(i,i+1),start='*Disappearing Nodes', end='#End Disappearing Nodes')
    previous_comm = precomm.read_pre_comm(path+"/community/community{}.txt".format(i))
    inherited_comm = delnodes.delete_prenodes(previous_comm, disappeared_nodes)
    comm_cores = initialcore.initial_comm_core(graph, inherited_comm) 
    initial_communities = initialmerge.initial_merge(graph, comm_cores)
    final_result = finalmerge.fastQ(graph,initial_communities)
    
    final_groups = list(final_result.values())
    n=len(final_result)
    Q = modu.modularity (graph , final_result)
    print ('Timestamp: {}, '.format(i+1), 'Number of Communities = {}, '.format(n), 'Q = {}, '.format(Q))

    with open(path+"/Q.txt",'a+') as f:
        f.write('{}\tQ = {}\tn = {}\n'.format(i+1,Q,n))
    
    if not os.path.exists(path+'/community/community{}.txt'.format(i+1)):     
        f1 = open(path+"/community/community{}.txt".format(i+1),'w')
        for comm in final_result.values():
            for com in comm:
                f1.write("{} ".format(com))
            f1.write("\n")
        f1.close() 
    else: 
        pass
    
 