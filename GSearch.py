def siteOpener(url):
    import webbrowser
    webbrowser.open(url, new=0, autoraise=False)


def imageDownload(url):
    import os
    if os.path.exists('./src/wiki.jpg'):
        os.remove('./src/wiki.jpg')
    import requests
    from imageExtract import extractImage
    # URL = 'https://upload.wikimedia.org/wikipedia/commons/thumb/c/c1/Lionel_Messi_20180626.jpg/940px-Lionel_Messi_20180626.jpg'
    URL = extractImage(url)
    # siteOpener(URL)  # wikipedia page
    # siteOpener(URL)  # wikipedia page

    response = requests.get(URL)

    file = open("./src/wiki.jpg", "wb")
    file.write(response.content)
    file.close()
    # from resize import imageResize
    # imageResize()

    return URL


def imageWiki(url):
    # from imageExtract import extractImage
    # imgURL = extractImage(url)
    imgURL = imageDownload(url)
    return imgURL


def gSearch(tkns):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")
    sent = ''
    for i in tkns:
        sent = sent + i
        sent = sent + ' '
    # to search
    query = sent

    print(query)
    sitesList = []
    for j in search(query, tld='co.in', num=5, stop=5, pause=2):
        print(j)
        sitesList.append(j)

    for j in sitesList:
        if "wikipedia" in j:
            imgURL = imageWiki(j)
            return imgURL, sitesList
    for j in sitesList:
        siteOpener(j)
    return 0


def siteOpener(url):
    import webbrowser

    webbrowser.open(url)
