# Stuart Spiegel
# Date: 2/19/2019

from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse


class LinkParser(HTMLParser):

    def main(self):
        LinkParser.Spider("www.google.com", "search", 10)


    def Spider(url, word, maxPages):
        pagesToVisit = [url]
        numberVisited = 0
        foundWord = False

        while numberVisited < maxPages and pagesToVisit != [] and not foundWord:
            numberVisited = numberVisited + 1
            url = pagesToVisit[0]
            pagesToVisit = pagesToVisit[1:]
            try:
                print(numberVisited, "Visiting:", url)
                parser = LinkParser()
                data, links = parser.getLinks(url)
                if data.find(word) > -1:
                    foundWord = True
                pagesToVisit = pagesToVisit + links
                print("--Success--")
            except:
                print("--Failed--")

        if foundWord:
            print("The word", word, "was found at", url)
        else:
            print("Word Never Found")
