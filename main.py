import random
def get_random_word(difficulty: int): 
    f = open("words.txt", "r")
    txt = f.read()
    print(f.read())
    # print(txt)
    random_number = random.randint(0, 100)
    txt_array = txt.split("\n")
    print(txt_array[random_number])


get_random_word(0)
# print(5)
