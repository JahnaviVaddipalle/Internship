#!/usr/bin/env python
# coding: utf-8

# # Wikipedia
# 

# In[16]:


get_ipython().system('pip install bs4')
get_ipython().system('pip install requests')


# In[25]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[26]:


page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
page


# In[39]:


soup = BeautifulSoup(response.text, "html.parser")
soup


# In[41]:


header_tags = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
header_text = [tag.text.strip() for tag in header_tags]

header_text


# In[42]:


df = pd.DataFrame({"Headers": header_text})
df


# #  List of former presidents of India(i.e. Name , Term ofoffice) in data frame.

# In[1]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[2]:


page = requests.get("https://presidentofindia.nic.in/former-presidents.htm")
page


# In[3]:


soup = BeautifulSoup(page.content)
soup


# In[4]:


first_title = soup.find('div', class_="presidentListing")

first_title


# In[8]:


first_title.text
first_title.text.split('(')[0]


# In[11]:


term = soup.find('span',class_="terms")
term


# In[43]:


paragraphs = soup.find('div', class_="presidentListing")


# In[44]:


paragraphs


# In[24]:


titles =[]

for i in soup.find_all('div', class_="presidentListing"):
    titles.append(i.text)

formatted_titles = [title.split('(')[0].strip() for title in titles]
print(formatted_titles)


# In[36]:


term = []

for i in soup.find_all('p'):
    term.append(i.text)

Term_of_service = [i.split(':')[1].strip() for i in term if len(i.split(':')) > 1]
print(Term_of_service)


# In[28]:


len(term)


# In[55]:


len(formatted_titles)


# In[45]:


term = []

for i in soup.find_all('div', class_="presidentListing"):
    term.append(i.text)

Term_of_service = [i.split(':')[1].strip() for i in term if len(i.split(':')) > 1]
print(Term_of_service)


# In[47]:


len(Term_of_service)


# In[60]:


df = pd.DataFrame({'Title':formatted_titles,'TermofOffice':Term_of_service})


# In[61]:


df


# # Top 10 ODI teams in men’s cricket with the records for matches, points & rating.

# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[3]:


odi = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi")
odi


# In[4]:


soup = BeautifulSoup(odi.content)
soup


# In[5]:


table = soup.find("table", class_="table")
teams = []
rows = table.tbody.find_all('tr')
for row in rows:
    cols = row.find_all("td")
    teams.append(cols[1].get_text(strip=True))
teams


# In[6]:


matches = []
rows = table.tbody.find_all('tr')
for row in rows:
    cols = row.find_all("td")
    matches.append(cols[2].get_text(strip=True))
matches


# In[7]:


points = []

rows =table.tbody.find_all('tr')
for row in rows:
    cols = row.find_all("td")
    points.append(cols[3].get_text(strip=True))
points


# In[8]:


ratings =[]

rows = table.tbody.find_all('tr')
for row in rows:
    cols = row.find_all("td")
    ratings.append(cols[4].get_text(strip=True))
ratings
    


# In[9]:


df = pd.DataFrame({'Teams':teams,'Matches':matches,'Points':points,'Ratings':ratings})
df.head(10)


# # Top 10 ODI Batsmen along with the records of their team andrating.

# In[13]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[14]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting")
page


# In[15]:


soup = BeautifulSoup(page.content)
soup


# In[16]:


player =soup.find('div',class_="rankings-block__banner--name-large")
formated_player=player.text
formated_player


# In[17]:


team = soup.find('div',class_="rankings-block__banner--nationality")
team=team.text
team


# In[18]:


rating = soup.find('div',class_="rankings-block__banner--rating")
rating=rating.text
rating


# In[19]:


players = []
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    players.append(i.text)
players=players[:9]
players.insert(0,formated_player)
print(players)


# In[20]:


teams = []
for i in soup.find_all('span',class_="table-body__logo-text"):
    teams.append(i.text)
teams=teams[:9]
teams.insert(0,team)
print(teams)


# In[21]:


ratings = []
for i in soup.find_all('td',class_="table-body__cell rating"):
    ratings.append(i.text)
ratings=ratings[:9]
ratings.insert(0,rating)
print(ratings)


# In[22]:


