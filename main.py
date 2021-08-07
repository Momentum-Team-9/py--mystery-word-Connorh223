import random
def get_maximum_length_word(word_list: list):
    current_longest_word = ''
    for word in word_list:
        if len(word) > len(current_longest_word):
            current_longest_word = word
    return len(current_longest_word)

def get_random_word(difficulty: int): 
    f = open("words.txt", "r")
    txt = f.read()
    txt_array = txt.split("\n")
    range_minimum = 0
    range_maximum = 10
    if difficulty == 0: 
        range_minimum = 4
        range_maximum = 6
    elif difficulty == 1:
        range_minimum = 6
        range_maximum = 8
    elif difficulty == 2:
        range_minimum = 8
        range_maximum = get_maximum_length_word(txt_array)
        # print(f"the longest word is: {range_maximum}")

    filtered_list = [x for x in txt_array if len(x) >= range_minimum and len(x) <= range_maximum]
    random_number = random.randint(0, len(filtered_list))
    if len(filtered_list) == 0:
        print("there were no words in this list")
        return None
    return filtered_list[random_number]


my_random_word = get_random_word(2)
print(my_random_word)
# print(5)
