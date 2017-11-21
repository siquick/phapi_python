import requests
import csv
import base64
import json


base_url = 'https://api.performancehorizon.com'

'''Authentication'''

def encode_auth(application_key,user_api_key):
	auth_credentials = base64.b64encode(application_key + ':' + user_api_key)
	return auth_credentials

'''POST / GET / PUT'''

def api_call_post(application_key,user_api_key,endpoint,payload):
	auth_credentials = encode_auth(application_key,user_api_key)
	headers = {'Authorization': 'Basic ' + auth_credentials}
	print headers
	print payload
	try:
		r = requests.post(endpoint,headers=headers,data=payload)
		return r
	except Exception as e:
		return str(e)
	

def api_call_get(application_key,user_api_key,endpoint,payload):
	auth_credentials = encode_auth(application_key,user_api_key)
	headers = {'Authorization': 'Basic ' + auth_credentials}
	print headers
	print payload
	try:
		r = requests.get(endpoint,headers=headers,data=payload)
		return r
	except Exception as e:
		return str(e)

def api_call_put(application_key,user_api_key,endpoint,payload):
	auth_credentials = encode_auth(application_key,user_api_key)
	headers = {'Authorization': 'Basic ' + auth_credentials}
	print headers
	print payload
	try:
		r = requests.put(endpoint,headers=headers,data=payload)
	except Exception as e:
		return str(r)


'''Publisher Functions'''
class Publisher():

	def __init__(self,application_key,user_api_key):
		self.application_key = application_key
		self.user_api_key = user_api_key

	#payload = TBC
	def create_publisher(application_key,user_api_key,payload):
		endpoint = 'https://api.performancehorizon.com/user/publisher'
		output = api_call_post(self.application_key,self.user_api_key,endpoint,payload)
		return output


	#payload = '{'campaign_id':campaign_id}'
	def join_campaign(application_key,user_api_key,payload,publisher_id,campaign_status):
		endpoint = 'https://api.performancehorizon.com/user/publisher/%s/campaign/%s' % (publisher_id,campaign_status)
		output = api_call_post(self.application_key,self.user_api_key,endpoint,payload)
		return output


'''Advertiser Functions'''
class Advertiser():

	def __init__(self,application_key,user_api_key):
		self.application_key = application_key
		self.user_api_key = user_api_key

	#payload = {'account_name': account_name,'company_name':company_name,'address1':address1,'postcode':postcode,'country':country,'phone':phone,'signup_ip':signup_ip}
	def create_advertiser(self, payload):
		endpoint = 'https://api.performancehorizon.com/user/advertiser'
		output = api_call_post(self.application_key,self.user_api_key,endpoint,payload)
		return output

	#payload = {}
	def list_campaigns(self):
		endpoint = base_url + '/campaign/'
		payload = ''
		output = api_call_get(self.application_key,self.user_api_key,endpoint,payload)
		return output

	#payload = {'auto_approval':'y','title':campaign_title,'advertiser_id':advertiser_id,'destination_url':destination_url,'default_commission_value':'0'}
	def create_campaign(self, payload):
		endpoint = 'https://api.performancehorizon.com/campaign'
		output = api_call_post(self.application_key,self.user_api_key,endpoint,payload)
		return output

	#payload = {'auto_approval':'y','title':campaign_title,'advertiser_id':advertiser_id,'destination_url':destination_url,'default_commission_value':'0'}
	def update_campaign(self, payload,campaign_id):
		endpoint = 'https://api.performancehorizon.com/campaign/%s' % (campaign_id)
		output = api_call_put(self.application_key,self.user_api_key,endpoint,payload)
		return output

	#payload = '{'campaign_id':campaign_id,'action':'delete','retire_reason':'add retire reasons here'}'
	def delete_campaign(self, payload,campaign_id):
		endpoint = 'https://api.performancehorizon.com/campaign/%s' % (campaign_id)
		output = api_call_post(self.application_key,self.user_api_key,endpoint,payload)
		return output

	'''payload = {"conversions":[{"conversion_reference_id":"abc123","status":"approved","reject_reason":""},{"conversion_reference_id":"def123","status":"rejected","reject_reason":"not an affiliate sale"}]}'''
	def validate_transaction(self, payload,campaign_id):
		endpoint = 'https://api.performancehorizon.com/campaign/%s/conversion' % (campaign_id)
		output = api_call_post(self.application_key,self.user_api_key,endpoint,payload)
		return output


'''Creative Functions'''
class Creative():
	
	def __init__(self,application_key,user_api_key):
		self.application_key = application_key
		self.user_api_key = user_api_key	

	#payload = TBC
	def create_creative(application_key,user_api_key,payload,campaign_id):
		endpoint = 'https://api.performancehorizon.com/campaign/%s' % (campaign_id)
		output = api_call_post(self.application_key,self.user_api_key,endpoint,payload)
		return output

	def update_creative(application_key,user_api_key,payload,campaign_id):
		endpoint = 'https://demoapi.performancehorizon.com/campaign/%s/creative' % (campaign_id)
		output = api_call_put(self.application_key,self.user_api_key,endpoint,payload)
		return output







