import requests

url = "https://quick-easy-sms.p.rapidapi.com/send"

payload = "message=hello&toNumber=14168052749"
headers = {
    'content-type': "application/x-www-form-urlencoded",
    'x-rapidapi-key': "cbc9fb60f2msh283a4325d46c8afp1b46e6jsn4353c386ff23",
    'x-rapidapi-host': "quick-easy-sms.p.rapidapi.com"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
