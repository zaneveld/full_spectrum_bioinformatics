from __future__ import division

"""
This script simulates a random biological network
and includes code for NetworkNode objects

"""
from random import random
from copy import copy
from numpy.random import choice 
import matplotlib.pyplot as plt
from numpy import linspace

class NetworkNode(object):
    """A network node"""
    def __init__(self,edges=None,name=None,metadata={}):
        """initialize a NetworkNode object
        edges -- a list of NetworkNode objects symmetrically
          connected to self
        name -- the name of the node as a str
        metadata -- a dictionary of metadata about the node
        """
        self.Edges = []
        if edges:
            self.Edges = edges
            #assuming a symmetrical network,
            #so self is an edge of each neighbor
            for neighbor in self.Edges:
                neighbor.addEdge(self)         
        #Why not just self.Edges = edges?
        #default parameter values are created once
        #so that would sneakily make all nodes
        #share the same edge list!
        self.Name = name
        self.Metadata = copy(metadata)
         
    def degree(self):
        """Returns the degree of the node"""
        result = len(self.Edges)  
        return result
    
    def addEdge(self,other):
        """Add an edge between self and another node"""
        if other not in self.Edges:
            self.Edges.append(other)
    
    def asString(self,field_delimiter="\t",list_delimiter=","):
        """Represent the node object as a string of name,edges,properties"""
        name = str(self.Name)
        edges = list_delimiter.join(map(str,[e.Name for e in self.Edges]))
        metadata = []
        for k,v in self.Metadata.items():
            metadata.append(":".join([k,v])) 
        metadata_str = list_delimiter.join(metadata)
        data_fields = field_delimiter.join([name,edges,metadata_str])+"\n"
        
        return data_fields
         
        

class Network(object):
    """A Network graph"""
    def __init__(self,nodes=None):
        """Generate network from nodes"""
        self.Nodes = []
        if nodes:
            self.Nodes = copy(nodes)
            
    def degree(self):
        """Return a dict of node name:node degree"""
        return {n.Name:n.degree() for n in self.Nodes}

    def addNode(self,node):
        """Add a NetworkNode object to the network"""
        self.Nodes.append(node)
    
    def asString(self):
        result = []
        for n in self.Nodes:
            result.append(n.asString())
        return "".join(result)
    
    def enumerateNodePairIndices(self,skip_self_pairs=True):
        n_Nodes = len(self.Nodes)        
        for i in range(n_Nodes):
            for j in range(n_Nodes):
                if skip_self_pairs and i==j:
                    continue

                yield i,j

    def connectNodesRandom(self,p):
        """Randomly add edges between all node pairs with uniform probability p
        p -- the probability that two nodes will be connected  
        """
        for i,j in self.enumerateNodePairIndices():
            #Don't add edges between node
            #and itself
            if i == j:
                continue
            
            if random() <= p:
                self.Nodes[i].addEdge(self.Nodes[j])          
                self.Nodes[j].addEdge(self.Nodes[i])

    def plot(self,outfile="network.png",x_attr=None,y_attr=None,\
        x_max=300.0,y_max=300.0):
        """Save a network plot
        x_attr -- metadata key to use for x locations
        y_attr -- metadata key to use for y locations
        """   
        #Plot nodes as a scatterplot 
        x_coords = []
        y_coords = []
        for i,node in enumerate(self.Nodes):
            if x_attr is not None:
                x = float(node.Metadata.get(x_attr))
            else:
                x = random() * x_max
           
            if y_attr is not None:
                y = float(node.Metadata.get(y_attr))
            else:    
                y = random() * y_max
            
            x_coords.append(x)        
            y_coords.append(y)  
        
        fig, ax = plt.subplots()
        ax.plot(x_coords, y_coords, 'ro')
        for i,j in self.enumerateNodePairIndices():
            n1 = self.Nodes[i]
            n2 = self.Nodes[j]
            #Assume undirected
            if n1 in n2.Edges or n2 in n1.Edges:        
                start_x = x_coords[i]
                start_y = y_coords[i]
                end_x = x_coords[j]                
                end_y = y_coords[j]
                ax.plot([start_x,end_x],[start_y,end_y],'k-',alpha=0.50)
        plt.savefig(outfile)

