import re
import pandas as pd
from concurrent.futures import ThreadPoolExecutor, as completed
from netmiko import ConnectHandler

DEVICE FILE

File Inputs

"C:\Users\dk17\OneDrive Capgemini\Desktop\Python scripts\Device Config Backup\Backing UP\devices.txt"

#

CREDENTIAL FILE

r"C:\Users\dk17\OneDrive Capgemini\Desktop\Python scripts\Device Config Backup Backing UP\credentials.txt"

COMMAND FILE

"C:\Users\dk17\OneDrive - Capgemini\Desktop\Python scripts\Device Config Backup Backing UP\commands.txt"

#

OUTPUT_EXCEL

"C:\

Users\dk17\OneDrive Capgemini\Desktop\Python scripts\Device Config Backup Backing UP\Cisco_IOS_Version_Report.xlsx"

Load Devices

with open(DEVICE_FILE) as f:

devices [line.strip() for line in f if line.strip()]

#

Load Credentials

with open(CREDENTIAL_FILE) as f:

creds f.read().strip().split(":")

#

USERNAME, PASSWORD = creds[0], creds [1]

Load Commands

with open(COMMAND FILE) as f:

commands [line.strip() for line in f if line.strip()]

# Worker Function

def collect outputs(host):

device {

"device type": "cisco ios",

"host": host,

"username": USERNAME,

"password": PASSWORD,

"fast cli": False,

}

try:

conn ConnectHandler(**device)

conn.enable()

version

model

for cmd in commands:

output conn.send.command( cmd, read timeout=60 )

for line in gutput.splitlines():

#10S Version

if "Version" in line and not version:

match re.search(r"version\s+([^\s,]+)", line)

if match:

version match.group(1)

# Catalyst 9K

if "Model Number" in line:

model line.split(":")[-1].strip()

# Catalyst 2K

elif "processor" in line.lower() and "cisco" in line.lower():

words line.split()

if len(words) > 1:

model words[1]



Get actual switch hostname

hostname conn.find prompt().replace("#", "").replace(">", "").strip()

conn.disconnect()

return {

"Host": host, "Hostname": hostname, "Status": "Success", "10S Version": version, "Model Number": model

except Exception as e:

return (

"Host": host, "Hostname": "", "Status": f"Failed (str(e))", "IOS version": "", "Model Number":

}

def main():

all_results = []

I

with ThreadPoolExecutor (max workers=50) as executor:

futures = {

executor.submit(collect_outputs, host): host for host in devices

}

for future in as completed (futures):

result = future.result()

all results.append(result)

print(

f"{result['Host']} | "

)

f"{result['Hostname']} | "

f"{result['status']} |

f"{result['IOS Version']} |"

f"{result['Model Number']}"


print(

)

f"(result['Host']} | "

f"(result['Hostname']} | "

f"{result['status']} |

f"(result['IOS Version']} |

f"{result['Model Number']}"

#Generate Excel

df pd.DataFrame(all results)

df = df[ [

"Host",

"Hostname",

"Status",

"IOS Version",

"Model Number"

]

1

df.to excel (OUTPUT_EXCEL, index=False)

print("\n====

")

print("Report Generated Successfully")

print(f"Location: (OUTPUT_EXCEL}")

print("======

if

")

name main()

main":

all results[]

with ThreadPoolExecutor (max workers-50) as executor:

}

futures {

executor.submit(collect outputs, host): host for host in devices

for future in as completed(futures):

result future.result() all results.append(result)

print(
