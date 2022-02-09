# import webbrowser

# from Clearing import Clear
# Clear()


def about(article):
    import wikipedia
    a = wikipedia.summary(article, sentences=8)
    print(a)
    return a
