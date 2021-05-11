import pandas as pd
import glob
import os
import fnmatch



other = pd.read_excel("othercampaigns/acumulado_other.xlsx", usecols = ['Campaign'])
twitter = pd.read_excel("twitter/acumulado_twitter.xlsx", usecols = ['Campaign'])
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
listfiles = []
mpfiles = []
frames = []
mp_frames =[]

for filename in glob.iglob(path, recursive=True):
    if os.path.isfile(filename): # filter dirs
        if fnmatch.fnmatch(filename, pattern):
            print(filename)
            df = pd.read_csv(filename)
            print(df.columns)
######

#for filename in glob.iglob(path, recursive=True):
#    if os.path.isfile(filename): # filter dirs
#        if fnmatch.fnmatch(filename, pattern):
#            google = pd.read_csv('google/{i}', usecols=['Campaign_duplicate'])
#            google = google.unique().tolist()
#            print("Googleleght:")
#            print(len(google))

#facebook = pd.read_csv("google/409571_adwords_adwords-143-20210427-94eedaa01640429a86addf575c77449a.csv")


#print(len(c_unified))
