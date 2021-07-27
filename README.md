# Source Code of Community Detection in Dynamic Networks - IncNSA #

The implementation of IncNSA: "[IncNSA: Detecting communities incrementally from time-evolving networks based on node similarity](https://www.worldscientific.com/doi/10.1142/S0129183120500941)".

***

If you find this method helpful for your research, please cite this paper.

    @article{su2020incnsa,  
          title={IncNSA: Detecting communities incrementally from time-evolving networks based on node similarity},  
          author={Su, Xing and Cheng, Jianjun and Yang, Haijuan and Leng, Mingwei and Zhang, Wenbo and Chen, Xiaoyun},  
          journal={International Journal of Modern Physics C},  
          volume={31},   
          number={07},  
          pages={2050094},  
          year={2020},  
          publisher={World Scientific}  
    } 

***

**Requirement**

The code of NSA has been tested running under Python 3.7.6, with the following packages installed (along with their dependencies):

- networkx == 2.4

***

**Data Format**

- The input data of each timestamp is in `.edgelist` format, in which each line contains two integers: source node id and target node id of an undirected edge. 
- The naming of the dynamic network datasets must begins at `1` and be continuous without suffix. For example, if a dynamic network contains 3 timestamps, their file names are `1`, `2`, `3`, respectively. 
- Synthetic dynamic networks are given as examples in `./syn_datasets` (generation of the synthetic networks refers to the paper). 

***

**How to Use**

1. **Initialization**: run `main1_initial.py` to initialize the network at the 1st time step. Here we use NSA algorithm (from paper "[Neighbor Similarity Based Agglomerative Method for Community Detection in Networks](https://www.hindawi.com/journals/complexity/2019/8292485/)") for initialization, other methods also can be ulitized to obtain the communities at the 1st time step. Paramaters setting in `main1_initial.py` is as follows (take dataset `birth_death` as example): 
 
        merge_ratio = 0.2  #The parameter of NSA, usually less than 0.3.  
        graph = nx.Graph(nx.read_edgelist("./syn_datasets/birth_death/birth_death_data/1")) # Path of input data at the 1st time step.  
        path = r'./syn_datasets/birth_death' # The file directory of a dataset that is the upper level directory of the input data, to save input data, groundtruth, evolving information, community results and evaluation results.   
        
2. **Detecting Communities Incrementally**: run `main2.py` to detecting communities in dynamic networks incrementally based on previous time step. Paramaters setting in `main1_initial.py` is as follows (take dataset `birth_death` as example): 

        n_stampt = 10 # The number of time steps. 
        path = r'./syn_datasets/birth_death' # The file directory of a dataset. 
        path_dataset = r'./syn_datasets/birth_death/birth_death_data' # The path of input data contains all time steps.  
        
        # The value of 'path' in main1_initial.py and main2.py must be the same, the value of 'path_dataset' which should keep the same upper level directory. 

***

**Output Files**
1. After running `main1_initial.py`, the community result of time step 1 can be obtain (see `./syn_datasets/birth_death/community/community1.txt` for example). 

2. After running `main2.py`, the the community results of all the time steps can be obtain. The output files include (take dataset `birth_death` as example):
    - `./syn_datasets/birth_death/community`: the results of communities. 
    - `./syn_datasets/birth_death/pre_inform`: evolution information of nodes and edges between the two consecutive time steps. 
    - `./syn_datasets/birth_death/Q.txt`: evaluation results by modularity.  

***

**Disclaimer**

If you find any bugs, please report them to me `xing.su2@hdr.mq.edu.au`.
