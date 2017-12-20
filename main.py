import os,sys
from app.phapi import *
import config

advertiser_application_key = config.advertiser_application_key
advertiser_user_api_key = config.advertiser_user_api_key


'''Usecase - I am an advertiser and want to see a list of all my campaigns'''
advertiser_client = Advertiser(advertiser_application_key,advertiser_user_api_key)
campaigns = advertiser_client.list_campaigns()
for campaign in json.loads(campaigns.text)['campaigns']:
	print campaign['campaign']


# '''Usecase - I am an advertiser and I want to Approve a transactions'''
advertiser_client = Advertiser(advertiser_application_key,advertiser_user_api_key)
payload = {"conversions":[{"conversion_reference_id":"abc123","status":"approved","reject_reason":""},{"conversion_reference_id":"def123","status":"rejected","reject_reason":"not an affiliate sale"}]}
campaign_id = 'ghj294'
validation = advertiser_client.validate_transaction(payload,campaign_id)
print validation.text	


