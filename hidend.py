import mmh3
import requests
import codecs
import time
import re
import urllib
from bs4 import BeautifulSoup as bs4
from urllib.request import urlopen, Request
from colorama import Fore
import dns
import dns.resolver


#Print
print('')
print('''-----Finding Website Backends Made Easy By Cybertoolbank.cc----''')  
ascii = '''                          ____                                 
 |         | | |``````.  |            |..          | |``````.  
 |_________| | |       | |______      |  ``..      | |       | 
 |         | | |       | |            |      ``..  | |       | 
 |         | | |......'  |___________ |          ``| |......'  
                                                              '''    
print(ascii)                                         
print('''---------------------------------------------------------------''')
print('1: Obtain Favicon Hash')
print('2: Subdomain Scan')
print('3: Domain Ip History') 
print('4: Ssl Certificate Fingerprint Search') 
print('5: Http Response Checker') 
print('''---------------------------------------------------------------''')
print('h: Help')
print('q: Quit') 
print('''---------------------------------------------------------------''')
option = input('Select Option: ')

# Favicon Hash

if option == "q":
   print('''---------------------------------------------------------------''')
   quit()
   
if option == "h":
   print('''---------------------------------------------------------------''')
   print('''
1:
  Obtain Favicon Hash: This option will obtain the favicon from
  the path you give and generate base64 hash out of it, which 
  it will then put inside a shodan.io search query ready for 
  you to paste inside shodan.io. We cannot automate this, 
  because the shodan API plan that allows using this filter 
  costs for the user. This method is good for finding backend 
  ips, because hosts with direct ip access will be exposed and
  could be using the same favicon. 
  
2:
  Subdomain Scan: This option will scan a website for possible 
  subdomains, and then check the DNS A record for you. This might
  help you find misconfigured subdomains, if one subdomain has a
  different ip than the other subdomains it might be a sign of 
  misconfigured DNS records which might expose the backend ip, 
  but thats not always the case. If you want to change the 
  default wordlist you will need to edit the subdomains.txt file.
  
3:
  Domain Ip History: This option will check a domains ip history.
  This is useful if the backends ip was directly pointed to the 
  domain before proxying the traffic trough a ddos protection like 
  cloudflare for example.
  
4: 
  Ssl Certificate Fingerprint Search: This option will give you a
  censys search query, which allows you to see if your configuration is 
  exposing the SSL certificate when directly connecting to your IP.
  
5: 
  Http Response Checker: This option will send a request to given URL
  and print the response for you to look at. The response might contain
  all kinds of useful information for finding the website backend like
  unique HTTP Headers. 
    ''')
   print('')
   print('''---------------------------------------------------------------''')
   quit()

if option == "1":
   print('''---------------------------------------------------------------''')
   print('Selected Option: Obtain Favicon Hash')
   print('''---------------------------------------------------------------''')
   type = input('Favicon URL Path: ')
   print('''---------------------------------------------------------------''')
   response = requests.get(type)
   favicon = codecs.encode(response.content,"base64")
   hash = mmh3.hash(favicon)
   print(f'[+] http.favicon.hash:{hash} paste this query to shodan.io')
   print('''---------------------------------------------------------------''')
   quit()   

# Subdomain Scan

if option == "2":
   print('''---------------------------------------------------------------''')
   print('Selected Option: Subdomain Scan')
   print('''---------------------------------------------------------------''')
   domain = input('Enter A Domain To Scan: ')
   print('''---------------------------------------------------------------''')
   print('''Scan started! It takes a while. Press ctrl+z to abort.''')
   print('''---------------------------------------------------------------''')
   filename="subdomains.txt"
   with open(filename) as file:
    for subdomain in file.readlines():
        subdomain_url = f"https://{subdomain.strip()}.{domain}"      
        try:
            reponse = requests.get(subdomain_url)
            if reponse.status_code==200:
               result = dns.resolver.resolve(f'{subdomain.strip()}.{domain}', 'A')
               for ipval in result:
                   ip = (ipval.to_text()) 
                   print(f"[+] Domain: {subdomain_url}  DNS: {ip}")                     
        except:
            pass              
   quit()  
        
# Domain Ip History

if option == "3":  
   print('''---------------------------------------------------------------''')
   print('Selected Option: Domain Ip History')
   print('''---------------------------------------------------------------''')
   dooman = input('Enter A Domain To Scan: ')
   print('''---------------------------------------------------------------''')
   print('''Scan started! please be patient this might take a while!''')
   print('''---------------------------------------------------------------''')
   url = 'https://viewdns.info/iphistory/?domain=' + dooman
   req = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
   res = req.read()
   sou = bs4(res, 'html.parser')
   rgx = re.compile('\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')
   fnl = [] 
   for ent in sou.findAll('td'):
	   if rgx.match(ent.text):
	       fnl.append(ent.text) 
   fnl = list(set(fnl))  
   for ent in fnl:
	    print (f"[+] {ent}")      	       	    
   print('''---------------------------------------------------------------''')
   quit() 
   
# Ssl Certificate

if option == "4":  
   print('''---------------------------------------------------------------''')
   print('Selected Option: Ssl Certificate Fingerprint Search')
   print('''---------------------------------------------------------------''')
   sslsig = input('Ssl Cert SHA-256 Fingerprint: ')
   sslsiga = sslsig.replace(':','') 
   print('''---------------------------------------------------------------''')
   url = (f'https://search.censys.io/search?resource=hosts&q=services.tls.certificates.leaf_data.fingerprint%3A+{sslsiga}+or+services.tls.certificates.chain.fingerprint%3A+{sslsiga}')
   print(f'''Paste this URL in your browser: 
{url}''')
   print('''---------------------------------------------------------------''')
   quit() 
   
# Http Response Checker

if option == "5":  

   print('''---------------------------------------------------------------''')
   url = input("URL To Scan: ")
   print('''---------------------------------------------------------------''')
   print('''Http request sent! Please be patient for the response!''')
   print('''---------------------------------------------------------------''')
   print('')
   print('')
   response = urlopen(Request(url, headers={'User-Agent': 'Mozilla'}))
   html = response.info()
   print(html)
   print('''---------------------------------------------------------------''')
   quit()
   
# If someone is retarded this will show

else:
	print('''---------------------------------------------------------------
Please make sure that the input you entered is correct!
---------------------------------------------------------------''')


