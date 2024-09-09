import random
random.seed(42)

from utils import print_correct, print_warning, print_error

class Wordle:
    def __init__(self, csv_file, txt_file, word_len, limit, guess_num):
        self.csv_file = csv_file
        self.txt_file = txt_file
        self.word_len = word_len
        self.limit = limit
        self.guess_num = guess_num


    def csv_to_txt(self):
        """Function to convert 'csv' file to 'txt'

        Args:
            csv_file (csv)): csv file of word and thier frequency.
            txt_file (txt): text file of word and thier frequency.
        """
        with open(self.csv_file, 'r') as f:
            with open(self.txt_file, 'w') as txt:
                for line in f:
                    txt.write(line)

    def words_frequency_list(self, txt_file):
        words_freq = []
        with open(txt_file) as txt:
            next(txt)
            for line in txt:
                word, frequency = line.split(',')
                frequency = int(frequency)
                words_freq.append((word, frequency))
            return words_freq

    def generate_words(self, words_freq):
        # Filter words 
        words_freq = list(filter(lambda w_freq: len(w_freq[0]) == self.word_len, words_freq))

        # Sort words
        words_freq = sorted(words_freq, key=lambda w_freq: w_freq[1], reverse=True)

        # Apply limit
        words_freq = words_freq[:self.limit]

        # Just words
        words = [w_freq[0].upper() for w_freq in words_freq]
        words = words

        return words

    def word_choice(self, words):
        word = random.choice(words)
        word = word.upper()
        return word

    def run(self):
        self.csv_to_txt()
        words_freq = self.words_frequency_list(self.txt_file)
        self.words = self.generate_words(words_freq)
        self.word = self.word_choice(self.words)

        while self.guess_num:

            user_guess = input(f'Please enter a word with {self.word_len} letter or (q to quit)')
            user_guess = user_guess.upper()

            if user_guess == 'Q':
                break
            
            # Check length
            if len(user_guess) != self.word_len:
                print(f'Enter word with {self.word_len} letter. You entered word with {len(user_guess)} letters')
                continue
            
            # Check valid word
            if user_guess not in self.words:
                print(f'Enter valid word')
                continue
            for w_letter, u_letter in zip(self.word, user_guess):
                if w_letter == u_letter:
                    print_correct(f' {u_letter} ')
                elif u_letter in self.word:
                    print_warning(f' {u_letter} ')
                else:
                    print_error(f' {u_letter} ')
            print()

            if user_guess == self.word:
                print_correct(' Congrdulation! You win :-) ')
                print()
                self.success = True
                break
            self.guess_num -= 1
