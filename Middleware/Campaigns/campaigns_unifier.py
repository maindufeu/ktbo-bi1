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
            if fnmatch.fnmatch(filename, '*sizmek*'):
                print(filename)
                df = pd.read_csv(filename, usecols = ['Campaign Name'])
                df = df['Campaign Name'].unique().tolist()
                sizmek.append(df)
                print("si")
                print(len(sizmek))

            elif fnmatch.fnmatch(filename, '*google*'):
                print(filename)
                df = pd.read_csv(filename, usecols = ['Campaign_duplicate'])
                df = df['Campaign_duplicate'].unique().tolist()
                google.append(df)
                print("go")
                print(len(google))

            elif fnmatch.fnmatch(filename, '*facebook*'):
                print(filename)
                df = pd.read_csv(filename, usecols = ['Temp Campaign Name'])
                df = df['Temp Campaign Name'].unique().tolist()
                facebook.append(df)
                print("fb")
                print(len(facebook))
######
fb = pd.DataFrame(facebook)
fb = fb[0].unique().tolist()
print(len(fb))

go = pd.DataFrame(google)
go = go[0].unique().tolist()
print(len(go))

si = pd.DataFrame(sizmek)
si = si[0].unique().tolist()
print("sizmek uniques")
print(len(si))

ot = pd.DataFrame(other)
ot = ot[0].unique().tolist()
print("otheruniques")
print(len(ot))

tw = pd.DataFrame(twitter)
tw = tw[0].unique().tolist()
print(len(tw))

c_unified = facebook + google + sizmek + twitter + other
print(len(facebook))
print(len(google))
print("sizmek")
print(len(sizmek))
print(len(twitter))
print("other")
print(len(other))
print("unida")
print(len(c_unified))
c_list = {'Campaign Name':c_unified}
c_list = pd.DataFrame(c_list, columns=['Campaign Name'])

c_list.to_csv("Campaigns/campaigns_unified.csv")

c_list = c_list[0].unique().tolist()
print("lista de campañas únicas:")
print(c_list)
print(len(c_unified))