def barbasi_albert_random_network(desired_size):
    """Generate a Barbasi-Albert random network
    desired_size -- desired number of nodes (integer)
    """
    #Seed a minimal start network of two 
    #*connected* nodes
    network = Network()
    network.addNode(NetworkNode(name="1"))
    network.addNode(NetworkNode(name="2"))
    n0,n1 = network.Nodes
    n0.addEdge(n1)
    n1.addEdge(n0)

    current_size = len(network.Nodes)
    curr_node_name = 2 
    #Repeatedly add nodes until network is the right size
    while len(network.Nodes) < desired_size:
        total_degree = sum([n.degree() for n in network.Nodes])
        node_weights = [float(n.degree())/total_degree for n in network.Nodes]
        #Pick a location to attach new node, using weighted random 
        #Note the result is an array with 1 element, so the [0]
        #accesses the chosen node
        attachment_node = choice(network.Nodes,1,p=node_weights)[0]
        new_node = NetworkNode(name=curr_node_name,edges = [attachment_node])
        network.addNode(new_node)     
        attachment_node.addEdge(new_node)
        curr_node_name +=1
    return network 

def erdos_renyi_random_network(n,p):
    """Define a random Erdos-Renyi network with n nodes
    n - number of nodes
    p - probability any pair of nodes is connected
    """
    #Generate nodes
    network = Network()
    for i in range(n):
        curr_node = NetworkNode(name=i)
        network.addNode(curr_node)
    #Connect nodes
    #Note the function doesn't need to return anything
    #as the Node objects are modified 'in place' rather
    #than copied.
    network.connectNodesRandom(p)
    
    return network

def plot_multiple_histogram(datasets,colors,labels,outfile):
    """Plot a multiple histogram of several datasets
    datasets -- list of data
    colors -- list of colors
    outfile -- file location to save histogram
    """
    fontsize = 16 
    if len(colors) < len(datasets):
        raise ValueError("Need to specify one color per dataset")

    if len(labels) < len(datasets):
        raise ValueError("Need to specify one label per dataset")
    fig,ax = plt.subplots()
    all_data = []
    for d in datasets:
        all_data.extend(d)
    max_val = max(map(int,all_data))
    bins = linspace(0,max_val,15) 
    plt.xlabel("Value",fontsize=fontsize)
    plt.ylabel("Frequency",fontsize=fontsize)
    common_params={'histtype':'stepfilled','alpha':0.50,'normed':True,'bins':bins}
    print("Plotting histogram")
    for i,dataset in enumerate(datasets):
        plt.hist(dataset,facecolor=colors[i],label=labels[i],**common_params)
   
    plt.legend(fontsize=fontsize) 
    plt.savefig(outfile)  


if __name__ == "__main__":
    graph_outfile1 = "erdos_renyi_network.png"
    data_outfile1 = "erdos_renyi_network.tab"
    graph_outfile2 = "barbasi_alberts_network.png"
    data_outfile2 = "barbasi_alberts_network.tab"
    histogram_outfile = 'histogram.png'
    n_nodes = 300
    er_p = 0.015
    er_network = erdos_renyi_random_network(n_nodes,er_p)
    print("Generating Erdos-Renyi network %f" %(0.015))
    network_datafile = open(data_outfile1,"w+")
    
    er_node_degrees = sorted(er_network.degree().values())
    
    data = er_network.asString()
    network_datafile.write(data)
    network_datafile.close()
    er_network.plot(graph_outfile1)

    print("Generating Barbasi-Albert network")
    ba_network = barbasi_albert_random_network(n_nodes)
     
    ba_node_degrees = sorted(ba_network.degree().values())
    
    network_datafile = open(data_outfile2,"w+")
    data = ba_network.asString()
    network_datafile.write(data)
    network_datafile.close()
    ba_network.plot(graph_outfile2)
 
    plot_multiple_histogram([ba_node_degrees,er_node_degrees],\
      colors = ['cyan','orange'],labels=["Barbasi-Alberts","Erdos-Renyi"],\
      outfile=histogram_outfile)

   def plot(self,outfile="network.png",x_attr=None,y_attr=None,\
        x_max=300.0,y_max=300.0):
        """Save a network plot
        x_attr -- metadata key to use for x locations
        y_attr -- metadata key to use for y locations
        """
        #Plot nodes as a scatterplot 
        x_coords = []
        y_coords = []
        for i,node in enumerate(self.Nodes):
            if x_attr is not None:
                x = float(node.Metadata.get(x_attr))
            else:
                x = random() * x_max

            if y_attr is not None:
                y = float(node.Metadata.get(y_attr))
            else:
                y = random() * y_max

            x_coords.append(x)
            y_coords.append(y)

        fig, ax = plt.subplots()
        ax.plot(x_coords, y_coords, 'ro')
        for i,j in self.enumerateNodePairIndices():
            n1 = self.Nodes[i]
            n2 = self.Nodes[j]
            #Assume undirected
            if n1 in n2.Edges or n2 in n1.Edges:
                start_x = x_coords[i]
                start_y = y_coords[i]
                end_x = x_coords[j]
                end_y = y_coords[j]
                ax.plot([start_x,end_x],[start_y,end_y],'k-',alpha=0.50)
        plt.savefig(outfile)
 
