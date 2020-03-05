# if we want to efficiently parse html, we can use BeautifulSoup

from bs4 import BeautifulSoup

with open ("wiki_attorneys.html", "r", encoding = 'utf8') as rf:
    html = rf.read()

soup = BeautifulSoup(html, 'lxml') # lxml is default parser, structured set of wells that tells beuatiful soup how html will behave, it is one of several parser options

# print(soup.prettify()) # prettify makes neat spaces

# html is hierarchical--every subordinate layer is tabbed out. Ignores white space. 

# let's get all the links!
# all links on a webpage have a. <a href _ "www.google.com">
links = soup.find_all("a")
for link in links:
    # print(link.get("href")) # this gets the actual hrls 
    url = link.get("href")
    link_text = link.string # becoming more refined
    # print(f"{link_text}: {url}")

full_text = soup.find_all(text=True)

for item in soup(["script", "style"]): # go into soup and get rid of script objects and style objects. 
    # script: grab <script> and dump
    # style: grab <style> and dump
    item.extract # for any item with a script tag, just go through and dump it. Get rid of it.

# all_text = soup.get_text()
# print(all_text)

lists = soup.find_all("ul") # looking at list of information, third list on the page for https://en.wikipedia.org/wiki/United_States_Attorney_for_the_Southern_District_of_New_York
# it is the second item.
# give me all of the lsits on page, jump to list with attorney generals in it (look at html on page), find all items in list
atts_general = lists[2].find_all("li")

for at in atts_general:
    print(at.get_text())

    atts_general[-1].text

# if it starts with a slash, it is in wiki
# if it starts wtih https:, it is external
# it is almost time to make a crawler that goes through the entire internet

# print(lists[1],get_text) # will give you table of contents?
# ul = these are tags for unordered list. li = list item, an item in the ul list.
# how to get a website's robots: https://facebook.com/robots.txt

# could scrape
# gutenberg
# https://ctext.org don't use that one
# Vierthaler's website
# http://open-lit.com # does not have robots.txt (share and enjoy!) # could reiterate through all these links and download all these pages, but must keep it slow, could add randomness


# AVOID
# User-Agent: * Disallow: /
