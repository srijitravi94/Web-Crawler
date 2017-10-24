# Importing required libraries
import urllib.request as ul
import re
from bs4 import BeautifulSoup
import time


# Declaring Global variables
BASE_URL = "https://en.wikipedia.org"
SEED_URL = "https://en.wikipedia.org/wiki/Tropical_cyclone"
GIVEN_DEPTH = 6
NO_OF_PAGES_TO_CRAWL = 1000


# A function that returns all the links of a given page
def getLinks(page):
    listOfLinks = []
    webPage = ul.urlopen(page)                                        # Opens the webpage 
    soup = BeautifulSoup(webPage, "html.parser")                      # Extracts all the contents of the opened webpage
    divData = soup.findAll('div')                                     # Finds all the 'div' tags
    header = soup.find('h1', { 'id' : 'firstHeading'}).text           # Finds the 'h1' tag of 'firstHeading' class; to handle redirected pages
    for div in divData:
        links = div.findAll('a',{'href' : re.compile('^/wiki/')})     # Finds all the 'a' tag with regex '/wiki/' 
        for link in links:
            fullURL = BASE_URL + link.get('href')
            if '#' not in fullURL and ':' not in link.get('href'):    # Ignores the admin links and sections inside the page
                listOfLinks.append(fullURL)
    return listOfLinks, header


# A funtion that returns a union of the given two lists with unique elements
def addToList(list1,list2):
    for link in list2:
        if link not in list1:
            list1.append(link)
    return list1           


# A function that returns a list of 1000 unique pages crawled from the given SEED_URL
def crawler(SEED_URL):
    pagesToCrawl = [SEED_URL]
    pagesCrawled = []
    linkHeadings = []
    nextSet = []
    depth = 1
    count = 1
    while pagesToCrawl and len(pagesCrawled) < NO_OF_PAGES_TO_CRAWL and depth <= GIVEN_DEPTH:
        page = pagesToCrawl.pop(0)
        if page not in pagesCrawled:
            time.sleep(1)                                             # Implementing the politeness policy
            links, header = getLinks(page)                            # Obtains all the links in given page
            if header not in linkHeadings:                            # Handling redirected pages
                linkHeadings.append(header)
                nextSet = addToList(nextSet,links)
                pagesCrawled.append(page)
                print(str(count) + ". " + page + " : " + str(depth))  # Printing the depth of each page
                count +=1
            if len(pagesToCrawl)==0:
                pagesToCrawl = nextSet
                nextSet = []
                depth += 1
    return pagesCrawled


# A function that writes the given content to a file 
def writeFile(listOfLinks):
    file = open('crawledURLs.txt', 'w')
    count = 1
    for link in listOfLinks:
        file.write(str(count) + ". " + str(link) + "\n")
        count+=1
    file.close()


# The main function
def main():
    listOfLinks = crawler(SEED_URL)
    writeFile(listOfLinks)
main()