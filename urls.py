# from Clearing import Clear

# Clear()
def imageDownload(url):    
    import os
    if os.path.exists('./src/wiki.jpg'):
        os.remove('./src/wiki.jpg')
        
    import requests
    # url = 'https://upload.wikimedia.org/wikipedia/en/0/0d/Avengers_Endgame_poster.jpg'

    response = requests.get(url)

    file = open("./src/wiki.jpg", "wb")
    file.write(response.content)
    file.close()
    
def siteOpener(url):
    import webbrowser
    webbrowser.open(url,new=2, autoraise=False)
    
def brow(url):    
    # importing webdriver from selenium
    from selenium import webdriver
    
    # Here Chrome  will be used
    driver = webdriver.Chrome()
    
    # URL of website
    # url = "https://www.geeksforgeeks.org/"
    
    # Opening the website
    driver.get(url)
    
    # All windows related to driver instance will quit
    driver.quit()
    
u = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Lionel_Messi_20180626.jpg/940px-Lionel_Messi_20180626.jpg'
imageDownload(u)
# siteOpener(u)