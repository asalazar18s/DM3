import pickle
import pandas as pd
import numpy as np
import csv

def load_pickle():
    '''
    Loads the Pickle file to memory and returns the pd Dataframe
    :return: pandas Dataframe
    '''
    pickle_file = "obj_livetweets_pandasdataframe.pkl"
    unpickled_df = pd.read_pickle(pickle_file)
    x = list(unpickled_df.columns)
    return unpickled_df


def get_candidates():
    '''
    Gets the candidates and separates them into two lists
    :return: single dictionary with keys as candidate tweet_screen_name's
    '''
    candidate_dictionary = {}
    with open('account_info.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                candidate_dictionary[row[6]] = 0
                line_count += 1
        print(f'Processed {line_count} lines.')
    return candidate_dictionary


def get_candidate_occurrence(tweets_df, candidates):
    '''
    will get the pd DATAFrame and loop through it to get candidate occurrence
    based on times tweeted and times mentioned
    :return:
    '''
    # ['tweet_id', 'tweet_date', 'tweet_screen_name', 'tweet_text']
    counter = 0
    for index, row in tweets_df.iterrows():
        # for every row we need to:
        # - get 'tweet_screen_name'
        if row['tweet_screen_name'] in candidates:
            # * add to the dictionary
            candidates[row['tweet_screen_name']] = candidates[row['tweet_screen_name']] + 1

        # - get 'tweet_text'
        tweet_text = row['tweet_text']
        # - loop through dictionary keys
        for key in candidates:
            if key in tweet_text:
                # * add to the dictionary
                candidates[key] = candidates[key] + 1
        counter += 1
        if counter % 10000 == 0:
            print(counter)

    print(counter)
    return candidates


#val = get_candidate_occurrence(load_pickle(), get_candidates())

#f = open("candidatos.txt","w+")
#for key in val:
#    f.write(key + ": " + str(val[key]) + "\n")

#f.close
#print(val)





