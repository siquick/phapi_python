This is a few useful commands for the Performance Horizon API.
--
You'll need to create a `config.py` file following the template in `config_template.py`. You will need the `requests` library installed. 

__
Example

'''
###Usecase - I am an advertiser and want to see a list of all my campaigns

```python
advertiser_client = Advertiser(advertiser_application_key,advertiser_user_api_key)   
campaigns = advertiser_client.list_campaigns()   
for campaign in json.loads(campaigns.text)['campaigns']:  
	print campaign['campaign']
```
