import requests
from bs4 import BeautifulSoup

URL = "https://nostarch.com"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

#finding the book titles
elements = soup.find_all("div", class_="field field-name-field-image-cache field-type-image field-label-hidden")


#parsing them 
for element in elements:
    title=element.img["alt"]
    print(title)

#finding the writers
elements2 = soup.find_all("div", class_="field field-name-field-author field-type-text field-label-hidden")
for element in elements2:
    writer=element.find("div",class_="field-item even")
    print(writer.text.strip())


#find all links in the page
all_hrefs = [a.get('href') for a in soup.find_all('a')]
print(all_hrefs)




#finish