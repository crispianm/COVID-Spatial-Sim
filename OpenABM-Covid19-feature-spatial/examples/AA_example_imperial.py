#!/usr/bin/env python
# coding: utf-8

# # Preliminaries

# ## Libraries

# In[ ]:


import example_utils as utils
import pandas as pd
import os
import numpy as np
import matplotlib.pyplot as plt
from tqdm.notebook import tqdm
import networkx as nx


# ## Hadean Colour scheme
# But feel free to choose your own.

# In[ ]:


# Hadean colour scheme
hadeanOrange = '#FF9448'
hadeanIndigo = '#27203B'
hadeanCoral = '#FF5C37'
hadeanCopper = '#D66444'
uranianBlue = '#AFDBF5'


# In[ ]:


def AddTransparency(c,a):
    b = format(max(int(255*a),0),'02X')
    return c+str(b[-2:])


# ## Chris' Imperial functions

# In[ ]:


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


# ## Very-much-draft Coordinate functions

# In[ ]:


def coord2ll(x,y):
    return np.array([y,x]) * 57.2957795131

def ll2coord(long,lat):
    return np.array([lat,long]) / 57.2957795131


# ## Load Networks

# In[ ]:


##########################
# Load Network Functions #
##########################

# Take path of _nodes.csv
def LoadDemographics(demoPath):
    df_household_demographics = pd.read_csv(demoPath, comment="#", sep=",", skipinitialspace=True)
    # Converting we use network_no=0, as that's for household network
    df_household_demographics = convert_imperial_node_data_to_oxford_node_data(df_household_demographics,0)
    return df_household_demographics

def CoordsFromDemo(df_household_demographics):
    df_coordinates = df_household_demographics.rename(columns={'x':'xcoords','y':'ycoords'})[['ID','xcoords','ycoords']]
    return df_coordinates

def LoadOccupationNetworks(projPath,prefix='leicestershire'):
    ocNetworksArcs_df_dict = {}
    ocNetworksArcs_colNames = ['ID_1','a.x','a.y','ID_2','b.x','b.y']
    network_name = np.array(['primary', 'secondary', 'general_workforce', 'retired', 'elderly'])

    # Can find network assignment by the a.index for each _i_arcs.csv
    for i,x in enumerate(tqdm(network_name)):
        print([i,x])
        ocNetworksArcs_df_dict[x] = pd.read_csv(projPath+'/'+prefix+"_"+str(i)+"_arcs.csv", comment="#", sep=",", skipinitialspace=True)
        ocNetworksArcs_df_dict[x].columns = ocNetworksArcs_colNames
    
    return ocNetworksArcs_df_dict

###################
# Parameter stuff #
###################

def LoadParams(df_household_demographics,params=None):
    if params == None:
        params = utils.get_baseline_parameters()
    n_total = len(df_household_demographics["ID"])
    params.set_param("n_total",n_total)
    params.set_demographic_household_table(df_household_demographics)
    return params

def LoadNetworks(model,ocNetworksArcs_df_dict,daily_fration=0.5):
    for i,net in enumerate(ocNetworksArcs_df_dict):
        model.delete_network(model.get_network_by_id(i+2))
        model.add_user_network(ocNetworksArcs_df_dict[net],name=net,daily_fraction=daily_fration)

def ImperialNetwork(netPath,n_infect=10,prefix='leicestershire'):
    df_household_demographics = LoadDemographics(netPath+'/'+prefix+'_0_nodes.csv')
    df_coordinates = CoordsFromDemo(df_household_demographics)
    ocNetworksArcs_df_dict = LoadOccupationNetworks(netPath)
    params = LoadParams(df_household_demographics)
    params.set_param("n_seed_infection",n_infect)
    model = utils.get_simulation( params ).env.model
    model.assign_coordinates_individuals(df_coordinates)
    LoadNetworks(model,ocNetworksArcs_df_dict)
    return model


# # Visualise Network

# In[ ]:


statuses2Track = [1,2,3,4,5,6,7,8,20] # In model.py, v. difficult to find
statuses2Track = [4,5]

def Infected(model):
    x = model.get_individuals()
    x = x.loc[x['current_status'].isin(statuses2Track)]
    return list(x['ID'])


# In[ ]:


# scarrily current_status does not seem to change when quarantined
def Lockdowned(model):
    x = model.get_individuals()
    print(x.columns.tolist())

    x = x.loc[x['quarantined'] == 1]
    return list(x['ID'])


# In[ ]:


def VisualiseNetwork(model,ax,aNode = 1/2**7,aEdge = 1/2**7):
    nodes = model.get_individuals()
    nodes_pos = {nodes['ID'][i]:[nodes['xcoords'][i],nodes['ycoords'][i]] for i in range(len(nodes))}
    infected = Infected(model)
    quarantined = Lockdowned(model)
    g = nx.Graph()
    #g = nx.from_pandas_edgelist(ocNetworksArcs_df_dict['primary'],'ID_1','ID_2',create_using=nx.Graph())
    g.add_nodes_from(nodes['ID'])
    g_infected = nx.subgraph(g,infected)
    g_quarantined = nx.subgraph(g,quarantined)
    #f,ax = plt.subplots(figsize=(20,10))
    nx.draw(g,pos=nodes_pos,node_size=5,edge_color=AddTransparency(hadeanOrange,aEdge),node_color=AddTransparency(hadeanIndigo,aNode),ax=ax)
    nx.draw_networkx_nodes(g_quarantined,pos=nodes_pos,node_size=5,node_color=AddTransparency(uranianBlue,0.02),ax=ax)
    nx.draw_networkx_nodes(g_infected,pos=nodes_pos,node_size=5,node_color=AddTransparency(hadeanOrange,0.9),ax=ax)


