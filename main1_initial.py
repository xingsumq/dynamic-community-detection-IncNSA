# -*- coding: utf-8 -*-
"""
Created on Wed May  9 10:15:00 2018

@author: Xing Su
"""
import networkx as nx
#import NMI as NMI_fuc
import modularity as modu
import os

def jaccard(gh, node1, node2):
    s1 = set(gh.neighbors(node1))
    s1.add(node1)
    s2 = set(gh.neighbors(node2))
    s2.add(node2)
    s12 = len(s1 & s2)
    return s12 / float(len(s1)+len(s2)-s12)


def similarities(gh, node1, node2):
    result = jaccard(gh, node1, node2)
    return result


def group_similarities(gh, group1, group2):
    total_similarity = 0.0

    for node1 in group1:
        for node2 in group2:
            if gh.has_edge(node1, node2):
                total_similarity += similarities(gh, node1, node2)
    total_similarity /= len(group2)
    return total_similarity


def ratio(gh, group):
    inout_ratio = 0.0
    inner_edge = 0
    out_edge = 0

    for node1 in group:
        N_node1 = gh.neighbors(node1)
        for node2 in N_node1:
            if node2 in group: inner_edge +=1
            else: out_edge +=1
        else: continue
  
    if out_edge == 0.0:
        inout_ratio = 1000
    else:
        inout_ratio = (inner_edge/(out_edge*2)) * (len(group)/len(gh))
   
    return inout_ratio


def InitialMerge(gh):
    sorted_nodes = []
    nodes_degree = dict(graph.degree())
    sorted_degree = sorted(nodes_degree.items(),key=lambda deg:deg[1],reverse=True)
    for i in range(len(sorted_degree)):
        sorted_nodes.append(sorted_degree[i][0])
    merge = []
    for v in sorted_nodes:
        max_similarity = 0
        max_node = ''
        for u in graph.neighbors(v):
            if graph.has_edge(v,u):
                similarity = similarities(graph,v,u)
                if similarity >= max_similarity:
                    max_similarity = similarity
                    max_node = u
        
        if merge==[] :
            merge.extend([v.split() + max_node.split()])
            sorted_nodes.remove(max_node)
        else:
            merge_index = -1
            for i in range(len(merge)):
                if max_node in merge[i]:
                    merge_index = i  
                    break
            if merge_index== -1:
                merge.extend([v.split() + max_node.split()])
                sorted_nodes.remove(max_node)
            else:    
                merge[merge_index] = merge[merge_index] + v.split()
    global groups
    groups = merge
    return groups
                

def merge_closure_by_ratio(gh):
    closure_ratio = []
    for i in range(len(groups)):
        closure_ratio.append(ratio(gh, groups[i]))   
    min_ratio=min(closure_ratio)  
       
    while min_ratio < merge_ratio:
        max_similarity = 0
        max_index = -1 
        min_groups_index=closure_ratio.index(min(closure_ratio))
        for j in range(len(groups)):
            if j != min_groups_index :
                total_similarity = group_similarities(gh, groups[min_groups_index], groups[j])
                if total_similarity > max_similarity:
                    max_similarity = total_similarity
                    max_index = j
        groups[max_index]=groups[min_groups_index]+groups[max_index]
        closure_ratio[max_index] = ratio(gh, groups[max_index])
        del closure_ratio[min_groups_index]
        del groups[min_groups_index]
         
        min_ratio = min(closure_ratio)
    return groups




if __name__ == '__main__':
    
    merge_ratio = 0.2  # Please set parameter, usually less than 0.3 
    graph = nx.Graph(nx.read_edgelist("./syn_datasets/birth_death/birth_death_data/1")) # Please input the path of the 1st timestampt 
    path = r'./syn_datasets/birth_death' # Please input the file directory.  
    
    initial_groups = InitialMerge(graph)
    final_groups = merge_closure_by_ratio(graph)   
    num = len(final_groups)
    a = [i for i in range(num)]
    communities = dict(zip(a,final_groups))
    print ('raio =',merge_ratio, 'Q =', modu.modularity(graph , communities))
    
    
    if not os.path.exists(path+'/community'): 
        os.mkdir(path + '/community')
    else: 
        pass
    
    if not os.path.exists(path+'/community/community1.txt'): 
        f = open(path + "/community/community1.txt",'a+')
        for com in communities.values():
            for node in com:
                f.write("{} ".format(node))
            f.write("\n")
        f.close()
    else: 
        pass
    


       
    