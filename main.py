import requests
import json
import urllib.request

print('Meme Generator')
print('\n')
with open('config.json') as config_file:
	data = json.load(config_file)

ammount = data['ammount']
name = data['name']
apiurl = data['api']



print('running with settings : ')
print(f'''
api url : {apiurl}

''')
ammount1 = 0
while True:
	r = requests.get(apiurl)
	print(r.json()['url'])
	url = r.json()['url']
	ammount1 = ammount1+1
	print(ammount1)
	urllib.request.urlretrieve(r.json()['url'],  url.replace('https://i.redd.it/', ''))
