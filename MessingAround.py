import uproot as rt
import pandas as pd 
import matplotlib as pyplot 
import awkward as ak 
infile_name = 'DataEgamma.root' #only works if data file is in venv 
file = rt.open(infile_name) #opening the dataset 
file.keys() #to see the TTrees; this data set only has 1 tree
tree = file["mini;1"] #shows bracnhes
df = tree.arrays(library = "pd") 
df.head()
