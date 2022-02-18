#!/bin/python3
import requests
from bs4 import BeautifulSoup
import sys

url = "https://scp-wiki.wikidot.com/joke-scps"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')

scps = soup.find_all('ul')

scp_list = []
# 
for i in scps:
    print(i.text)
# 
# scps2 = soup.find('div', attrs={"style": "border: solid 1px #999999; width:95%; background-color:#ECE3A6; padding:5px; float:left; margin-bottom:4px;"})
# #
# for i in scps2:
    # scp = i.text
    # scp_list.append(scp)

# print(scp_list, len(scp_list))

'''
scp_no = sys.argv[1]

# url = f"http://scpclassic.wikidot.com/scp-{scp_no}"
url = f"https://scp-wiki.wikidot.com/scp-{scp_no}"

r = requests.get(url)
soup = BeautifulSoup(r.content, 'html5lib')

scp_details = soup.find('div', attrs={"id": "page-content"})

for i in scp_details:
    print(i.text)
'''
