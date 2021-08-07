import random
from enum import Enum


class GameState(Enum):
    running = "running"
    failed = "failed"
    success = "success"
    start = "start"



class RandomWordGame:

    allowed_guesses = 2
    current_guesses = 0
    failed_guesses = 0
    current_state = GameState.start
    guessed_letters = set()
    correct_word = None

    def get_maximum_length_word(self, word_list: list):
        current_longest_word = ''
        for word in word_list:
            if len(word) > len(current_longest_word):
                current_longest_word = word
        return len(current_longest_word)

    def get_random_word(self, difficulty: int):
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
            range_maximum = self.get_maximum_length_word(txt_array)
            # print(f"the longest word is: {range_maximum}")

        filtered_list = [x for x in txt_array if len(x) >= range_minimum and len(x) <= range_maximum]
        random_number = random.randint(0, len(filtered_list))
        if len(filtered_list) == 0:
            print("there were no words in this list")
            return None
        return filtered_list[random_number]

    def get_user_letter_guess(self):
        guess = None
        guess = input("please enter your a single letter to guess: ").lower()
        return guess

    def get_word_with_dashes(self):
        out_str = ""
        for letter in self.correct_word:
            if letter in self.guessed_letters:
                out_str += letter
            else:
                out_str += "_"
        return out_str

    def print_current_state(self):
        all_text = ""
        all_text += (f"you have guessed the letters: {self.guessed_letters}\n")
        all_text += (f"you have {self.allowed_guesses - self.failed_guesses} guesses left\n")
        all_text += self.get_word_with_dashes()
        all_text += "\n\n\n"
        print(all_text)

    def run_game(self, dificulty: int):
        # prepare the word and game
        print("the game has begun!")
        word = self.get_random_word(dificulty)
        print(f"we generated a word with {len(word)} characters: {word}\n\n\n")
        self.correct_word = word.lower()
        self.current_state = GameState.running


        #  begin actual game
        while self.current_state == GameState.running:  # keep running until the game isnt "running"
            guessed_letter = self.get_user_letter_guess()
            if guessed_letter in word:  # success case
                self.guessed_letters.add(guessed_letter)
                print("got the letter!")
                if set(self.correct_word) == self.guessed_letters:
                    self.current_state = GameState.success  # you won!
            else:  # failure cases

                if guessed_letter not in self.guessed_letters:
                    self.guessed_letters.add(guessed_letter)
                    self.failed_guesses += 1
                    print("letter not found in word! imma gank a point from you")
                elif guessed_letter in self.guessed_letters:
                    print("you already guessed that letter dumbass")

                if self.failed_guesses >= self.allowed_guesses:
                    self.current_state = GameState.failed
            self.print_current_state()

        if self.current_state == GameState.failed:
            print("GAME OVER!")
            return
        if self.current_state == GameState.success:
            print("You guessed it correctly!")


game = RandomWordGame()
game.run_game(0)