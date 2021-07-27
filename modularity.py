# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:02:05 2018

@author: Xing Su
"""

def modularity(G, partition):
  m=len(G.edges())
  Q=0.0
  
  pKeys=partition.keys()
  for key in pKeys:
    inner_edge=0; out_edge=0
    for u in partition[key]:
      N_u=G.neighbors(u)
      for v in N_u:
        if v in partition[key]: inner_edge += 1
        else: out_edge += 1
    #end of for u in partition[key]
    eii=inner_edge/(2.0*m); ai=(out_edge+inner_edge)/(2.0*m)
    Q +=  eii-ai*ai
  #end of for key in pKeys
  return Q
#end of def modularity(G, partition)
