import uproot as rt
import pandas as pd 
import matplotlib as pyplot 
import awkward as ak 
infile_name = 'DataEgamma.root' #only works if data file is in venv 
file = rt.open(infile_name) #opening the dataset 
file.keys() #to see the TTrees; this data set only has 1 tree
tree = file["mini;1"] #shows bracnhes
df = tree.arrays(library = "pd") #creates a dataframe to view everything 
df_relevant = df[['lep_pt','lep_eta','lep_phi','lep_charge','lep_E','lep_type']] #a dataframe that pulls only the relevant variables for mass reconstruction; might have to include more later to help with reducing noise



