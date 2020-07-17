import re
import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import init, Style

def createFile(url, content):
    filename = directory + '\\' + re.sub("https://", ".com", url) + '.txt'
    print(filename)
    with open(filename, 'w+', encoding="utf-8") as file:
        file.write(content)
        file.seek(0)
        for line in file:
            if "blue_font_here " in line:
                print(blue + line.lstrip("blue_font_here "))
            else:
                print(line)
        print(Style.RESET_ALL)

def readFile(url):
    try:
        filename = directory + re.sub("https://", ".com", url) + '.txt'
        with open(filename, 'r', encoding="utf-8") as file:
            for line in file:
                if "blue_font_here " in line:
                    print(blue + line.lstrip("blue_font_here "))
                else:
                    print(line)
        print(Style.RESET_ALL)
    except FileNotFoundError:
        print("function Error! Enter a valid URL.")


# write your code here

directory = sys.argv[1]
choice = True
pages = []
blue='\033[34m'

if not (os.path.exists(directory)):
    os.mkdir(directory)

while choice:
    url = input()

    if "." not in url:
        if url != 'exit':
            read_url = ''
            for i in pages:
                if url in i:
                    read_url = i
            try:
                r = requests.get(read_url if "https://" in read_url else "https://" + read_url)
                if url == 'back':
                    if len(pages) == 1:
                        pass
                    else:
                        pages.pop()
                        readFile(pages[-1])
                elif r:
                    readFile(url)
                    pages.append(url)
            except requests.exceptions.InvalidURL:
                print("Error! Enter a valid URL.")
                continue
        elif url == 'exit':
            choice = False

    else:
        r = requests.get(url if "https://" in url else "https://" + url)
        soup = BeautifulSoup(r.content, 'html.parser')
        content = ''
        for i in soup.find_all(['p','a','ul','ol',re.compile('^h[1-6]$')]):
            if i.has_attr('href'):
                content += "blue_font_here " + i.get_text() + '\n'
            else:
                content += i.get_text() + '\n'

        if r:
            createFile(url, content)
            pages.append(url)
            print(pages)
        else:
            print("Error! Enter a valid URL.")

