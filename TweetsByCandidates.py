import pandas
from Main import load_pickle

def get_top_ten_candidates():
    candidate_list = []
    with open("top10.txt", "r+") as f:
        line = f.readline()
        candidate_list.append(line.rstrip())
        cnt = 1
        while line:
            line = f.readline()
            candidate_list.append(line.rstrip())
            cnt += 1
    candidate_list.pop()
    return candidate_list

def get_file_for_each(candidate_list):
    tweets_df = load_pickle()
    # ['tweet_id', 'tweet_date', 'tweet_screen_name', 'tweet_text']
    tweet_dictionary = {}
    for candidate in candidate_list:
        tweet_dictionary[candidate] = []
    counter = 0
    for index, row in tweets_df.iterrows():
        if row['tweet_screen_name'] in candidate_list:
            tweet_dictionary[row['tweet_screen_name']].append(row['tweet_text'])
        counter += 1
        if counter % 10000 == 0:
            print(counter)

    for key in tweet_dictionary:
        print(key + " " + str(len(tweet_dictionary[key])))

    return tweet_dictionary

def send_each_to_file(tweet_dictionary):
    for key in tweet_dictionary:
        new_file = open(key + "_tweets.txt", "w+")
        for tweet in tweet_dictionary[key]:
            new_file.write(tweet)
        new_file.close()



x = {"aaron":['hola','chao'],"sharon":['hola','chao'], "olivia":['hola','chao']}
#send_each_to_file(x)
send_each_to_file(get_file_for_each(get_top_ten_candidates()))
#get_file_for_each(get_top_ten_candidates())
