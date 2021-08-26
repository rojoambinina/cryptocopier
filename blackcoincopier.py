# Copyright 2017 - writed by Rojo Ambinina

#  This code is just a homemade webscraping algorithm, to store in a file "Blackcoin_address.txt" 
#  the top 100 richest in Blackcoin on https://bitinfocharts.com using the module BeautifulSoup and Requests.
#  To use this little code, you just have to install the BeautifulSoup and Requests modules. That's all needed.

import re
import time
import sys
import os
from time import strftime
import requests
from bs4 import BeautifulSoup

i = 1
count = 100
t = time.process_time()
d = time.process_time() - t

while True:
    try:
        if i < 102:
            ask = requests.get('https://bitinfocharts.com/top-100-richest-blackcoin-addresses-' + str(i) + '.html')
            soup = BeautifulSoup(ask.content, 'html.parser')
            address = soup.find_all(href=re.compile("https://bitinfocharts.com/blackcoin/address/"))
            for blackcoin in address:
                print("\tCurrent Dash Address... \t\t" + str(blackcoin.text) + "\n")
                with open('Blackcoin_address.txt', 'a+') as output:
                    output.write(str(blackcoin.text) + "\n")
                    output.close()
                    time.sleep(0.1)
            with open('Blackcoin_address.txt', 'a+') as output:
                output.write("\n----------------------- Blackcoin Address ----------------------- \n\n")
                output.close()
            time.sleep(0.2)
            print("----------------------------- " + str(count) + " Blackcoin Address -----------------------------\n\n")
            count += 100
            i += 1
        else:
            print("Process termined in " + d/10)
            break
          
    except:
        print("\n\t Please wait ...\n")
        with open('Blackcoin_address.txt', 'a+') as output:
            output.write("\n----------------------- There was an ERROR here -----------------------\n\n")
            output.close()
        time.sleep(5)
        print("\t Error solved, Restarting ... \n")
        continue