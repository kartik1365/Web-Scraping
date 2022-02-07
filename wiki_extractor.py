import argparse
from ast import arg, keyword
from cgitb import html
from html.parser import HTMLParser
import requests
from bs4 import BeautifulSoup as bs
from itertools import islice

parser = argparse.ArgumentParser()
parser.add_argument('--keyword',type=str,required=True)
parser.add_argument('--num_urls',type=int,required=True)
parser.add_argument('--output', help='Output synthesis script', required=True)

args = parser.parse_args()
print("given inputs - ")
print('To find - ' , args.keyword)
print('Number of Urls - ' ,args.num_urls)
print('Direct the o/p to - ', args.output)

N = args.num_urls 
key = args.keyword
output_file = args.output

keyword_str = "https://en.wikipedia.org/w/index.php?title=Special:Search&limit="+str(N)+"&offset=20&profile=default&search="+ key + "&ns0=1"
res = requests.get(keyword_str)
soup = bs(res.text, "html.parser")
links = []

for link in soup.find_all("a"):
    url = link.get("href", "")
    if '#' in url or url.strip() == '' or 'Help' in url:
        continue
    if '/wiki/' in url:
        links.append(url)

for i in links[: N]:
    print(i)

cnt = 0
output_text = ''
for i in links[: N]:
    contents = requests.get("https://en.wikipedia.org" + i)
    soup = bs(contents.text,'html.parser')
    rows = soup.find_all('p')
    for row in rows:          # Print all occurrences
        if row.get_text().strip() != '':
            if len(row.get_text()) < 60:
                continue
            output_text += "url - https://en.wikipedia.org" + i + '\n'
            output_text += "paragraph - " + row.get_text().rstrip("\n")
            output_text += "\n" + "\n"
            print('Task', cnt ,' Done!')
            cnt += 1
            break

outF = open(output_file, "w")
outF.write(output_text)
outF.close()