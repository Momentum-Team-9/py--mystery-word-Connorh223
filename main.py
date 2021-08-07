import random
def get_random_word(difficulty: int): 
    f = open("words.txt", "r")
    txt = f.read()
    # print(txt)
    txt_array = txt.split("\n")
    filtered_list = [x for x in txt_array if len(x) >= 4 and len(x) <= 6]
    random_number = random.randint(0, len(filtered_list))
    return(filtered_list[random_number])


my_random_word = get_random_word(0)
print(my_random_word)
# print(5)
