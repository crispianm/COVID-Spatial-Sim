import sys

# Python function to write a grid params.in in the same fashion as the one provided
#   Arguments default to original values
def WriteGridParams(
    gridPath='./params/build_grid_params.in',
    intSeed=1234,
    dblHexagonWidth=0.001,
    intNoMaximalNodes=1,
    dblMaxSpatialNeighbours=100,
    blNetworkDumpFile=True,
    intBlockSizeInUnitsOfPointers=4096,
    dblAverageWorkplaceSize=150,
    strHouseholdAgeDistributionFile='./data/ons-hh-ages_modified_nocrisis.csv',
    intNoNodes=620000,
    dblAverageHousehold=2.4,
    strHouseholdDensityFile='./data/bristol.asc'
    ):
    with open(gridPath, "w") as text_file:
        text_file.write("[General setup]\n")
        text_file.write("\t intSeed\t1\t"+str(intSeed)+"\n")
        text_file.write("\t dblHexagonWidth\t1\t"+str(dblHexagonWidth)+"\t[radians]\t\n")
        text_file.write("\t intNoMaximalNodes\t1\t"+str(intNoMaximalNodes)+"\n")
        text_file.write("\t dblMaxSpatialNeighbours\t1\t"+str(dblMaxSpatialNeighbours)+"\n")
        text_file.write("\t blNetworkDumpFile\t0\t"+str(blNetworkDumpFile).upper()+"\n")
        text_file.write("\t intBlockSizeInUnitsOfPointers\t1\t"+str(intBlockSizeInUnitsOfPointers)+"\n")
        text_file.write("\t dblAverageWorkplaceSize\t1\t"+str(dblAverageWorkplaceSize)+"\n")
        text_file.write("\t strHouseholdAgeDistributionFile\t0\t"+str(strHouseholdAgeDistributionFile)+"\t[0]\t\n")
        text_file.write("\n[Household setup]\n")
        text_file.write("\t intNoNodes\t1\t"+str(intNoNodes)+"\t[584396,24881385]\t\n")
        text_file.write("\t dblAverageHousehold\t1\t"+str(dblAverageHousehold)+"\t[3.3]\n")
        text_file.write("\t strHouseholdDensityFile\t0\t"+str(strHouseholdDensityFile)+"\t[0]\t\n")

# Original Grid params file
'''
[General setup]
	intSeed 1 1234
	dblHexagonWidth	1	0.001	[radians]
	intNoMaximalNodes	1	1
	dblMaxSpatialNeighbours	1	100
	blNetworkDumpFile	0	TRUE
	intBlockSizeInUnitsOfPointers	1	4096
	dblAverageWorkplaceSize	1	150
	strHouseholdAgeDistributionFile 0 ../../data/ons-hh-ages.csv [0]

[Household setup]			
	intNoNodes	1	700000	[584396,24881385]
	dblAverageHousehold	1	2.4	[3.3]
	strHouseholdDensityFile	0	data/bristol_2020_30_sec.asc
'''



def WriteStrataParmas(
    strataPath='./params/build_strata_params.in',
    noIterations=1,
    strStrataProportionsFile='data/workplace_strata_distribution'
    ):
    with open(strataPath, "w") as text_file:
        text_file.write("[Strata Parameters]\n")
        text_file.write("\t noIterations\t1\t"+str(noIterations)+"\n")
        text_file.write("\t strStrataProportionsFile\t0\t"+str(strStrataProportionsFile)+"\n")

'''
[Strata Parameters]
	noIterations 1 1
	strStrataProportionsFile	0	data/workplace_strata_distribution
'''


