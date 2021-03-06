import glob
import match
import pandas as pd
import os
import csv
import fnmatch
import datetime

path = 'Campaigns/**'
pattern = '*.csv'
mp_path = 'Mediaplan/mp_processed'
listfiles = []
mpfiles = []
frames = []
mp_frames =[]

for filename in glob.iglob(path, recursive=True):
    if os.path.isfile(filename): # filter dirs
        if fnmatch.fnmatch(filename, pattern):
                listfiles.append(filename)
                df = pd.read_csv(filename)
                frames.append(df)

for filename in glob.iglob(mp_path, recursive=True):
    if os.path.isfile(filename): # filter dirs
        if fnmatch.fnmatch(filename, pattern):
            mpfiles.append(filename)
            df = pd.read_csv(filename)
            mp_frames.append(df)

#mediafacts = pd.concat([df['Campaign', 'Datasource'] for df in frames], ignore_index=True)
#mediafacts = pd.read_csv('Campaigns/adverity-export_sftp.csv')
mediafacts = pd.read_csv('Campaigns/campaigns_unified.csv')

#mediaplans = pd.concat([df['Campaign', 'Datasource'] for df in mp_frames], ignore_index=True)
mediaplans =  pd.read_csv('Mediaplan/mp_processed/Adverity-export_Plan.csv')

print('Mediaplan')
print(mediaplans)

print('Mediafacts')
print(mediafacts)

mr = match.mp_match(mediaplans, mediafacts)
print(mr)


#file = open('unmatched.csv', 'w+', newline ='')
#write = csv.writer(file)
#write.writerows(mr)
