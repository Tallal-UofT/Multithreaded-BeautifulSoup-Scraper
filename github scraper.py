from urllib.request import urlretrieve
import urllib.parse
from urllib.parse import urlencode, urlparse, parse_qs
import webbrowser
from bs4 import BeautifulSoup, SoupStrainer
import requests
import re
import os
import csv
from multiprocessing.dummy import Pool  # This is a thread-based Pool
from multiprocessing import cpu_count
import time
import random
from requests.adapters import HTTPAdapter
from requests.exceptions import ConnectionError



def crawlToCSV(URLr):
    #strainer = SoupStrainer('tr')
    session = requests.Session()
    adapter = HTTPAdapter(max_retries=50)
    session.mount('https://', adapter)
    print(URLr)
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'referrer': 'https://www.ic.gc.ca/opic-cipo/cpd/eng/search/boolean.html',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9',
        'Upgrade-Insecure-Requests': '1',
        'Pragma': 'no-cache'
    }
    delays = [1,3,5,7]
    delay = random.choice(delays)
    time.sleep(delay)
    u = session.get(URLr, headers=headers, timeout=1500).text
    soup = BeautifulSoup(u, "lxml")
    O = []
    for match in soup.find_all('p'):
            match = match.text
            match = " ".join(re.split("\s+", match, flags=re.UNICODE))
            #print(match)
            O.append(match)
    


    return O



if __name__ == "__main__":
    os.chdir('C:\\Users\\TU\\Desktop')

    
    l = 0
    
    for n in range(1,100):
        URLr = []
        for k in range( (l), (l+20000)):
            URLr.append("URL" + str(k))
        print(URLr)
        result = []
        pool = Pool(cpu_count()*2)
        result= pool.map(crawlToCSV, URLr)
        time.sleep(5)
        print(result)
    
        result1 = result
        
        l = l+20000
        #
        #
        with open('File_NAME' + str(n)+ '.csv', 'w') as csvFile:
            writer = csv.writer(csvFile)
            writer.writerows(result1)
        
            csvFile.close()

  


    

