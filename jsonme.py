#Extracting Data from JSON with given url
#You can check result with: http://py4e-data.dr-chuck.net/comments_42.json
#Output should be: ===> Count: 50 and Sum: 2553

#import necessary libs
import urllib.request , urllib.parse , urllib.error
import json
import ssl

#Constant var.
sum = 0
counter = 0
#ignore ssl
cer = ssl.create_default_context()
cer.check_hostname = False
cer.verify_mode = ssl.CERT_NONE

#Ask for url of JSON file and decode it
url_name = input("Enter -")
fhand = urllib.request.urlopen(url_name , context = cer)
data = fhand.read().decode()

#Create dict() from json obj.
try:
    data_js = json.loads(data)
except:
    data_js = None

if not (data_js == None):
    #Print for debugging
    print(json.dumps(data_js))
    counter = len(data_js['comments'])
    #Count and sum needed parts
    for i in range(0,counter):
        sum = sum + (data_js["comments"][i]["count"])

#Print results
print("Count:",counter,"and","Sum:",sum)
