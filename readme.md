Python library for the Performance Horizon API.
--

### Requirements & Depedencies

You'll need to create a `config.py` file following the template in `config_template.py`. You will need the `requests` library installed. 

Payloads and descriptions of API methods available at https://docs.performancehorizon.apiary.io/#

### Syntax and example


##### I am an advertiser and want to see a list of all my campaigns

```python
advertiser_client = Advertiser(advertiser_application_key,advertiser_user_api_key)   
campaigns = advertiser_client.list_campaigns()   
for campaign in json.loads(campaigns.text)['campaigns']:  
	print campaign['campaign']
```
