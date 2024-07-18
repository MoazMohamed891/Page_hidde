import os
import sys
import requests
import time
from bs4 import BeautifulSoup
##############################################################
print ("\033[31m")

os.system("figlet Hallo To Moaz Mohamed Script")

time.sleep(3)

os.system("clear")


print ("\033[1;31m")

print ("#"*67)

print ("\033[1;34m")

os.system('figlet Page Hidde ')

print ("\033[1;31m")

print ("\033[35m")
print (" \033[93;5m⚡\033[0m \033[35mBY.Moaz Mohamed\033[93;5m ⚡\033[0m")
print ("\033[36m")
print ("Github : https://github.com/MoazMohamed891")
print ("Linkedin : https://www.linkedin.com/in/moaz-mohamed-10b807318")
print ("\033[1;31m")

print ("#"*67)
##############################################################

print ("\033[1;37m")

url = input("\n[?] Enter Url Web : \033[1;31m")

print ("\033[1;33m")

print ("-"*67)

print ("\033[1;32m")

response = requests.get(url)
html_content = response.text

soup = BeautifulSoup(html_content, "html.parser")

links = soup.find_all("a")
for link in links:
      href = link.get("href")
      print (href)

print ("\033[1;33m")

print ("-"*67)

print ("\033[1;34m")

print ("\033[35m")
print (" \033[93;5m⚡\033[0m \033[35mBY: MoazMohamedx3\033[93;5m ⚡\033[0m")
