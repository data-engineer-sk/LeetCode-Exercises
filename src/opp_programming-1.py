class Score():
    def __init__(self):
        self.score = 0
        self.num_enemies = 5
        self.num_lives = 3

    def setScore(self, num):
        self.score = num
    def getScore(self):
         return self.score
    def getEnemies(self):
        return self.num_enemies
    def getLives(self):
        return self.num_lives
       
s = Score()
s.setScore(9)
print(s.getScore())
print(s.getEnemies())
print(s.getLives())