def WriteNetworkParams(
    networkPath='./params/build_network_params.in',
    dblPropColleguesInNetwork=0.1,
    strWorkplaceDensityFile='./data/bristol.asc',
    dblDistanceAllWorkplacesHistDx=10,
    dblDistanceAllWorkplacesGridDx=5,
    intMCMCMaxSamplesInMillions=512,
    dblMCMCProportionResample=0.3,
    dblMCMCGridSize=1,
    dblWeightMCMCUpdateLocal=0.9,
    Commute_Power_One_GZ=2.29,
    Commute_Change_Point_GZ=1,
    Commute_Power_One_HK=2.29,
    Commute_Change_Point_HK=1,
    Constant_Generate_Spatial_Neighbour=0,
    Decay_Generate_Spatial_Neighbour=0.75,
    Prob_Generate_Spatial_Neighbour=0,
    Offset_Generate_Spatial_Neighbour=0,
    Cutoff_Distance_Generate_Spatial_Neighbour=0.01,
    intMaxNeighbourEvents=1000,
    intSetupKernelStackSize=200
    ):
    with open(networkPath, "w") as text_file:
        text_file.write("[Workplace setup]\n")
        text_file.write("\t dblPropColleguesInNetwork\t1\t"+str(dblPropColleguesInNetwork)+"\n")
        text_file.write("\t strWorkplaceDensityFile\t0\t"+str(strWorkplaceDensityFile)+"\n")
        text_file.write("\t dblDistanceAllWorkplacesHistDx\t1\t"+str(dblDistanceAllWorkplacesHistDx)+"\n")
        text_file.write("\t dblDistanceAllWorkplacesGridDx\t1\t"+str(dblDistanceAllWorkplacesGridDx)+"\n")
        text_file.write("\t intMCMCMaxSamplesInMillions\t1\t"+str(intMCMCMaxSamplesInMillions)+"\n")
        text_file.write("\t dblMCMCProportionResample\t1\t"+str(dblMCMCProportionResample)+"\n")
        text_file.write("\t dblMCMCGridSize\t1\t"+str(dblMCMCGridSize)+"\n")
        text_file.write("\t dblWeightMCMCUpdateLocal\t1\t"+str(dblWeightMCMCUpdateLocal)+"\n")
        text_file.write("\n[Commuting distribution]\n")
        text_file.write("\t Commute_Power_One_GZ\t1\t"+str(Commute_Power_One_GZ)+"\n")
        text_file.write("\t Commute_Change_Point_GZ\t1\t"+str(Commute_Change_Point_GZ)+"\n")
        text_file.write("\t Commute_Power_One_HK\t1\t"+str(Commute_Power_One_HK)+"\n")
        text_file.write("\t Commute_Change_Point_HK\t1\t"+str(Commute_Change_Point_HK)+"\n")
        text_file.write("\n[Spatial neighbour generation - Currently Unused]\n")
        text_file.write("\t Constant_Generate_Spatial_Neighbour\t1\t"+str(Constant_Generate_Spatial_Neighbour)+"\n")
        text_file.write("\t Decay_Generate_Spatial_Neighbour\t1\t"+str(Decay_Generate_Spatial_Neighbour)+"\n")
        text_file.write("\t Prob_Generate_Spatial_Neighbour\t1\t"+str(Prob_Generate_Spatial_Neighbour)+"\n")
        text_file.write("\t Offset_Generate_Spatial_Neighbour\t1\t"+str(Offset_Generate_Spatial_Neighbour)+"\n")
        text_file.write("\t Cutoff_Distance_Generate_Spatial_Neighbour\t1\t"+str(Cutoff_Distance_Generate_Spatial_Neighbour)+"\n")
        text_file.write("\t intMaxNeighbourEvents\t1\t"+str(intMaxNeighbourEvents)+"\n")
        text_file.write("\t intSetupKernelStackSize\t1\t"+str(intSetupKernelStackSize)+"\n")


'''
[Workplace setup]			
	dblPropColleguesInNetwork	1	0.1
	strWorkplaceDensityFile	0	data/bristol_2020_30_sec.asc
	dblDistanceAllWorkplacesHistDx	1	10
	dblDistanceAllWorkplacesGridDx	1	5
	intMCMCMaxSamplesInMillions	1	512
	dblMCMCProportionResample	1	0.3
	dblMCMCGridSize	1	1
	dblWeightMCMCUpdateLocal	1	0.9

[Commuting distribution]			
	Commute_Power_One_GZ	 1	2.29
	Commute_Change_Point_GZ	1	3.47
	Commute_Power_One_HK	 1	2.29
	Commute_Change_Point_HK	1	3.47

[Spatial neighbour generation - Currently Unused]			
	Constant_Generate_Spatial_Neighbour	1	0
	Decay_Generate_Spatial_Neighbour 	1	0.75
	Prob_Generate_Spatial_Neighbour	1	0
	Offset_Generate_Spatial_Neighbour	1	0
	Cutoff_Distance_Generate_Spatial_Neighbour	1	0.01
	intMaxNeighbourEvents	1	1000
	intSetupKernelStackSize	1	200
'''

########
# Main #
########
# Need to work out how to give arguments to python to sometimes supercede defaults
# **{} works!!!
# e.g. **{'noIterations':100} ... GENIUS

gridParamNames = [
    'gridPath',
    'intSeed',
    'dblHexagonWidth',
    'intNoMaximalNodes',
    'dblMaxSpatialNeighbours',
    'blNetworkDumpFile',
    'intBlockSizeInUnitsOfPointers',
    'dblAverageWorkplaceSize',
    'strHouseholdAgeDistributionFile',
    'intNoNodes',
    'dblAverageHousehold',
    'strHouseholdDensityFile',
    'gridArgs'
]
gridArgs = {}

strataParamNames = [
    'strataPath',
    'noIterations',
    'strStrataProportionsFile'
    ]
strataArgs = {}

networkParamNames = [
    'networkPath',
    'dblPropColleguesInNetwork',
    'strWorkplaceDensityFile',
    'dblDistanceAllWorkplacesHistDx',
    'dblDistanceAllWorkplacesGridDx',
    'intMCMCMaxSamplesInMillions',
    'dblMCMCProportionResample',
    'dblMCMCGridSize',
    'dblWeightMCMCUpdateLocal',
    'Commute_Power_One_GZ',
    'Commute_Change_Point_GZ',
    'Commute_Power_One_HK',
    'Commute_Change_Point_HK',
    'Constant_Generate_Spatial_Neighbour',
    'Decay_Generate_Spatial_Neighbour',
    'Prob_Generate_Spatial_Neighbour',
    'Offset_Generate_Spatial_Neighbour',
    'Cutoff_Distance_Generate_Spatial_Neighbour',
    'intMaxNeighbourEvents',
    'intSetupKernelStackSize'
]
networkArgs = {}


for a in sys.argv[1:]:
    x = a.split('=')[0]
    y = a.split('=')[1]
    if x in gridParamNames: gridArgs[x]=y
    elif x in strataParamNames: strataArgs[x]=y
    elif x in networkParamNames: networkArgs[x]=y
    else: print(str(x)+' is not taken by grid, strata, or network parameter files')


WriteGridParams(**gridArgs)
WriteStrataParmas(**strataArgs)
WriteNetworkParams(**networkArgs)

print("\nDone!")