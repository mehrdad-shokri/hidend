# Hidend

Hidend is a simple multitool for finding website backend ips. Hidend can be used to peform ip history checks, subdomain scans, http response checks, favicon hash matching with shodan and censys SSL certificate matching.

# Install

git clone https://github.com/cybertoolbank/hidend/

cd hidend

bash setup.sh

# Usage 

cd hidend

python3 hidend.py

# Tools Included

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
