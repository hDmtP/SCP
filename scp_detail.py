#!/bin/python3
import sys
import requests
from bs4 import BeautifulSoup

R = '\033[31;1m'
H = '\033[95m'
B = '\033[94m'
G = '\033[92m'
W = '\033[93m'
F = '\033[91m'
E = '\033[0m'
U = '\033[4m'
O = '\033[33m'


logo = '''
\t  ____     ____   ____  
\t / ___|   / ___| |  _ \ 
\t \___ \  | |     | |_) |
\t  ___) | | |___  |  __/ 
\t |____/   \____| |_|    
                       
'''

if len(sys.argv) > 1:

    scp_no = sys.argv[1]

    url = f"https://scp-wiki.wikidot.com/scp-{scp_no}"

    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html5lib')

    scp_details = soup.find('div', attrs={"id": "page-content"})

    for i in scp_details:
        print(i.text)

else:    
    
    print(O + ' ')
    print("[!] Didn't specified any SCP number/code\n")
    print("[*] For Example, \n")
    print(" [-] python3 scp_detail" + G + " 096\n")
    print(O + " [-] python3 scp_detail" + G + " 005-INT\n")
    print(O + " [-] ./scp_detail" + G + " 6930\n")
    print(O + " [-] ./scp_detail" + G + " COOL-J\n")

    print(R + '_     _'.center(40))
    print("o' \.=./ `o".center(40))
    print('(o o)'.center(40))
    print('ooO--(_)--Ooo'.center(40))
    print(F + ' ')
    print(('Secure Contain Protect').center(40))
    print(logo)
