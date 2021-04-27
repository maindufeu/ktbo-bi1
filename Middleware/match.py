import datetime as dt
import pandas as pd
import requests
import os
import fnmatch
import re

def mp_match(mediaplan, mediafacts):
    print('working on it')
    matched = 0
    mp_u = mediaplan['Campaign Name'].unique()
    mf_u = mediafacts['Campaign Name'].unique()
    for i in mp_u:
        if i not in mf_u:
            print(f'falta {i} en los datastreams')
        else:
            matched = matched + 1

    for i in mf_u:
        if i not in mp_u:
            print(f'falta {i} en los planes de medios')
    mp_len = len(mp_u)
    mf_len = len(mf_u)
    matched_len = len(matched)
    matchrate = matched/mp_len
    if valid_status == 0:
        print('el match rate es de:')
        print(matchrate)
    else:
        print('el mediaplan contiene errores')
    return campaigns_matched
