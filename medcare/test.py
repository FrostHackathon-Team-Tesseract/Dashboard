import requests

response = requests.get('https://api.endlessmedical.com/v1/dx/GetFeatures')
print(response.status_code)
print(response.json())