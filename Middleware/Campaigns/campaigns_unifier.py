import pandas as pd
import glob
import os
import fnmatch



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

fb_df.to_csv("Campaigns/campaigns_unified_fb.csv")

go_df.to_csv("Campaigns/campaigns_unified_go.csv")

si_df.to_csv("Campaigns/campaigns_unified_si.csv")

ot.to_csv("Campaigns/campaigns_unified_ot.csv")

tw.to_csv("Campaigns/campaigns_unified_tw.csv")

df_u = pd.concat([fb_df, go_df, si_df, ot, tw])
df_u['Campaign Name'] = df_u['Campaign Name'].unique()

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

#c_list = pd.DataFrame(c_list, columns=['Campaign Name'])
#c_list = c_list['Campaign Name'].unique().tolist()
#c_list.to_csv("Campaigns/campaigns_unified1.csv")

print("lista de campañas únicas:")
print(c_list)
print(len(c_unified))
