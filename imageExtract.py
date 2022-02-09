from bs4 import *
# from Clearing import Clear

# Clear()


def siteOpener(url):
    import webbrowser
    webbrowser.open(url)


def extractImage(url):
    import re
    import requests
    # upload.wikimedia.org/wikipedia/en/thumb/1/1b/Semi-protection-shackle.svg/20px-Semi-protection-shackle.svg.png

    # Fetch URL Content
    r = requests.get(url)

    # Get body content
    soup = BeautifulSoup(r.text, 'html.parser').select('body')[0]

    # Initialize variable
    paragraphs = []
    images = []
    link = []
    heading = []
    remaining_content = []

    # Iterate throught all tags
    for tag in soup.find_all():

        if tag.name == "img":

            # Add url and Image source URL
            images.append(url+tag['src'])

    count = -1
    req = ''
    name = url.replace('https://en.wikipedia.org/wiki', '')
    # print(name)
    for i in images:
        # print(i)
        count += 1
        if i.endswith("upload.wikimedia.org/wikipedia/en/thumb/1/1b/Semi-protection-shackle.svg/20px-Semi-protection-shackle.svg.png") or i.endswith('upload.wikimedia.org/wikipedia/en/thumb/8/8c/Extended-protection-shackle.svg/20px-Extended-protection-shackle.svg.png'):
            # print(count)
            # print(len(images))
            req = images[count+1]
            reqCount = count

    if (req.find(name) != -1):
        print('FOUND')
    else:
        req = images[reqCount+2]

    req = req.replace(url, '')
    req = 'https:' + req.replace('220px', '600px')
    print(req)
    siteOpener(req)
    return req


# extractImage('https://en.wikipedia.org/wiki/Forest')
