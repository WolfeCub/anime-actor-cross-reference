import requests
import lxml
from bs4 import BeautifulSoup

def main():
    usr = "Psyonic" #input("MAL username: ")
    r = requests.get('http://myanimelist.net/malappinfo.php?u=' + str(usr) + '&status=all&type=anime')

    soup = BeautifulSoup(r.text, "lxml-xml")
    titles = soup.find_all('series_title')
    ids = soup.find_all('series_animedb_id')
    
    titles = ["Golden Time"]
    ids = [17895]

    for i in range(len(titles)):
        url = 'http://myanimelist.net/anime/' + str(ids[i]) + '/' +\
                titles[i].replace(' ', '_') + '/characters'

        r = requests.get(url)

        soup = BeautifulSoup(r.text, "lxml")
        print(soup.find_all())


if __name__ == "__main__": main()
