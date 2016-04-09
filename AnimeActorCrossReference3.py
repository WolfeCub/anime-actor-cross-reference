#!/usr/bin/python3
import sys
import pprint
import requests
import lxml
from bs4 import BeautifulSoup

def main():
    usr = input("MAL username: ")

    r = requests.get('http://myanimelist.net/malappinfo.php?u=' + str(usr) + '&status=all&type=anime', headers={"user-agent": "iMAL-iOS"})

    soup = BeautifulSoup(r.text, "lxml-xml")
    titles = soup.find_all('series_title')
    ids = soup.find_all('series_animedb_id')

    total_watched = int(soup.find('user_watching').contents[0]) + int(soup.find('user_completed').contents[0]) +\
            int(soup.find('user_onhold').contents[0]) + int(soup.find('user_dropped').contents[0]) +\
            int(soup.find('user_plantowatch').contents[0])

    counter = 0
    master = {}

    for i in range(len(titles)):
        url = 'http://myanimelist.net/anime/' + str(ids[i].contents[0]) + '/' +\
                titles[i].string.replace(' ', '_') + '/characters'

        r = requests.get(url, headers={"user-agent": "iMAL-iOS"})

        temp = None

        soup = BeautifulSoup(r.text, "lxml")
        for k in soup.find_all('tr'):
            for j in k.children:
                if j.name != None and j.a != None:
                    att = j.attrs
                    if 'width' not in att and 'valign' in att and 'class' in att and att['valign'] == 'top':
                        if temp == None:
                            if j.small.contents[0] == 'Main' or j.small.contents[0] == 'Supporting' or \
                                    j.small.contents[0] == 'Japanese':
                                        temp = j.a.contents[0]
                        else:
                            if j.a.contents[0] in master:
                                master[j.a.contents[0]].append((titles[i].string, temp))
                            else:
                                master[j.a.contents[0]] = [(titles[i].string, temp)]
                            temp = None

        counter += 1
        sys.stdout.write('\r')
        sys.stdout.write(str(counter) + '/' + str(total_watched))
        sys.stdout.flush()

    sys.stdout.write('\r')
    display(master)

def display(dict):
    for key in dict:
        print(key)
        for j in dict[key]:
            print('\t' + j[0] + ' - ' + j[1])

if __name__ == "__main__": main()
