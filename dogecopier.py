# Copyright 2017 - writed by Rojo Ambinina

#  This code is just a homemade webscraping algorithm, to store in a file "Dogecoin_address.txt" 
#  the top 100 richest in Dogecoin on https://bitinfocharts.com using the module BeautifulSoup and Requests.
#  To use this little code, you just have to install the BeautifulSoup and Requests modules. That's all needed.

import re
import time
import sys
import os
from time import strftime
import requests
from bs4 import BeautifulSoup

i = 100
count = 100
t = time.process_time()
d = time.process_time() - t

while True:
    try:
        if i < 5000:
            ask = requests.get('https://privatekeys.pw/richest/dogecoin?page=' + str(i))
            soup = BeautifulSoup(ask.content, 'html.parser')
            address = soup.find_all(href=re.compile("https://privatekeys.pw/address/dogecoin/"))
            for dogecoin in address:
                print("\tCurrent Dogecoin Address... \t\t" + str(dogecoin.text) + "\n")
                with open('Dogecoin_address.txt', 'a+') as output:
                    output.write(str(dogecoin.text) + "\n")
                    output.close()
                    time.sleep(0.1)
            with open('Dogecoin_address.txt', 'a+') as output:
                output.write("\n----------------------- Dogecoin Address ----------------------- \n\n")
                output.close()
            time.sleep(0.2)
            print("----------------------------- " + str(count) + " Dogecoin Address -----------------------------\n\n")
            count += 100
            i += 1
        else:
            print("Process termined in " + d/10)
            break
          
    except urllib.error.HTTPError:
        print("\n\t Please wait ...\n")
        with open('Dogecoin_address.txt', 'a+') as output:
            output.write("\n----------------------- There was an ERROR here -----------------------\n\n")
            output.close()
        time.sleep(5)
        print("\t Error solved, Restarting ... \n")
        continue