# Austin Martin anonfile.com scraper

import re
import requests
from bs4 import BeautifulSoup
import socket
import sys

#First scrape pastebin.com for urls containing anonfile.com. Make sure IP of machine is whitelisted
ip = requests.get("https://api.ipify.org").text
print ("\033[1;31;40m" + str(ip) + "\033[1;37;40m is your scraping IP")


print ("Now starting scraping for Anon files on the internet.\n")
print ("Starting with pastebin.com")


# Code referenced from justhackerthings.com
keyword = ["anonfile", "anonfiles", "anonfile.com", "anonfiles.com"]

#Insert reference for the following code that I used below
# Start the scraping process by grabbing all the links in bing 
bingsearch = True
writtenlinks = []
counter = 1
print ("Now scraping through the Bing Search Engine")
print ("By default will do the first 30 Bing pages\n")

while bingsearch:
    src = requests.get('https://www.bing.com/search?q=https%3a%2f%2fanonfile.com%2f+site%3ahttps%3a%2f%2fanonfile.com%2f&first='+str(counter)+'&FORM=PERE', timeout=10).text
    links = src.split('<h2><a href="')[1:]
    for link in links:
        link = link.split('"')[0]
        if link in writtenlinks:
            continue
        else:
            handle = open('links.txt', 'a')
            handle.write(link+'\n')
            print(link + "\033[1;31;40m <--- New Link Found \033[1;37;40m")
            writtenlinks.append(link)
    src = requests.get('https://www.bing.com/search?q=https%3a%2f%2fanonfile.com%2f+site%3ahttps%3a%2f%2fanonfile.com%2f&first='+str(counter)+'&FORM=PERE2', timeout=10).text
    links = src.split('<h2><a href="')[1:]
    for link in links:
        link = link.split('"')[0]
        if link in writtenlinks:
            continue
        else:
            handle = open('links.txt', 'a')
            handle.write(link+'\n')
            print(link + "\033[1;31;40m <--- New Link Found \033[1;37;40m")
            writtenlinks.append(link)
    src = requests.get('https://www.bing.com/search?q=https%3a%2f%2fanonfile.com%2f+site%3ahttps%3a%2f%2fanonfile.com%2f&first='+str(counter)+'&FORM=PERE3', timeout=10).text
    links = src.split('<h2><a href="')[1:]
    for link in links:
        link = link.split('"')[0]
        if link in writtenlinks:
            continue
        else:
            handle = open('links.txt', 'a')
            handle.write(link+'\n')
            print(link + "\033[1;31;40m <--- New Link Found \033[1;37;40m")
            writtenlinks.append(link)
    src = requests.get('https://www.bing.com/search?q=https%3a%2f%2fanonfile.com%2f+site%3ahttps%3a%2f%2fanonfile.com%2f&first='+str(counter)+'&FORM=PERE4', timeout=10).text
    links = src.split('<h2><a href="')[1:]
    for link in links:
        link = link.split('"')[0]
        if link in writtenlinks:
            continue
        else:
            handle = open('links.txt', 'a')
            handle.write(link+'\n')
            print(link + "\033[1;31;40m <--- New Link Found \033[1;37;40m")
           
	    #end = link.split("https://anonfile.com/")[1]
            #api = requests.get("https://api.anonfile.com/" + end).text
	    #print (str(api))
	    #download(link) #Function to download the file
	    writtenlinks.append(link)

    if counter == 50:
	bingsearch=False

    counter += 1
#End of weird ass function

def download(url):
	#This function pulls the file to download

	#First request the api and see the file size
	api = requests.get("https://api.anonfile.com/" + url)
	print (str(api))


	#End of download() function


def vt():
	#This function hashes and submits files to Virus Total
	print ("Do nothing")




	# End of vt() function

def removedups():
	#This function removes duplicates from the resulting text file but keeps one
	print ("Do nothing")

	#End of remove dups file

#End of scraper
