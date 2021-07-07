def startProcess(URL = "https://coinmarketcap.com/currencies/bitcoin", treshold = 34000):

    import time
    import warnings

    warnings.filterwarnings("ignore")

    treshold = treshold

    def getcoin():

        import requests
        from bs4 import BeautifulSoup

        page = requests.get(URL)

        soup = BeautifulSoup(page.content, "html.parser")

        results = soup.find("div", class_="priceValue___11gHJ")

        currentPrice = results.text[1:]
        currentPrice = currentPrice.replace(',', '');

        print("Current Price: " + currentPrice)

        return float(currentPrice)

    def scream():
        import winsound
        winsound.PlaySound("alert", winsound.SND_FILENAME)

    def checkPrice():
        print("Checking...")

        price = getcoin()
        fprice = '%.8f' % price

        if price < treshold:
            #treshold = price

            scream()

        print("Waiting...")
        time.sleep(60)
        checkPrice()

    checkPrice()

startProcess()