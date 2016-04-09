#!/usr/local/bin/python
import sys
import re
import urllib2

def main():
    usr = raw_input("MAL username: ")
    response = urllib2.urlopen('http://myanimelist.net/malappinfo.php?u=' + str(usr) + '&status=all&type=anime')
    html = response.read()

    m = re.findall('<series_animedb_id>(\d*?)</series_animedb_id><series_title>(.*?)</series_title>', html)

    total_watched = int(re.findall('<user_watching>(.*?)</user_watching>', html)[0]) + int(re.findall('<user_completed>(.*?)</user_completed>', html)[0]) +\
            int(re.findall('<user_onhold>(.*?)</user_onhold>', html)[0]) + int(re.findall('<user_dropped>(.*?)</user_dropped>', html)[0]) +\
            int(re.findall('<user_plantowatch>(.*?)</user_plantowatch>', html)[0])

    master = []

    counter = 0
    for tup in m:
        url = 'http://myanimelist.net/anime/' + str(tup[0])

        response = urllib2.urlopen(url)
        html = response.read()

        info = re.findall('<div class="picSurround"><a href="/character/\d*?/.*?" style="font-weight: normal;"><img src="http://cdn.myanimelist.net/r/.*?" alt="(.*?)" vspace="4" hspace="8" border="0"></a></div>\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*\n.*?<td valign="top"><div class="picSurround"><a href="/people/\d*?/.*?"><img src="http://cdn.myanimelist.net/r/.*?" alt="(.*?)"', html)

        for i in info:
            temp = []
            temp.append(i[1])
            temp.append((tup[1], i[0]))
            index = check(master, i[1])
            if index == None:
                master.append(temp)
            else:
                master[index].append(temp[1])
        counter += 1
        sys.stdout.write('\r')
        sys.stdout.write(str(counter) + '/' + str(total_watched))
        sys.stdout.flush()

    sys.stdout.write('\r')
    display(master)

def check(master, name):
    for i in range(0, len(master)):
        if master[i][0] == name:
            return i;
    return None

def display(master):
    for i in master:
        print(i[0])
        for j in range(1, len(i)):
            print('\t' + str(i[j]))

if __name__ == "__main__": main()
