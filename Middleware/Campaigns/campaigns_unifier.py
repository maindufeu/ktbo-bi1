import pandas as pd
import glob
import os
import fnmatch



other = pd.read_excel("Campaigns/othercampaigns/acumulado_other.xlsx", usecols = ['Campaign'])
twitter = pd.read_excel("Campaigns/twitter/acumulado_twitter.xlsx", usecols = ['Campaign'])
twitter = twitter['Campaign'].str.upper().str.strip(" ").unique().tolist()
print("Twitter length:")
print(len(twitter))

other = other['Campaign'].str.upper().str.strip(" ").unique().tolist()
print("Other Campaigns length:")
print(len(other))

path = 'google/*'
pattern = '*.csv'

########
path = 'Campaigns/**'
pattern = '*.csv'
mp_path = 'Mediaplan/mp_processed'
sizmek = []
google = []
facebook = []
mpfiles = []
mp_frames =[]

for filename in glob.iglob(path, recursive=True):
    if os.path.isfile(filename): # filter dirs
        if fnmatch.fnmatch(filename, pattern):
            if fnmatch.fnmatch(filename, '/.*sizmek.*/'):
                print(filename)
                df = pd.read_csv(filename, usecols = ['Campaign Name'])
                df = df['Campaign Name'].unique().tolist()
                sizmek.append(df)
                print(sizmek)

            elif fnmatch.fnmatch(filename, '/.*google.*/'):
                print(filename)
                df = pd.read_csv(filename, usecols = ['Campaign Name'])
                df = df['Campaign Name'].unique().tolist()
                sizmek.append(df)
                print(google)

            elif fnmatch.fnmatch(filename, '/.*facebook.*/'):
                print(filename)
                df = pd.read_csv(filename, usecols = ['Campaign Name'])
                df = df['Campaign Name'].unique().tolist()
                sizmek.append(df)
                print(facebook)
######

import numpy as np

# function to get unique values
def unique(list1):
    x = np.array(list1)
    print(np.unique(x))

c_unified = facebook + google + sizmek + twitter + other
c_unified = unique(c_unified)
print(len(c_unified))
