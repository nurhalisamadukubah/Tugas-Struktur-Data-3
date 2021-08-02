class GameEntry:
    def __init__(self, name, score, time):
        self.name = name
        self.score = score
        self.time = time
        
    def get_name(self, name):
        self.name = name
    def get_name(self):
        return self.name
    def get_score(self, score):
        self.score = score
    def get_score(self):
        return self.score
    def get_time(self, time):
        self.time = time
    def get_time(self):
        return self.time

class ScoreBoard:
    def __init__(self, capacity):
        self.capacity = capacity
        self.board = [None] * self.capacity
        self.n = 0


    def addItem(self, game_entry):
        score = game_entry.get_score()

        good = len(self.board) > self.n or score > self.board[self.capacity -1].get_score()

        if good:
            if self.n < self.capacity:
                self.n +=1

            j = self.n-1

            while j > 0 and self.board[j-1].get_score() < score:
                self.board[j] = self.board[j-1]
                j -=1
                self.board[j] = game_entry

a_score = GameEntry("a", 89, 4)

score_board = ScoreBoard(2)
score_board.addItem(a_score)

print(a_score.get_score())
