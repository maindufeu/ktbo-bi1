import glob
import pandas as pd
import os
import fnmatch

path = 'Campaigns/**'
pattern = '*.csv'
listfiles = []
frames = []

for filename in glob.iglob(path, recursive=True):
    if os.path.isfile(filename): # filter dirs
        if fnmatch.fnmatch(filename, pattern):
            filename = re.split('\', filename)[1]
            listfiles.append(filename)
            df = pd.read_csv(filename)
            frames.append(df)

mediafacts = pd.concat([df['Campaign', 'Datasource'] for df in frames], ignore_index=True)