df=pd.DataFrame({'Players':players,'Teams':teams,'Ratings':ratings})
df


# # Top 10 ODI bowlers along with the records of their team andrating.

# In[23]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[24]:


page = requests.get("https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling")
page


# In[25]:


soup = BeautifulSoup(page.content)
soup


# In[26]:


player =soup.find('div',class_="rankings-block__banner--name-large")
formated_player=player.text
formated_player


# In[27]:


team = soup.find('div',class_="rankings-block__banner--nationality")
team=team.text
team


# In[28]:


rating = soup.find('div',class_="rankings-block__banner--rating")
rating=rating.text
rating


# In[29]:


players = []
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    players.append(i.text)
players=players[:9]
players.insert(0,formated_player)
print(players)


# In[30]:


teams = []
for i in soup.find_all('span',class_="table-body__logo-text"):
    teams.append(i.text)
teams=teams[:9]
teams.insert(0,team)
print(teams)


# In[31]:


ratings = []
for i in soup.find_all('td',class_="table-body__cell rating"):
    ratings.append(i.text)
ratings=ratings[:9]
ratings.insert(0,rating)
print(ratings)


# In[32]:


df=pd.DataFrame({'Players':players,'Teams':teams,'Ratings':ratings})
df


# # Top 10 ODI teams in women’s cricket along with the records for matches, points and rating.

# In[61]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[62]:


page = requests.get("https://www.icc-cricket.com/rankings/womens/team-rankings/odi")
page


# In[63]:


soup = BeautifulSoup(page.content)
soup


# In[64]:


table = soup.find("table", class_="table")
teams = []
rows = table.tbody.find_all('tr')
for row in rows:
    cols = row.find_all("td")
    teams.append(cols[1].get_text(strip=True))
teams


# In[65]:


matches = []
rows = table.tbody.find_all('tr')
for row in rows:
    cols = row.find_all("td")
    matches.append(cols[2].get_text(strip=True))
matches


# In[66]:


points = []

rows =table.tbody.find_all('tr')
for row in rows:
    cols = row.find_all("td")
    points.append(cols[3].get_text(strip=True))
points


# In[67]:


ratings =[]

rows = table.tbody.find_all('tr')
for row in rows:
    cols = row.find_all("td")
    ratings.append(cols[4].get_text(strip=True))
ratings


# In[68]:


df = pd.DataFrame({'Teams':teams,'Matches':matches,'Points':points,'Ratings':ratings})
df=df.head(10)
df


# # Top 10 women’s ODI Batting players along with the records of their team and rating.

# In[9]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[10]:


page = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/batting")
page


# In[11]:


soup = BeautifulSoup(page.content)
soup


# In[12]:


player =soup.find('div',class_="rankings-block__banner--name-large")
formated_player=player.text
formated_player


# In[13]:


team = soup.find('div',class_="rankings-block__banner--nationality")
team=team.text
team


# In[14]:


rating = soup.find('div',class_="rankings-block__banner--rating")
rating=rating.text
rating


# In[15]:


players = []
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    players.append(i.text)
players=players[:9]
players.insert(0,formated_player)
print(players)


# In[16]:


teams = []
for i in soup.find_all('span',class_="table-body__logo-text"):
    teams.append(i.text)
teams=teams[:9]
teams.insert(0,team)
print(teams)


# In[17]:


ratings = []
for i in soup.find_all('td',class_="table-body__cell rating"):
    ratings.append(i.text)
ratings=ratings[:9]
ratings.insert(0,rating)
print(ratings)


# In[18]:


df=pd.DataFrame({'Players':players,'Teams':teams,'Ratings':ratings})
df


# # Top 10 women’s ODI all-rounder along with the records of their team and rating.

# In[19]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[20]:


page = requests.get("https://www.icc-cricket.com/rankings/womens/player-rankings/odi/all-rounder")
page


# In[21]:


soup = BeautifulSoup(page.content)
soup


# In[22]:


player =soup.find('div',class_="rankings-block__banner--name-large")
formated_player=player.text
formated_player


# In[23]:


team = soup.find('div',class_="rankings-block__banner--nationality")
team=team.text
team


# In[24]:


