import os,sys
from app.phapi import *
import config



application_key = config.application_key
user_api_key = config.user_api_key

advertiser_client = Advertiser(application_key,user_api_key)

x = advertiser_client.list_campaigns()
print x.text