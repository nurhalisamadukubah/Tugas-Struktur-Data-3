class GameEntry:
    total_player = 0

    def __init__(self, name, score, time):
        self.name = name
        self.score = score
        self.time = time
        
        GameEntry.total_player += 1
    
    def set_Name(self, name):
        self.name = name

    def get_Name(self):
        return self.name

    def set_Score(self, score):
        self.score = score
    
    def get_Score(self):
        return self.score

    def set_Time(self, time):
        self.time = time

    def get_Time(self):
        return self.time

    def get_Total():
        return GameEntry.total_player

class ScoreBoard:
    def __init__(self, capacity):
        self.capacity = capacity
        self.board = [None] * self.capacity
        self.n = 0
    
    def getCapacity(self):
        return self.capacity

    def sumEntries(self):
        return self.n

    def addItem(self, game_entry):
        name = game_entry.get_Name()
        score = game_entry.get_Score()

        good = len(self.board) > self.n or score > self.board[self.capacity - 1].get_Score()

        if good:
            if self.n < self.capacity:
                self.n += 1

            j = self.n - 1

            while j > 0 and self.board[j-1].get_Score() < score:
                self.board[j] = self.board[j-1]
                j -= 1
            self.board[j] = game_entry
            print(f"Entri {name} ditambahkan!")

    def listEntri(self):
        for i in range (0, self.n):
            print("Rank", i+1,"|", getattr(self.board[i], 'name'), getattr(self.board[i], 'score'), getattr(self.board[i], 'time'))

Nurma_score = GameEntry("Nurma", 99, 4)
Nunu_score = GameEntry("Nunu", 90, 6)
Nununu_score = GameEntry("Nununu", 91, 4)

score_board = ScoreBoard(10)
score_board.addItem(Nurma_score)
score_board.addItem(Nunu_score)
score_board.addItem(Nununu_score)

active = True

while active:
    print("")
    start = input("Menu: \n 1 = Tambah Entri Baru \n 2 = Tampilkan List ScoreBoard \n 3 = Keluar \n")
    print("")
    if start == '2':
        score_board.listEntri()
    elif start == '1':
        name = input("Masukkan Nama Pemain ")
        skor = int(input("Masukkan Skor "))
        waktu = int(input("Masukkan Waktu "))

        in_score = GameEntry(name, skor, waktu)
        set_board = score_board.addItem(in_score)

        print(f"Entri baru ditambahkan: {in_score.get_Name()} {in_score.get_Score()} {in_score.get_Time()}")
    else:
        break
