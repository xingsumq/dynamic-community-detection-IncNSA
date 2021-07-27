# -*- coding: utf-8 -*-
"""
Created on Tue May  8 17:02:05 2018

@author: Xing Su
"""


def fastQ(G,finalCommunity):
    cs={}
    for i in range(len(finalCommunity)):
        cs[i]=finalCommunity[i]
    mmb={v:k for k in cs for v in cs[k]}
    e,a = {(k,k):0 for k in cs},{k:0 for k in cs}
    m=G.number_of_edges()
    for (u,v) in G.edges():
        i,j=mmb[u],mmb[v]
        
        e[(i,j)] = e[(i,j)] + 1.0 if (i,j) in e else 1.0
        e[(j,i)] = e[(j,i)] + 1.0 if (j,i) in e else 1.0
      #end of for(u,v) in G.edges()
    for (i,j) in e:
        e[(i,j)] /= 2.0*m
        a[i] = a[i] + e[(i,j)] if i in a else 0.0
      #end of for (i,j) in e     
    while 1:  
        dQ_max,si,sj = -100,None,None
        for (i,j) in e:   
          if i>=j: continue
          dQ=e[(i,j)]-a[i]*a[j]    
          if dQ >= dQ_max and dQ > 0: si,sj,dQ_max = i,j,dQ
        #end of for i, j in i_j

        if si is None or sj is None:
            break
    #    print 'si=',si,'sj=',sj
        cs[si]= list(set(cs[si]) | set(cs[sj]))  
        cs.pop(sj)    
    
        dQ += dQ_max*2.0      
        if dQ>=dQ_max: dQ_max = dQ; 
   

        a[si] += a[sj]; a.pop(sj)
        e[(si,si)] += e[(sj,sj)]
        get=e.get
        for k in cs:
          e_jk=get((sj,k),-1)
          if e_jk > 0: 
              e[(si,k)] = e[(si,k)]+e_jk if (si,k) in e else e_jk
          e_kj=get((k,sj),-1)
          if e_kj > 0:
              e[(k,si)] = e[(k,si)]+e_kj if (k,si) in e else e_kj
          if(k,sj) in e: e.pop((k,sj))
          if(sj,k) in e: e.pop((sj,k))
        #end of for k in cs
      #end of while 1
    return cs  