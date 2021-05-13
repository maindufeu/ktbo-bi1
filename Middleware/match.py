import datetime as dt
import pandas as pd
import requests
import os
import fnmatch
import re

"""
def mp_match(mediaplan, mediafacts):
_    print('working on it')
    valid_status = 0
    matched = 0
    campaigns_matched = []
    mp_list = []
    mp_u = mediaplan['Campaign Name'].unique()
    mf_u = mediafacts['Campaign Name'].unique()
    for i in mp_u:
        if i not in mf_u:
            mediaplan_c = list(mediaplan[mediaplan['Campaign Name'] == i]['Mediaplan'])[0]
            print(f'falta {i} del plan de medios {mediaplan_c} en los datastreams')
            mp_list.append(mediaplan_c)
            campaigns_matched.append(i)
        else:
            matched = matched + 1

    for i in mf_u:
        if i not in mp_u:
            print(f'falta {i} en los planes de medios')
    mp_len = len(mp_u)
    mf_len = len(mf_u)
    matchrate = matched/mp_len
    if valid_status == 0:
        print('el match rate es de:')
        print(matchrate)
    else:
        print('el mediaplan contiene errores')

    campaigns_matched = [campaigns_matched,mp_list]
    return campaigns_matched
"""
mediafacts=pd.read_csv(r"Campaigns\campaigns_unified.csv")
mediaplan=pd.read_csv(r"Mediaplan\mp_processed\Adverity-export_Plan.csv")



###########################################
def mp_match(mediaplan, mediafacts):
    df_facts = mediafacts[["Campaign Name"]]
    df_facts['is_fact'] = True
    df_mediaplan = mediaplan[["Campaign Name", "Mediaplan"]]
    df_mediaplan['is_campaign'] = True

    df_join = pd.merge(df_facts, df_mediaplan, on='Campaign Name', how='outer')

    matching_campaigns = df_join[(df_join['is_fact'] == True) & (df_join['is_campaign'] == True)]
    unmatching_campaigns = df_join[(df_join['is_fact'] != True) & (df_join['is_campaign'] == True)]

    matching_campaigns[["Campaign Name", "Mediaplan"]].to_csv("matching_campaigns.csv", index=False)
    unmatching_campaigns[["Campaign Name", "Mediaplan"]].to_csv("unmatching_campaigns.csv", index=False)

    print("Matching: ",len(matching_campaigns))
    print("Unmatching: ", len(unmatching_campaigns))

    return 0
