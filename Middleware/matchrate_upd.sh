rm Campaigns/facebook/*
rm Campaigns/google/*
rm Campaigns/mp/*
rm Campaigns/othercampaigns/*
rm Campaigns/sizmekco/*
rm Campaigns/sizmekmx/*
rm Campaigns/sizmekmi/*
rm Campaigns/sizmekpr/*
rm Campaigns/twitter/*
rm Campaigns/youtube/*

cd Campaigns
./sftp_download.#!/bin/sh
python3 matchrate.py
aws s3 cp unmatched.csv s3://testingmidktbo/unmatched.csv
