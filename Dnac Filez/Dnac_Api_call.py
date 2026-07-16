url = f"https://{CC_IP}/dna/system/api/vl/auth/token"

Bresponse = requests.post(

url,

auth=(USERNAME, PASSWORD),

verify=False

# Disable certificate verification (lab only)

)

token = response.json() ["Token"]

print("Authentication Token:")

print (token)

url= f"https://{CC_IP}/dna/intent/api/vl/network-device"

headers = {

}

"X-Auth-Token": token,

"Content-Type": "application/json"

response = requests.get(

(

url,

headers=headers,

verify=False

print(response.status code)

print(response.json())