import datetime as dt
import pandas as pd
import requests
import os
import fnmatch
import re

def mp_match(mediaplan, mediafacts):
    print('working on it')
    mp_len = len(mediaplan)
    mf_len = len(mediafacts)
    campaigns_matched = mediaplan.join(mediafacts,  how = left)
    matched_len = len(campaigns_matched)
    matchrate = matched_len/mp_len
    if valid_status == 0:
        print('el match rate es de:')
        print(matchrate)
    else:
        print('el mediaplan contiene errores')
    return campaigns_matched
    print(matchrate)
