from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
from urllib.request import Request
import ssl


PIRATE_LINKS = False

def main():
    tester = input("Search the seven seas: ")
    x = search(tester)

def search(query):
    """
    Searches the pirate bay for torrents, returns list
    with title, link, size, seeders, leechers
    """
    # set base url and get user input
    url = "https://tpb.party/search/"

    # add split to url
    split = query.split()
    for word in split:
        if split[len(split) - 1] == word:
            url += word
        else:
            url += word + "%20"
    url += '/1/99/100,200,300,400,600'

    # open connection and grab page
    context = ssl._create_unverified_context()

    req = Request(
        url, 
        data=None, 
        headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'
        }
    )
    client = uReq(req,context=context)


    html = client.read()
    client.close()

    # create soup class
    souped = soup(html, "html.parser")

    # create search for each elements
    searchTitle = souped.findAll("div",{"class":"detName"})
    searchSeeders = souped.findAll("td",{"align":"right"})
    searchSize = souped.findAll("font",{"class":"detDesc"})
    searchLink = souped.findAll("a",{"title":"Download this torrent using magnet"})
        
    # name and open csv for writing
    # filename = "movies.csv"
    # f = open(filename, "w")
    # headers = "title, link, size, seeders, leechers\n"
    # f.write(headers)

    #loop for each item
    newList = []
    linkList = []
    for i in range(len(searchTitle)):
        # normalize searches
        title = searchTitle[i].a["title"][len("details for "):]
        seeders = searchSeeders[i*2].string
        leechers = searchSeeders[i*2+1].string
        magnet = searchTitle[i].a["href"]

        # determine wether urls or magnet links
        if PIRATE_LINKS:
            magnet = searchTitle[i].a["href"]
        else:  
            magnet =searchLink[i]["href"]

        # get size
        size = ""
        cache = str(searchSize[i]).split()
        for j in range(len(cache)):
            if cache[j] == "Size":
                size += cache[j+1] + cache[j+2][:1]

        #print testing
        # print("\n" + str(i+1) + ": " + title)
        # print("Seeders: " + seeders + " Leechers: " + leechers)
        # print("Size: " + size) 
        # print("Link: " + magnet + "\n")

        # f.write(title + "," + magnet + "," + size + "," + seeders + "," + leechers + "\n")
        newList += [ [title, magnet, size, seeders, leechers ] ]
        linkList += [magnet]

    newStr = ""
    for i in range(len(newList)):
        for j in range(len(newList[i])):
            if j == 0:
                newStr += "Title: " + newList[i][j] + "\n"
            if j == 1:
                newStr += "Link: " + newList[i][j] + "\n"
            if j == 2:
                newStr += "Size: " + newList[i][j] + "\n"
            if j == 3:
                newStr += "Seeders: " + newList[i][j] + "\n"
            if j == 4:
                newStr += "Leechers: " + newList[i][j] + "\n\n"
        
    # close csv file
    # f.close()
    print(newStr)
    return newStr, linkList
    
if __name__ == '__main__':
    main()