import mp_checker as mp
import datetime as dt
import pandas as pd

df = pd.read_excel('03302021_ktbo_kube_AdverityExample_Mediaplan_Abril-Miami.xlsx')

mp.mp_validate(df)
print(mp.mp_validate(df))
