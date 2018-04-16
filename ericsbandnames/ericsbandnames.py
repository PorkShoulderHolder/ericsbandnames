from requests import get
from bs4 import BeautifulSoup
import random
import sys

def list_band_names(sep=" ", url="http://ericsbandnames.com"):
    raw = get(url).text
    soup = BeautifulSoup(raw, "html.parser")
    names = [n.string.replace(" ", sep).replace('\r\n','') for n in soup.find(id='content').find_all('li')]
    return names

def random_name(n=1, sep=" ", url="http://ericsbandnames.com"):
    n = int(n)
    names = list_band_names(sep, url)
    if n == 1:
        return random.choice(names)
    elif n > 1 and n < len(names) + 1:
        return random.sample(names, n)
    else:
        raise ValueError("n must be a positive integer less than or equal to {}".format(len(names)))

if __name__ == "__main__":
    if len(sys.argv) >  1:
        print random_name(*sys.argv[1:])
    else:
        print random_name()

