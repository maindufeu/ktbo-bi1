import pandas as pd
import glob
import os
import fnmatch
import subprocess


other = pd.read_excel("Campaigns/othercampaigns/acumulado_other.xlsx", usecols = ['Campaign'])
twitter = pd.read_excel("Campaigns/twitter/acumulado_twitter.xlsx", usecols = ['Campaign'])

twitter = twitter['Campaign'].str.upper().str.strip(" ").unique().tolist()
tw =pd.DataFrame({'Campaign Name':twitter})
print("Twitter length:")
print(len(twitter))

other = other['Campaign'].str.upper().str.strip(" ").unique().tolist()
ot = pd.DataFrame({'Campaign Name':other})
print("Other Campaigns length:")
print(len(other))

########
path = 'Campaigns/**'
pattern = '*.csv'

sizmek = []
google = []
facebook = []

si_df = pd.DataFrame(({'Campaign Name' : []}))
fb_df = pd.DataFrame(({'Campaign Name' : []}))
go_df = pd.DataFrame(({'Campaign Name' : []}))


for filename in glob.iglob(path, recursive=True):
    if os.path.isfile(filename): # filter dirs
        if fnmatch.fnmatch(filename, pattern):
            if fnmatch.fnmatch(filename, '*sizmek*'):
                print(filename)
                si = pd.read_csv(filename, usecols = ['Campaign Name'])
                si.columns = ['Campaign Name']
                si_l = si['Campaign Name'].unique().tolist()
                sizmek.append(si_l)
                si_df = pd.concat([si_df, si])
                print("si")
                print(len(sizmek))

            elif fnmatch.fnmatch(filename, '*google*'):
                print(filename)
                go = pd.read_csv(filename, usecols = ['Campaign'])
                go.columns = ['Campaign Name']
                go_l = go['Campaign Name'].unique().tolist()
                google.append(go_l)
                go_df = pd.concat([go_df, go])
                print("go")
                print(len(google))

            elif fnmatch.fnmatch(filename, '*facebook*'):
                print(filename)
                fb = pd.read_csv(filename, usecols = ['Temp Campaign Name'])
                fb.columns = ['Campaign Name']
                fb_l = fb['Campaign Name'].unique().tolist()
                facebook.append(fb_l)
                fb_df = pd.concat([fb_df, fb])
                print("fb")
                print(len(facebook))
######

df_u = pd.concat([fb_df, go_df, si_df, ot, tw])
df_u = df_u.drop_duplicates('Campaign Name')
df_u.to_csv('Campaigns/campaigns_unified.csv', index = False)

print("lista de campañas únicas:")
print(df_u)

subprocess.call('git add .', shell=True)
subprocess.call('git commit -m "campaigns unified update"', shell=True)
subprocess.call('git push', shell=True)
