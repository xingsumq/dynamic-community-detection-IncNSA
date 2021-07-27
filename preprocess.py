# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:02:05 2018

@author: Xing Su
"""
import networkx as nx
import os

def preprocess(path, path_of_dataset, number_of_timestampt): 
    
    if not os.path.exists(path+'/pre_inform'): 
        os.mkdir(path + '/pre_inform')
    else: 
        pass
        
    for i in range(1,number_of_timestampt):
        d=i+1
        graph_old = nx.Graph(nx.read_edgelist(path_of_dataset + '/{}'.format(i)))
        graph_new = nx.Graph(nx.read_edgelist(path_of_dataset + '/{}'.format(d)))
        
        v_old = graph_old.nodes()  
        v_new = graph_new.nodes()
        e_old = graph_old.edges()  
        e_new = graph_new.edges()
        deg_old = dict(graph_old.degree())
        deg_new = dict(graph_new.degree())
    
        if not os.path.exists(path+'/pre_inform/inform_{}_{}.txt'.format(i,d)):
            f = open(path+'/pre_inform/inform_{}_{}.txt'.format(i,d),'w')

            f.write("*Disappearing Nodes\n")
            for v in v_old:
                if v not in v_new:
                    f.write("{}\n".format(v))
            f.write("#End Disappearing Nodes\n")
            
            f.write("\n*Newborn Nodes\n")
            for v in v_new:
                if v not in v_old:
                    f.write("{}\n".format(v))
            f.write("#End Newborn Nodes\n")
               
            f.write("\n*Disappearing Edges\n")         
            for (u,v) in e_old:
                if (u,v) not in e_new:
                    f.write("{}\t{}\n".format(u,v))
            f.write("#End Disappearing Edges\n")
            
            f.write("\n*Newborn Edges\n")         
            for (u,v) in e_new:
                if (u,v) not in e_old:
                    f.write("{}\t{}\n".format(u,v))
            f.write("#End Newborn Edges\n")
            
            f.write("\n*Degree Changed Nodes\n")
            for node in deg_old.keys():
                if (node in deg_new.keys()) and (deg_old[node] != deg_new[node]):
                    f.write("{}\t{}\t{}\n".format(node,deg_old[node],deg_new[node]))
            
            f.close()
                
        else: 
            pass
    
    return "preprocessing is completed!"
        
        
