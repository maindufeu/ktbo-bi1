import pandas as pd


other = pd.read_excel("othercampaigns/acumulado_other.xlsx")
twitter = pd.read_excel("twitter/acumulado_twitter.xlsx")
twitter = twitter['Campaign'].upper().strip(" ")
print("Twitter length:")
print(len(twitter))

print("othercampaigns")
other = other['Campaign'].upper().strip(" ")
print("Other Campaigns length:")
print(len(other))


google = pd.read_csv("google\409571_adwords_adwords-143-20210427-94eedaa01640429a86addf575c77449a.csv")
google = google['Campaign_duplicate']
print(len(google))
c_unified =twitter + other +google
print(len(c_unified))
