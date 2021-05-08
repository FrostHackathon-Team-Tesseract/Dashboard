import requests

response = requests.get('https://api.rootnet.in/covid19-in/stats/latest')
print(response.status_code)
data = (response.json())
data = data['data']['regional']

statewise_data = {}

for i in data:
    s = {
    i['loc']:i['confirmedCasesIndian']     
    }
    statewise_data.update(s)
print(statewise_data)
