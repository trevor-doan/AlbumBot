#! python3
# albumBot.py - Generates photo albums of top comments in Reddit threads

import requests, os, bs4, re
from selenium import webdriver

def downloadHTML(url):
    """downloads an html page and returns a BeautifulSoup object"""
    
    res = requests.get(url, headers = {'User-agent': 'your bot 0.1'})
    res.raise_for_status()

    return bs4.BeautifulSoup(res.text, "html.parser")

def createThreadList(soup, threadList):
    """makes a sorted list of reddit threads with 100 comments or more"""

    # search for links to reddit threads with 100 comments or more
    for attribute in soup.find_all("a"):
        line = attribute.get_text()

        lineRegex = re.compile(r"\d\d\d comments")
        comm = lineRegex.search(line)

        if comm is not None:

            # print line that meets criteria for debugging purposes
            # print("WOW LOOKEY HERE! "+ comm.group())

            # get the link to the reddit thread with 100 comments or more sorted by top comments
            threadList.append(attribute.get("href") + "sort=top?depth=1")
        
        # print line for debugging purposes
        # print(line)

        prevLine = line

    #remove first link in threadList, as it is an imgur link to a subreddit rule
    threadList.pop(0);

    # TODO: make a while loop that will run until no more reddit pages
    #       with over 100 comments are left



def create2DList(soup):
    """makes a 2D list of imgur links, reddit permalinks, and reddit usernames"""

    twoDimList = []

    for div in soup.find_all(attrs={"data-type": "comment"}):
        commentData = {'username': None, 'link': None, 'text': None, 'permalink': None}
        commentData['username'] = div.get("data-author")
        comment = div.contents[2].contents[1].contents[1].contents[0]
        
        usr = div.get("data-author")
        if usr == None:
            usr = "Deleted"

        print("Username: " + usr)
        print("Link: " + comment.a['href'])
        print("Text: " + str(comment.a.contents[0].encode("utf-8")))

        temp = div.find(attrs={"class": "deepthread"})
        if(temp != None):
            print("Thread Permalink: " + "https://reddit.com" + temp.a.get("data-href-url"))
        
        print("\n\n")


def saveImage():
    """saves image to ./albumBot"""


def makeAlbum():
    """uses Selenium to make an imgur album"""

def printList(list):
    """prints a list of strings"""

    for index in list:
        print(index)

def main():

    threadList = []
    url = "https://www.reddit.com/r/photoshopbattles/top/?sort=top&t=week"

    soup = downloadHTML(url)
    createThreadList(soup, threadList)

    # debug print statment
    printList(threadList)

    # new
    for i in range(0, len(threadList)):
        soup = downloadHTML(threadList[i])
        create2DList(soup)



main()