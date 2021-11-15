#############
# Libraries #
#############
import networkx as nx
import sys
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib

# Make matplotlib use a 'non-interactive' background
matplotlib.use('Agg') # was getting a "Could not connect to any X display" error

# # Load Hadean font
# from matplotlib import font_manager
# font_manager._rebuild()
# font = font_manager.get_font('/mnt/c/Users/crisp/AppData/Local/Microsoft/Windows/Fonts/proximaNova.ttf')
# prop = font_manager.FontProperties(fname='/mnt/c/Users/crisp/AppData/Local/Microsoft/Windows/Fonts/proximaNova.ttf')

# Hadean colour scheme
hadeanOrange = '#FF9448'
hadeanIndigo = '#27203B'
hadeanCoral = '#FF5C37'
hadeanCopper = '#D66444'

def AddTransparency(c,a):
    b = format(max(int(255*a),0),'02X')
    return c+str(b[-2:])

# Chris' functions 
def convert_imperial_network_edges_to_oxford_network_edges(network_data):
    network_data.rename(columns = {'a.index': 'ID_1', 'b.index': 'ID_2'}, inplace=True)
    return network_data

def convert_imperial_node_data_to_oxford_node_data(person_node_data, index_to_label_network_with):
    person_node_data.rename(columns = {'index': 'ID',
                                       'household.index': 'house_no',
                                       'age': 'age_group',
                                       'coord.x': 'x',
                                       'coord.y': 'y'}, inplace=True)

    person_node_data['network_no'] = (np.zeros(len(person_node_data)) + index_to_label_network_with)

    # Convert the age to age group (the decade age group of the person and is an integer between 0 (0-9 years) and 8 (80+).)
    person_node_data['age_group'] = person_node_data['age_group'].apply(lambda x: int(x / 10))

    #print(person_node_data) # CA remove

    return person_node_data

###################
# Load network(s) #
###################

p = sys.argv[1] #awfully hard coded

nodes_df = pd.read_csv(p+'_0_nodes.csv', comment="#", sep=",", skipinitialspace=True)
arcs_df = pd.read_csv(p+'_0_arcs.csv', comment="#", sep=",", skipinitialspace=True) # Different arcs, temp only use one

# Load positions into a different struct
nodes_pos = {nodes_df['index'][i]:[nodes_df['coord.x'][i],nodes_df['coord.y'][i]] for i in range(len(nodes_df))}
nodes_pos_x = {nodes_df['index'][i]:nodes_df['coord.x'][i] for i in range(len(nodes_df))}
nodes_pos_y = {nodes_df['index'][i]:nodes_df['coord.y'][i] for i in range(len(nodes_df))}

g = nx.Graph() # from_pandas_edgelist(arcs_df,'a.index','b.index',create_using=nx.Graph())
g.add_nodes_from(nodes_df['index'])

########
# Plot #
########

o = sys.argv[2] #output path

aNode = 1/2**7
aEdge = 1/2**7
print('Creating Figure...')
f = plt.figure(figsize=(20,10))
print('Drawing...')
nx.draw(g,pos=nodes_pos,node_size=5,edge_color=AddTransparency(hadeanOrange,aEdge),node_color=AddTransparency(hadeanIndigo,aNode),ax=f.add_subplot(111))
print('Saving figure...')
f.savefig(o)
