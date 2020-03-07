# In order to pull anything off the internet, we must first connect to the internet!
import urllib.request

# I will be parsing this page.
url = "https://www.w3schools.com/xml/simple.xml"

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

# robots.txt

with open ("menu.html", "w", encoding = 'utf8') as wf:
    wf.write(htmlstring)
# This gives us a nice, easy-to-read html. Can open it in Chrome or Visual.

# Now it's time to think about scraping specifically.
# Get information out of a static HTML page.
# Import html parsing library Beautiful Soup. 
from bs4 import BeautifulSoup

# make empty variable to have context manager to open html file, but not have everything indended over.
soup = ""

# rf opens html file.
with open('menu.html', 'r', encoding='utf8') as rf:
    # lxml is a default parser option that tells Beautiful Soup how html will behave.
    soup = BeautifulSoup(rf.read(), 'lxml')
# print(soup.prettify()) # gives you a nice reformatted html.

# Let's get all the tables:
foodItems = soup.find_all("food")

# Simply get texts from tables or rows. But if you want to get a specific reason, then you need to identify the table at hand. 
# Here, our desired tables seem to be tables 2 to 10 (not including special episodes)
# limit the tables you go through to just those and save the episodes.
breakfast = []
for food in foodItems:
    breakfast.append(foodItems.get_text())

print(breakfast)
