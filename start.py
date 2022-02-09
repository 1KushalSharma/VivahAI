from nltk.tokenize import sent_tokenize
import nltk
import GSearch as gsearch


# from Clearing import Clear


def siteOpener(url):
    import webbrowser
    webbrowser.open(url, new=0, autoraise=True)


# articles = 'Klay Thompson'
# articles = 'Kobe Bryant'


# articles = 'M.S. Dhoni'
# articles = 'Usain Bolt'
#articles = 'Barack Obama'
# articles = 'Shah Rukh Khan'
# articles = 'Lionel Messi'

# Clear()
# nltk.download()
# nltk.download('punkt')
# nltk.download('wordnet')


def nltkProcessing(article):
    from GSearch import gSearch

    nltk.download('stopwords')
    nltk_stopwords = nltk.corpus.stopwords.words('english')
    wordnet_lemmatizer = nltk.stem.WordNetLemmatizer()

    # Clear()
    inputs = ''
    doc = sent_tokenize(article)
    for i, token in enumerate(doc):
        inputs = inputs + token

        tkns = nltk.tokenize.word_tokenize(inputs)
        tkns = [tkn for tkn in tkns if not tkn in nltk_stopwords]
        # print(tkns)
        # print()

        # LEMMATIZER
        for tkn in tkns:
            lemmatized_tkn = wordnet_lemmatizer.lemmatize(tkn)

            if tkn != lemmatized_tkn:
                # print(tkn, ' ', lemmatized_tkn)
                for i in range(len(tkns)):
                    if tkns[i] == tkn:
                        tkns[i] = lemmatized_tkn

        # print(tkns)
        # print()
        ret, listURL = gSearch(tkns)
        if ret == 0:
            UI1 = 'activate'  # not wikipedia page
        else:
            return ret, listURL
        #     siteOpener(ret)  # wikipedia page
        #     siteOpener(ret)  # wikipedia page
        # from UI import UI
        # ui=UI()
        # ui.run()

        # https://github.com/makcedward/nlp


#nltkProcessing(articles)
