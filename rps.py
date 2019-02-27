import random

moves = ['rock', 'paper', 'scissors']


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Player:

    def move(self):
        return 'rock'

    def learn(self, my_move, their_move):
        return my_move, their_move


class RandomPlayer(Player):
    def move(self):
        return(random.choice(moves))


class HumanPlayer(Player):
    def move(self):
        my_move = input("Please choose one: paper, rock or scissors. \n")

        while True:
            if my_move.lower() not in moves:
                my_move = input("Please choose one or 'quit': paper, "
                                "rock or scissors. \n")
            elif my_move.lower() is 'quit':
                print("You Quitter...")
                quit()
            else:
                return my_move.lower()


class CyclePlayer(Player):
    def __init__(self):
        self.cycle_move = ""

    def learn(self, my_move, their_move):
        self.cycle_move = my_move

    def move(self):
        if self.cycle_move == "":
            return random.choice(moves)
        elif self.cycle_move == "rock":
            return "paper"
        elif self.cycle_move == "paper":
            return "scissors"
        elif self.cycle_move == "scissors":
            return "rock"


class ReflectPlayer(Player):
    def __init__(self):
        self.my_move = "rock"

    def learn(self, my_move, their_move):
        self.my_move = their_move

    def move(self):
        return self.my_move


class Game:
    p1_score = 0
    p2_score = 0

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"Player 1: {move1}  Player 2: {move2}")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)
        if beats(move1, move2) is True:
            self.p1_score += 1
            print("YOU WON!")
        elif beats(move2, move1) is True:
            self.p2_score += 1
            print("YOU LOOSE!")
        else:
            print("DRAW!")

    def play_game(self):
        print("Game start!")
        while True:
            try:
                round_num = int(input("Enter the number of rounds you would "
                                      "like to play > "))
                for round in range(round_num):
                    print(f"Round {round}:")
                    self.play_round()
                    print(f"The score is {self.p1_score} to {self.p2_score}")
                if self.p1_score > self.p2_score:
                    print("YOU WON THE GAME!!!")
                elif self.p1_score < self.p2_score:
                    print("YOU LOST THE GAME!")
                else:
                    print("THE GAME IS A DRAW!")
            except ValueError:
                round_num = int(input("Enter the NUMBER of rounds you would "
                                      "like to play > "))


if __name__ == '__main__':
    stratagy = [Player(), RandomPlayer(), CyclePlayer(), ReflectPlayer()]
    random_stratagy = random.choice(stratagy)
    game = Game(HumanPlayer(), random_stratagy)
    game.play_game()
