import os
import sys
import time
import json
from urllib import request

os.system("clear")
print("\033[32;1m ")
os.system("figlet Ip Track")
print("VERSION 1,1")
print("<=========================>")
print("Welcome To Ip Track")
print("1)Track Ip")
print("2)Exit")
print("<=========================>")
select = input("Select:")
if select == "1":
	print("Loading...")
	time.sleep(5)
	url = "https://ipinfo.io/"
ip = input("Input the IP Address : ")
request = request.urlopen(url + ip + "/json")
data_json = json.loads(request.read())

for data in data_json:
	info = str(data_json[data])
	print(data + " : " + info)
	
	



	
	