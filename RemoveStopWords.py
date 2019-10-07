
import re
import nltk
import ssl
from nltk.corpus import stopwords

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
punctuations = '''!¡¿()-[]{};:'"\,<>./?@#$%^&*_~'''

s_words = set(stopwords.words('spanish'))

def remove_stop_words(given_file):
    new_file = "./FilesWithNoStopWord/" + given_file + "_N_S_Words.txt"
    file_to_write = open(new_file, 'w+')

    candidate_tweets = "./TweetsByCandidates/" + given_file +"_tweets.txt"
    stop_words = set(stopwords.words('spanish'))
    stop_words.add("dr")
    stop_words.add("19")
    stop_words.add("hoy")
    stop_words.add("“")
    stop_words.add("cesarmontufar51")
    stop_words.add("gracias")
    stop_words.add("cada")
    stop_words.add("juntos")
    stop_words.add("ciudad")
    stop_words.add("vamos")
    stop_words.add("día")
    stop_words.add("mañana")
    stop_words.add("lee")
    stop_words.add("uncafeconjj")
    stop_words.add("nota")
    stop_words.add("años")
    stop_words.add("jimmyjairala")
    stop_words.add("lorohomero")
    stop_words.add("hola")
    stop_words.add("pacomoncayo")
    stop_words.add("hacer")
    stop_words.add("puede")
    stop_words.add("días")
    stop_words.add("si")
    stop_words.add("cosas")
    stop_words.add("nota")
    stop_words.add("años")
    stop_words.add("juancaholguin")
    stop_words.add("luisamaldonadom")
    stop_words.add("5")
    stop_words.add("hagamos")
    stop_words.add("vickydesintonio")
    stop_words.add("24")
    stop_words.add("q")
    stop_words.add("x")
    stop_words.add("d")
    stop_words.add("”")
    stop_words.add("httpstcoo9phkbcolh")
    stop_words.add("nadie")
    stop_words.add("obrassincorrupcion")


    file1 = open(candidate_tweets,'r+')
    lines = file1.readlines()  # Use this to read file content as a stream:
    #for each tweet
    for tweet in lines:
        # set string to lower
        sentence = tweet.lower()
        # remove punctuations
        no_punct = ""
        for char in sentence:
            if char not in punctuations:
                no_punct = no_punct + char
        # create a list of all the words
        words = nltk.word_tokenize(no_punct,'spanish')
        # remove the stop words
        filtered_sentence = [w for w in words if not w in stop_words]
        # write to new file
        for word in filtered_sentence:
            file_to_write.write(word + " ")

    print("Done")
    file_to_write.close()
    file1.close()


remove_stop_words('CesarMontufar51')
remove_stop_words("CynthiaViteri6")
remove_stop_words('davalos2019')
remove_stop_words("jimmyjairala")
remove_stop_words("juancaholguin")
remove_stop_words("LoroHomero")
remove_stop_words("LuisaMaldonadoM")
remove_stop_words("PacoMoncayo")
remove_stop_words("VickyDesintonio")
remove_stop_words("wgomezr")