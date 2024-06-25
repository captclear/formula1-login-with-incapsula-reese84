import requests
import json
import uuid

# captcha api config on https://www.clearcaptcha.com 
clearcaptcha_api="http://api.clearcaptcha.com/captcha/incapsula_reese84_sub";
token = 'd7897e0ac82d47909af94a4a9b30test'
jsurl = "https://api.formula1.com/6657193977244c13"
user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"

post_data = {
    "token": token,
    "jsurl": jsurl,
    "user_agent": user_agent,
}

response = requests.post(clearcaptcha_api, data=post_data)
if response.status_code == 200:
    response_data = response.json()
    print(response_data)
else:
    print({
        "error": "api error",
        "status_code": response.status_code,
        "response": response.text
    })
    

post_data=response_data.get("data", {}).get("post_data", {})

headers={
        "Content-Type":"text/plain; charset=utf-8",
        "Host": "api.formula1.com",
        "User-Agent": user_agent,
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Content-Length": str(len(post_data)),
        "Referer": "https://account.formula1.com/",
        "Origin": "https://account.formula1.com",
        "Upgrade-Insecure-Requests": "1",
        "Sec-Fetch-Dest": "document",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-User": "?1",
        "Connection": "keep-alive",
        "Priority": "u=1"
    }
post_url="https://api.formula1.com/6657193977244c13?d=account.formula1.com"

response = requests.post(post_url, data=post_data,verify=False)
response_data = response.json()
reese84=response_data.get("token", {})

login_url="https://api.formula1.com/v2/account/subscriber/authenticate/by-password"
post_data =  {
    "Login": "test@gmail.com",
    "Password": "test123456",
    "DistributionChannel":"d861e38f-05ea-4063-8776-a7e2b6d885a4",
}
post_data=json.dumps(post_data)

cookies = {"reese84": reese84}
headers["Content-Type"]="application/json"
headers["apiKey"]="fCUCjWrKPu9ylJwRAv8BpGLEgiAuThx7"
response = requests.post(login_url, data=post_data,headers=headers,cookies=cookies,verify=False)
if response.status_code == 200: #The account and password are correct and the reese84cookie is correct, so the response is 200
    response_data = response.json()
elif response.status_code == 401: #If the account and password are incorrect and the reese84cookie is correct, the response is 401
    response_data = response.json()
else:
    response_data={
        "error": "api error",
        "status_code": response.status_code,
        "response": response.text
    }
    
print(response_data)
