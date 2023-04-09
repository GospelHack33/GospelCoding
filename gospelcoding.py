# this is a webcam analysis toolkit that's perform webcam tracking i.e location, id, and its status
# this is is only built for educational purposes only... don't misuse this tool!!! 
# start
import time
import os
import requests
import cfonts
from colorama import Fore, Back

# ...
if os.name == 'posix':
   os.system('clear')
elif os.name == 'nt':
   os.system('cls')
else:
   print(Fore.RED+'[*] Unable To Clear Screen Output...'+Fore.WHITE)
#

# ...
app_title = cfonts.render('Gospel Coding', colors=['red', 'blue'], align='center')
print(app_title)
print(Fore.YELLOW+'WebCam Analysis Toolkit'.center(66)+Fore.WHITE)
print(Fore.BLUE+'V3.2.1'.center(66)+Fore.WHITE)
#

# ...
print(Fore.GREEN+'[01] Fetch Active WebCams By Country'+Fore.WHITE, '\n')
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
   if len(country) == 2:
      pass
   else:
      print(Fore.RED+'\n[*] The Country Code Must Be An Alpha-2-Code e.g NG For Nigeria CA For Canada EU For Europe And So On...'+Fore.WHITE)

   print(Fore.YELLOW+'\n[*] Fetching Active WebCams At {}... '.format(country)+Fore.WHITE, '\n')

   fetch = requests.get('https://api.windy.com/api/webcams/v2/list/country={}/orderby=popularity/limit=20?key={}'.format(country, apikey))
   if fetch.text == '{"status":"OK","result":{"offset":0,"limit":20,"total":0,"webcams":[]}}':
      print(Fore.GREEN+'\n[*] No Active WebCams Available...'+Fore.WHITE)
      exit(0)
   else:
        pass
   response = eval(fetch.text)['result']['webcams']
   for data in response:
       print(Fore.BLUE+'[*] WebCam ID - ', data['id'], Fore.GREEN+'Status -', data['status'], Fore.YELLOW+'Location - ', data['title'], '\n')
else:
     exit(0)
