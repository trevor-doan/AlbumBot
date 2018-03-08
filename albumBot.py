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

        # TODO: Also check for HTML bits with XXXX comments.
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
        
        print(div.get("data-author"))
        print(comment.a['href'])
        print(comment.a.contents)
        print("\n\n")
        
        



    # search for imgur links, reddit permalinks, and reddit usernames

    # this will print every reddit user found in the page, INCLUDING the moderators of the subreddit
    """
    for item in soup.find_all(href=re.compile("https://www.reddit.com/user/")):
        print(item)

    # this will print every imgur link found in page INCLUDING "display 500 comments..." and "report" in the sidebar
    for item in soup.find_all(href=re.compile("imgur.com/")):
        print(item)

    """
    #TODO: does not work - trying to print every continue this thread link

    """
    for item in soup.find_all('deepthread', attrs={"data-inbound-url"}):
        print(item.attrs)
    """

    """
    
    for item in soup.find_all('span', attrs={"class" : "deepthread"}):
        print(item.contents[0])

    for item in soup.find_all('span', attrs={"class" : "deepthread"}):
        print(item.contents[0].get("href"))

    """

    """
    
    #new test ( 1/5/2018) of "parent class"
    for item in soup.find_all('div', attrs={"data-type" : "comment"}):
        print(item.attrs)
    """




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
    url = "http://reddit.com/r/photoshopbattles/top"

    soup = downloadHTML(url)
    createThreadList(soup, threadList)

    #debug print statment
    print("NOW PRINTING LIST OF LINKS")
    printList(threadList)

    # new
    soup = downloadHTML(threadList[0])
    create2DList(soup)



main()