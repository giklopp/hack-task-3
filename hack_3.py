'''
Pick a website and look at its robots.txt. Make sure you are allowed to write a script that can scrape it.
Write a short script that downloads and parses a page from that website.
My chosen website: 
Parsed output should be the plain text of the page, not the HTML.
Script should save this parsed output into a file.
'''

# In order to pull anything off the internet, we must first connect to the internet!
import urllib.request

# I will be parsing this page.
url = "https://en.wikipedia.org/wiki/List_of_Dragon_Ball_Z_episodes"

# Use a request object to get the page here.
request = urllib.request.urlopen(url)

# Use the 'read' function to get the contents.
contents = request.read()

# Close request object
request.close()

# print contents. This gives us the html of this particular page.
# print(contents)

# We want to save these html contents. Don't want to call it everytime we analyze it. Save it as a file.
# Decode the results from bytecode into a string in order to save it to file. 
htmlstring = contents.decode()

with open ("DBZ_Episodes.html", "w", encoding = 'utf8') as wf:
    wf.write(htmlstring)
# This gives us a nice, easy-to-read html. Can open it in Chrome or Visual.

# Now it's time to think about scraping specifically.
# Get information out of a static HTML page.
# Import html parsing library Beautiful Soup. 
from bs4 import BeautifulSoup

# make empty variable to have context manager to open html file, but not have everything indended over.
soup = ""

# rf opens html file.
with open('DBZ_episodes.html', 'r', encoding='utf8') as rf:
    # lxml is a default parser option that tells Beautiful Soup how html will behave.
    soup = BeautifulSoup(rf.read(), 'lxml')
# print(soup.prettify()) # gives you a nice reformatted html.

# Let's get all the links:
links = soup.find_all("a")

# Let's print the text and url for the first link:
linktext = links[2].string # this is actually the 3rd link on the string.
url = links[2].get("href") # inside the html, the actual url is stored inside an href attribute.
print(f"{linktext}: {url}") # print linktext and url.

# look at chosen page. What list do you want to strip out of page?
# get some information off of this page using very sparse html knowledge.

# Find all of the lists on the page:
lists = soup.find_all('ul')

# The second list on the page contains information on all episodes, season 1-9 (in sub lists), of DBZ episodes.
episodes = lists[1].find_all('li')

# print out most recent episode, for some reason. (think of a better idea)
print(f"Most Recent Dragon Ball Z Episode: {episodes[-1].text}")