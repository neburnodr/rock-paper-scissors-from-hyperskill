import random

class RockPaperScissors:
    win_dict = {'rock': 'scissors', 'paper': 'rock', 'scissors': 'paper'}

    def __init__(self):
        self.user()

    def user(self):
        self.name = input('Enter your name: ')
        print(f'Hello, {self.name}')
        with open('rating.txt', 'r') as file:
            self.scores = file.read().split()
            if self.name in self.scores:
                self.user_score = int(self.scores[self.scores.index(self.name) + 1])
            else:
                self.user_score = 0
        self.mode()

    def mode(self):
        items = input().split(',')
        print("Okay, let's start")
        if items == ['']:
            self.options()
        else:
            self.win_dict = {}
            for item in items:
                self.win_dict[item] = []
                lst = items[items.index(item) + 1:]
                lst += items[:items.index(item)]
                for i in range(len(lst) // 2, len(lst)):
                    self.win_dict[item].append(lst[i])
            self.options()

    def options(self):
        option_chosen = input()
        if option_chosen == '!rating':
            print(f'Your rating: {self.user_score}')
            self.options()
        elif option_chosen in list(self.win_dict):
            self.game(option_chosen)
        elif option_chosen == '!exit':
            print("Bye!")
            self.update_ratings()
        else:
            print('Invalid input')
            self.options()

    def game(self, option):
        computer_choice = random.choice(list(self.win_dict))
        if option in self.win_dict[computer_choice]:
            print(f"Sorry, but computer chose {computer_choice}")
        elif computer_choice in self.win_dict[option]:
            print(f"Well done. Computer chose {computer_choice} and failed")
            self.user_score += 100
        else:
            print(f"There is a draw ({computer_choice})")
            self.user_score += 50
        self.options()

    def update_ratings(self):
        if self.name in self.scores:
            self.scores[self.scores.index(self.name) + 1] = str(self.user_score)
        else:
            self.scores[len(self.scores):] = self.name, str(self.user_score)
        writings_list = []
        for i in range(0, len(self.scores), 2):
            user = ' '.join(self.scores[i:i + 2])
            writings_list.append(user)
        self.save_ratings(writings_list)

    def save_ratings(self, lst):
        with open('rating.txt', 'w') as file:
            for user in lst:
                print(user + '\n', file=file)

rockpaperscissors = RockPaperScissors()