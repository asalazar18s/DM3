import math

candidates = ['CesarMontufar51', "CynthiaViteri6", 'davalos2019', "jimmyjairala", "juancaholguin", "LoroHomero",
              "LuisaMaldonadoM", "PacoMoncayo", "VickyDesintonio", "wgomezr"]


def get_top_ten_word_freq(file_name):
    file_to_read = open("./TermFrequencyByCandidate/" + file_name + "_W_Frequency.txt", 'r+')
    x = file_to_read.readlines()
    top_ten_dict = {}
    counter = 0
    for line in x:
        temp = line.split(":")
        top_ten_dict[temp[0].rstrip()] = int(temp[1].strip())
        counter += 1
        if counter > 9:
            break

    return top_ten_dict


def get_df(candidate, top_ten_dict):
    file_name_feb = "./Candidates/" + candidate + "/" + "Feb.txt"
    file_to_read_feb = open(file_name_feb, 'r+')
    file_name_mar = "./Candidates/" + candidate + "/" + "Mar.txt"
    file_to_read_mar = open(file_name_mar, 'r+')
    file_name_may = "./Candidates/" + candidate + "/" + "May.txt"
    file_to_read_may = open(file_name_may, 'r+')
    file_name_abr = "./Candidates/" + candidate + "/" + "Abr.txt"
    file_to_read_abr = open(file_name_abr, 'r+')

    final_dict = {}

    file_list = [file_to_read_feb.readlines(), file_to_read_mar.readlines(), file_to_read_abr.readlines(),file_to_read_may.readlines()]
    for word in top_ten_dict:
        final_dict[word] = 0
        for file in file_list:
            temp_lines = file
            for line in temp_lines:
                temp = line.split(":")
                temp_val = int(temp[1].strip())
                if word == temp[0].strip():
                    if temp_val != 0:
                        final_dict[word] = final_dict[word] + 1

    return final_dict


def get_idf(df_values):
    idf_dict = {}
    for word in df_values:
        idf_dict[word] = math.log(4/df_values[word], 10)

    return idf_dict


def get_tf_idf(top_ten, idf_values):
    tf_idf_dict = {}
    for word in top_ten:
        tf_idf_dict[word] = top_ten[word] * idf_values[word]

    return tf_idf_dict


print("tf values:")
print(get_top_ten_word_freq("juancaholguin"))
print("df values: ")
print(get_df("juancaholguin", get_top_ten_word_freq("juancaholguin")))
print("idf values: ")
print(get_idf(get_df("juancaholguin", get_top_ten_word_freq("juancaholguin"))))
print("tf - idf values: ")
print(get_tf_idf(get_top_ten_word_freq("juancaholguin"), get_idf(get_df("juancaholguin", get_top_ten_word_freq("juancaholguin")))))











#print(get_top_ten_word_freq("juancaholguin"))
# we need to print tf df  idf tf-idf
# we got tf
# we got df

