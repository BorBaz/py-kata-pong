# My case
class Pong:
    def __init__(self, max_score):
        self.max_score = max_score
        self.player = 2
        self.scores = [0, 0]
        self.game_ended = False

    def play(self, ball_pos, player_pos):

        global result
        upper_limit = player_pos + 3
        down_limit = player_pos - 3
        hit = (ball_pos <= upper_limit) and (ball_pos >= down_limit)

        if hit and not self.game_ended:
            self.toggle_player()
            return f"Player {self.player} has hit the ball!"
        elif not hit and not self.game_ended:
            self.add_point(self.player)

            if self.scores[self.get_rival(self.player) - 1] >= self.max_score:
                self.game_ended = True
                self.toggle_player()
                return f"Player {self.get_rival(self.player)} has won the game!"
            else:
                self.toggle_player()
                return f"Player {self.player} has missed the ball!"
        else:
            self.toggle_player()
            return "Game Over!"

    def toggle_player(self):
        if self.player == 1:
            self.player = 2
        else:
            self.player = 1

    def add_point(self, player):
        self.scores[self.get_rival(player) - 1] += 1

    def get_rival(self, player):
        return 1 if player == 2 else 2


pong = Pong(2)
print(pong.play(50, 53))
print(pong.play(100, 97))
print(pong.play(0, 4))
print(pong.play(25, 25))
print(pong.play(75, 25))
print(pong.play(50, 50))


# Best case
from itertools import cycle


class Pong:
    def __init__(self, max_score):
        self.max_score = max_score;
        self.scores = {1: 0, 2: 0}
        self.players = cycle((1, 2))

    def game_over(self):
        return any(score >= self.max_score for score in self.scores.values())

    def play(self, ball_pos, player_pos):
        if self.game_over():
            return "Game Over!"

        player = next(self.players)
        if abs(ball_pos - player_pos) <= 3:
            return "Player {} has hit the ball!".format(player)
        else:
            self.scores[player] += 1
            if self.scores[player] == self.max_score:
                return "Player {} has won the game!".format(next(self.players))
            else:
                return "Player {} has missed the ball!".format(player)