rating = soup.find('div',class_="rankings-block__banner--rating")
rating=rating.text
rating


# In[25]:


players = []
for i in soup.find_all('td',class_="table-body__cell rankings-table__name name"):
    players.append(i.text)
players=players[:9]
players.insert(0,formated_player)
print(players)


# In[26]:


teams = []
for i in soup.find_all('span',class_="table-body__logo-text"):
    teams.append(i.text)
teams=teams[:9]
teams.insert(0,team)
print(teams)


# In[27]:


ratings = []
for i in soup.find_all('td',class_="table-body__cell rating"):
    ratings.append(i.text)
ratings=ratings[:9]
ratings.insert(0,rating)
print(ratings)


# In[28]:


df=pd.DataFrame({'Players':players,'Teams':teams,'Ratings':ratings})
df


# # python program to scrape news details from https://www.cnbc.com/world/?region=world and make data frame-
# i) Headline ii) Time iii) News Link

# In[29]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[30]:


page = requests.get("https://www.cnbc.com/world/?region=world")
page


# In[31]:


soup = BeautifulSoup(page.content)
soup


# In[32]:


title = []
for i in soup.find_all('div',class_="RiverHeadline-headline RiverHeadline-hasThumbnail"):
    title.append(i.text)
title


# In[39]:


time =[]
for i in soup.find_all('span',class_="RiverByline-datePublished"):
    time.append(i.text)
time


# In[34]:


link = []
for i in soup.find_all('a',class_="LatestNews-headline"):
    link.append(i.get('href'))
link


# In[35]:


len(title),len(time),len(link)


# In[36]:


title = title[:6]  
print(title) 


# In[37]:


link = link[:6]  
print(link) 


# In[38]:


df=pd.DataFrame({'Headline':title,'Time':time,'News Link':link})
df


# # python program to scrape the details of most downloaded articles from AI in last 90 days.https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles¶
# i) Paper Title ii) Authors iii) Published Date iv) Paper URL

# In[40]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[41]:


page = requests.get("https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles")
page


# In[42]:


soup= BeautifulSoup(page.content)
soup


# In[43]:


title = []
for i in soup.find_all('h2',class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    title.append(i.text)
title


# In[44]:


authors=[]
for i in soup.find_all('span',class_="sc-1w3fpd7-0 dnCnAO"):
    authors.append(i.text)
authors


# In[45]:


dates=[]
for i in soup.find_all('span',class_="sc-1thf9ly-2 dvggWt"):
    dates.append(i.text)
    
dates


# In[46]:


url = []
for i in soup.find_all('a',class_="sc-5smygv-0 fIXTHm"):
    url.append(i.get('href'))
url


# In[47]:


len(title),len(authors),len(dates),len(url)


# In[50]:


df=pd.DataFrame({'Paper Title':title,'Authors':authors,'Published Date':dates,'Paper URL':url})
df=df.head(10)
df


# # Write a python program to scrape mentioned details from dineout.co.in and make data frame-
# i) Restaurant name ii) Cuisine iii) Location iv) Ratings v) Image URL

# In[51]:


import requests
import pandas as pd
from bs4 import BeautifulSoup


# In[52]:


page = requests.get("https://www.dineout.co.in/delhi-restaurants/buffet-special")
page


# In[53]:


soup= BeautifulSoup(page.content)
soup


# In[54]:


titles = []
for i in soup.find_all('a',class_="restnt-name ellipsis"):
    titles.append(i.text)
titles


# In[55]:


cuisine = []
for i in soup.find_all('span',class_="double-line-ellipsis"):
    cuisine.append(i.text.split('|')[1])
cuisine


# In[56]:


locations = []

for i in soup.find_all('div',class_="restnt-loc ellipsis"):
    locations.append(i.text)

locations


# In[57]:


rating =[]
for i in soup.find_all('div',class_="restnt-rating rating-4"):
    rating.append(i.text)
rating


# In[58]:


images = []
for i in soup.find_all('img',class_="no-img"):
    images.append(i.get('data-src'))

images


# In[59]:


df=pd.DataFrame({'Restaurant Name':titles,'Cuisine':cuisine,'Locations': locations,'Rating':rating,'image URL':images})
df


# In[ ]:




