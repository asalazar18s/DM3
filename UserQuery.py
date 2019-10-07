from Main import load_pickle
import datetime
from collections import Counter
from TermFrequency import get_term_frequency

candidates = ['CesarMontufar51', "CynthiaViteri6", 'davalos2019', "jimmyjairala", "juancaholguin", "LoroHomero",
              "LuisaMaldonadoM", "PacoMoncayo", "VickyDesintonio", "wgomezr"]
t_dictionary = load_pickle()


def get_tweets_by_month(candidate_list, dict):
    tweets_df = dict
    # ['tweet_id', 'tweet_date', 'tweet_screen_name', 'tweet_text']
    tweet_month_dictionary = {}
    for candidate in candidate_list:
        tweet_month_dictionary[candidate] = {1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[],10:[],11:[],12:[]}
    counter = 0
    for index, row in tweets_df.iterrows():
        # if its one of the candidates in the list
        if row['tweet_screen_name'] in candidate_list:
            date_time = row['tweet_date']
            tweet_month_dictionary[row['tweet_screen_name']][date_time.month].append(row['tweet_text'])
        counter += 1
        if counter % 10000 == 0:
            print(counter)

    return tweet_month_dictionary


final_dictionary = get_tweets_by_month(candidates, t_dictionary)


def get_top_ten_word_freq(file_name):
    file_to_read = open("./TermFrequencyByCandidate/" + file_name + "_W_Frequency.txt", 'r+')
    x = file_to_read.readlines()
    top_ten_list = []
    counter = 0
    for line in x:
        temp = line.split(":")
        top_ten_list.append(temp[0].rstrip())
        counter += 1
        if counter > 9:
            break

    return top_ten_list


def get_freq_of_word_by_month(candidate):
    global t_dictionary, final_dictionary
    words = get_top_ten_word_freq(candidate)
    tweet_dictionary = final_dictionary
    new_dict = {}
    # for each of the top ten words
    for word in words:
        # for the given candidate for each month
        new_dict[word] = {}
        for month in tweet_dictionary[candidate]: # 1->12
            # if there are tweets in the month
            if len(tweet_dictionary[candidate][month]) > 0:
                # give the month an initial value of 0
                new_dict[word][month] = 0
                # for every tweet
                for tweet in tweet_dictionary[candidate][month]:
                    # turn everythong to lowercase
                    temp = tweet.lower()
                    # if the current word exists in the tweet
                    if word in temp:
                        # add to the value of the given month
                        new_dict[word][month] = new_dict[word][month] + 1

    return new_dict

def to_file_by_month(candidate,month_dictionary):
    file_name_feb = "./Candidates/" + candidate + "/" + "Feb.txt"
    file_to_write_feb = open(file_name_feb, 'w+')
    file_name_mar = "./Candidates/" + candidate + "/" + "Mar.txt"
    file_to_write_mar = open(file_name_mar, 'w+')
    file_name_may = "./Candidates/" + candidate + "/" + "May.txt"
    file_to_write_may = open(file_name_may, 'w+')
    file_name_abr = "./Candidates/" + candidate + "/" + "Abr.txt"
    file_to_write_abr = open(file_name_abr, 'w+')
    for word in month_dictionary:
        for month in month_dictionary[word]:
            if month == 2:
                file_to_write_feb.write(word + " : " + str(month_dictionary[word][month]) + "\n")
            elif month == 3:
                file_to_write_mar.write(word + " : " + str(month_dictionary[word][month]) + "\n")
            elif month == 4:
                file_to_write_abr.write(word + " : " + str(month_dictionary[word][month]) + "\n")
            elif month == 5:
                file_to_write_may.write(word + " : " + str(month_dictionary[word][month]) + "\n")

    file_to_write_feb.close()
    file_to_write_mar.close()
    file_to_write_abr.close()
    file_to_write_may.close()



for candidate in candidates:
    to_file_by_month(candidate, get_freq_of_word_by_month(candidate))
    print("Done " + candidate)



