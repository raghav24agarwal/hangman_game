from plyer import notification
import requests
from bs4 import BeautifulSoup
import time


def notifyMe(title,message):
    notification.notify(
        title = title,
        message = message,
        app_icon = r"C:\Users\Public.cz-PC\Downloads\corona.ico",
        timeout = 3
    )


def getData(url):
    r = requests.get(url)
    return r.text

if __name__ == "__main__":
    while True:
        #notifyMe("Raghav","Lets stop corona")
        myHtmlData = getData(r"https://www.mohfw.gov.in/")
        #print(myHtmlData)
        soup = BeautifulSoup(myHtmlData,'html.parser')
        #print(soup.prettify())

        #for table in soup.find_all('table'):
            #print(table.get_text())

        myDataStr = ""
        for tr in soup.find_all('tbody')[7].find_all('tr'):
            #print(tr.get_text())
            myDataStr += tr.get_text()
        myDataStr = myDataStr[1:]
            
        itemList = myDataStr.split("\n\n")

        states = ["Goa" , "Delhi" , "Maharashtra"]
        for item in itemList[0:21]:
            dataList = item.split("\n")
            if dataList[1] in states:
                print(dataList)
                nTitle = "Cases of Covid-19"
                nText = f"State : {dataList[1]} \nIndian : {dataList[2]} Foreign : {dataList[3]} \nCured : {dataList[4]} \nDeath : {dataList[5]}"
                notifyMe(nTitle,nText)
                time.sleep(4)

        
