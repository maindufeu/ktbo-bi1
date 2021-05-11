sshpass -p Eemaa9eiF4aeteigheiyu3Mae0piej sftp ktbo@sftp.adverity.com -22 << !
  cd uploads/test

  lcd Campaigns/facebook
  get facebook/*
  lcd ..
  rmdir facebook
  mkdir facebook

  lcd Campaigns/sizmekpr
  get sizmekpr/*
  lcd ..
  rmdir sizmekpr
  mkdir sizmekpr

  lcd Campaigns/sizmekmx
  get sizmekmx/*
  rmdir sizmekmx
  mkdir sizmekmx

  lcd Campaigns/sizmekmi
  get sizmekmi/*
  lcd ..
  rmdir sizmekmi
  mkdir sizmekmi

  lcd Campaigns/sizmekco
  get sizmekco/*
  lcd ..
  rmdir sizmekco
  mkdir sizmekco

  lcd Campaigns/google
  get google_ads/*
  lcd ..
  rmdir google_ads
  mkdir google_ads

  lcd Campaigns/youtube
  get youtube/*
  lcd ..
  rmdir youtube
  mkdir youtube

#  lcd mp
#  get mp/*
#  lcd ..
#  rmdir mp
#  mkdir mp

#  lcd twitter
#  get twitter/*
#  lcd ..
#  rmdir twitter
#  mkdir twitter

#  lcd othercampaigns
#  get othercampaigns/*
#  lcd ..
#  rmdir othercampaigns
#  mkdir othercampaigns


  bye
!

aws s3 cp s3://othercampaigns/acumulado_other/pautas_locales_acumulado_other.xlsx Campaigns/othercampaigns/acumulado_other.xlsx
aws s3 cp s3://othercampaigns/acumulado_twitter/pautas_locales_acumulado_twitter.xlsx Campaigns/twitter/acumulado_twitter.xlsx
