from collections import Counter

candidates = ['CesarMontufar51', "CynthiaViteri6", 'davalos2019', "jimmyjairala", "juancaholguin", "LoroHomero",
              "LuisaMaldonadoM", "PacoMoncayo", "VickyDesintonio", "wgomezr"]
def get_term_frequency(given_file):

    new_file = "./FilesWithNoStopWord/" + given_file + "_N_S_Words.txt"
    file_to_read = open(new_file, 'r+')

    freq_dictionary = {}
    lines = file_to_read.readlines()
    # get line of file
    for line in lines:
        # for each word of the line
        word_list = line.split(" ")
        for word in word_list:
            # if it exists in the dictionary add to its key
            if word in freq_dictionary:
                freq_dictionary[word] = freq_dictionary[word] + 1
            # else create a key with starting value 1
            else:
                freq_dictionary[word] = 1

    file_to_read.close()
    return(freq_dictionary)

def write_freq_to_file(freq_dictionary, given_file):
    new_file = "./TermFrequencyByCandidate/" + given_file + "_W_Frequency.txt"
    file_to_write = open(new_file, 'w+')
    # get top 10 words
    k = Counter(freq_dictionary)
    high = k.most_common(len(freq_dictionary))
    for i in high:
        file_to_write.write(i[0] + " : " + str(i[1]) + "\n")
    file_to_write.close()





for candidate in candidates:
    write_freq_to_file(get_term_frequency(candidate), candidate)