# In[ ]:


net_dir = "../../id_spatial_sim/scenarios/mdm3_scenario/output/networks"
model = ImperialNetwork(net_dir)
f,ax = plt.subplots(figsize=(20,10))
VisualiseNetwork(model,ax)


# In[ ]:


n = 64
aNode = 1/2**7
aEdge = 1/2**7
gif_out = '../../NetworkData/NewForestGIF/all/'


# In[ ]:


from matplotlib.lines import Line2D

# Run several time-steps and produce many PNGs to be converted to a GIF
def RunSim(model,out_dir=gif_out,n=64,title_text='Spread of covid19 on an artificial network of the New Forest'):
    for i in tqdm(range(n)):
        f,ax = plt.subplots(figsize=(20,10))
        t = model.one_time_step_results()['time']
        VisualiseNetwork(model,ax)
        plt.title(title_text,fontsize=32)
        agentPatch = Line2D([0],[0],marker='o',linestyle='none',color=AddTransparency(hadeanIndigo,aNode),label='Agent')
        conPatch = Line2D([0],[0],marker='o',linestyle='none',color=AddTransparency(hadeanOrange,0.9),label='Contagious')
        lg1 = plt.legend(handles=[agentPatch,conPatch],fontsize=16)
        text = "Time = "+"{:04d}".format(t)
        textPatch = Line2D([0],[0],linestyle='none',label=text)
        ax.legend(handles=[textPatch],loc='lower left',frameon=False)
        ax.add_artist(lg1)
        print(out_dir+"{:04d}".format(t)+'.png')
        f.savefig(out_dir+"{:04d}".format(t)+'.png')
        model.one_time_step()
        ax.clear()
        plt.clf()
    
# Then use a `convert ./out_dir/*.png ./net.gif` from terminal


# # Seeding
# For the New Forest.

# In[ ]:


# replace bc4 with the coords of your desired location
long,lat = coord2ll(1.0,-.1)
x,y = ll2coord(long,lat)
bc4 = [50.75328904, -1.55764306]
bc4_x, bc4_y = ll2coord(bc4[0],bc4[1])
bc4_xy = np.array([bc4_x,bc4_y])
print([bc4_x, bc4_y])


# In[ ]:


model = ImperialNetwork(net_dir)
df_indiv = model.get_individuals()


# In[ ]:


d = np.linalg.norm
df_indiv['d'] = d(df_indiv[['xcoords','ycoords']]-bc4_xy,axis=1)


# In[ ]:


mind = df_indiv['d'].idxmin()
print(mind)
bc4_house = int(df_indiv.iloc[mind]['house_no'])
print(df_indiv.iloc[mind])
print(coord2ll(df_indiv.iloc[mind]['xcoords'],df_indiv.iloc[mind]['ycoords']))


# In[ ]:


coord2ll(df_indiv.iloc[mind]['xcoords'],df_indiv.iloc[mind]['ycoords'])


# In[ ]:


df_indiv.loc[df_indiv['house_no']==bc4_house]


# In[ ]:


bc4_indivs = [x for x in list(df_indiv.loc[df_indiv['house_no']==bc4_house]['ID'])]
bc4_indivs


# In[ ]:


for i in bc4_indivs:
    model.seed_infect_by_idx(i)


# In[ ]:


f,ax = plt.subplots(figsize=(20,10))
VisualiseNetwork(model,ax)


# In[ ]:


RunSim(model,n=63)


# In[ ]:


bc4 = [50.75328904, -1.55764306]
bc4_x, bc4_y = ll2coord(bc4[0],bc4[1])
bc4_xy = np.array([bc4_x,bc4_y])
print(bc4)
print(bc4_xy)


# In[ ]:


d = np.linalg.norm
df_indiv['d'] = d(df_indiv[['xcoords','ycoords']]-bc4_xy,axis=1)
mind = df_indiv['d'].idxmin()
print(mind)
bc4_house = int(df_indiv.iloc[mind]['house_no'])
print(bc4_house)


# In[ ]:


def RadiusIndividual(model,target,r,d=np.linalg.norm):
    x = model.get_individuals()
    x['d'] = d(x[['xcoords','ycoords']]-target,axis=1)
    x = x.loc[x['d']<=r]
    return list(x['ID'])


# In[ ]:


Lockdowned(model)


# In[ ]:


bc4_indivs[-1]


# In[ ]:


RadiusIndividual(model,bc4_xy,.00001)


# In[ ]:


ev = [50.74722149271622, -1.5903702505310746]


# In[ ]:


bc4


# In[ ]:


r2halfkm = np.linalg.norm(np.array(ll2coord(bc4[0],bc4[1]))-np.array(ll2coord(ev[0],ev[1]))) #3.5km
r2halfkm


# In[ ]:


len(RadiusIndividual(model,bc4_xy,r2halfkm))


# In[ ]:


def LockdownInRadius(model,target,r,n=14):
    indivs = model.get_individuals()
    indivs = RadiusIndividual(model,target,r)
    t = model.one_time_step_results()['time']
    for i in indivs:
        model.intervention_quarantine_until_by_idx(i,None,t+n,0)


# In[ ]:


# GIF without local lockdown
model = ImperialNetwork()
for i in bc4_indivs:
    model.seed_infect_by_idx(i)
RunSim(model,n=64)


# In[ ]:


# GIF WITH local lockdown
gif_out = '../../NetworkData/NewForestGIF/all_2/'
model = ImperialNetwork()
for i in bc4_indivs:
    model.seed_infect_by_idx(i)
RunSim(model,out_dir=gif_out,n=6)
LockdownInRadius(model,bc4_xy,r2halfkm*2,n=21)
RunSim(model,out_dir=gif_out,n=64-6)

