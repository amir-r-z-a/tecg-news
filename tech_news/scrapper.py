from selenium import webdriver
from urllib.parse import urlparse
# import requests
from selenium.webdriver.common.keys import Keys
# from Selenium.webdriver.common.by import By
from selenium.webdriver.common.by import By
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "tech_news.settings")
django.setup()
from news.models import News, Tag

expected_domain = "https://www.zoomit.ir/"


def check_domain(url, expected_domain):
    parsed_url = urlparse(url)
    extracted_domain = f"{parsed_url.scheme}://{parsed_url.netloc}/"

    return extracted_domain == expected_domain


driver = webdriver.Chrome()
driver.get("https://www.zoomit.ir/archive/?sort=Newest")
# print("hi1")
elements = driver.find_elements(By.CLASS_NAME, "BrowseArticleListItemDesktop__ArticleCard-zb6c6m-0")
# print(elements)
x = []
y = []
for e in elements:
    x.append(e.find_elements(By.TAG_NAME, "p"))

for e in elements:
    y.append(e.find_elements(By.TAG_NAME, "a"))

# print(x)
# print(y)

linkes = []

for i in y:
    for j in i:
        linkes.append(j.get_attribute("href"))

# print(linkes)

title = ""
tags = []
tag_objects = []
contents = []
text = ""
for i in range(len(linkes)):
    if i % 2 == 0:
        if not (check_domain(linkes[i], expected_domain)):
            print("not here")
            continue
        try:
            driver.get(linkes[i])
        except:
            continue
        contents = driver.find_elements(By.CLASS_NAME, "gOVZGU")
        for content in contents:
            # print(content.text)
            # print("'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''")
            try:
                text = text + content.text
            except:
                continue

        title = driver.find_element(By.TAG_NAME, "h1").text
        news = News(title=title, text=text)
        news.save()

        # print(titles)
        # print(driver.find_element(By.CLASS_NAME, "BlockContainer__InnerArticleContainer-i5s1rc-1").find_elements(By.TAG_NAME, "a"))
        tags.append(driver.find_element(By.CLASS_NAME, "BlockContainer__InnerArticleContainer-i5s1rc-1").find_elements(
            By.CLASS_NAME, value="eMeOeL"))
        for j in tags:
            for k in range(len(j)):
                obj = Tag.objects.get_or_create(name=j[k].text)
                tag_objects.append(obj[0])
        for l in tag_objects:
            news.tag_set.add(l)
        print("--------------------------------------------------")
        tags.clear()
        title = ""
        text = ""
