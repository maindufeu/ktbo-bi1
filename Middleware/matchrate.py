import glob
import match
import pandas as pd
import os
import fnmatch

path = 'Campaigns/**'
pattern = '*.csv'
mp_path = 'Campaigns/mp/'
listfiles = []
mpfiles = []
frames = []
mp_frames =[]

for filename in glob.iglob(path, recursive=True):
    if os.path.isfile(filename): # filter dirs
        if fnmatch.fnmatch(filename, pattern):
            if fnmatch.fnmatch(filename, mp_pattern):
                mpfiles.append(filename)
                df = pd.read_csv(filename)
                mp_frames .append(df)
            else:
                listfiles.append(filename)
                df = pd.read_csv(filename)
                frames.append(df)

mediafacts = pd.concat([df['Campaign', 'Datasource'] for df in frames], ignore_index=True)

mediaplans = pd.concat([df['Campaign', 'Datasource'] for df in mp_frames], ignore_index=True)
