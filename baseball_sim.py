import random

class Team():

    def __init__(self, name, k, action):
        self.name = name
        self.k = k
        self.action = action
        self.wins = 0
        self.losses = 0

class Match():

    def __init__(self, teamA, teamB, verbose=False):
        self.teamA = teamA
        self.teamB = teamB
        self.teamAScore = 0
        self.teamBScore = 0
        self.field = {1: None, 2: None, 3: None}
        self.verbose = verbose

    def sim(self):
        for inning in range(1, 10):
            self.play_inning(inning)
        
        while self.teamAScore == self.teamBScore:
            self.play_inning(inning)
            inning += 1
    
        if self.teamAScore > self.teamBScore:
            self.teamA.wins += 1
            self.teamB.losses += 1
        else:
            self.teamB.wins += 1
            self.teamA.losses += 1

    def play_inning(self, inning):
        if self.verbose:
            print "Inning {}".format(inning)

        strikeouts = 0
        while strikeouts < 3:
            prob = random.randint(0, 100)
            if prob < self.teamA.k:
                strikeouts += 1
            else:
                if self.teamA.action == "homerun":
                    self.teamAScore += 1
                elif self.teamA.action == "double":
                    score = len([x for x in self.field.values() if x is not None])
                    self.teamAScore += score
                    import pdb;pdb.set_trace()
                    self.field[2] = "P"
                elif self.teamA.action == "walk":
                    if self.field[3] == "P":
                        self.teamAScore += 1
                    self.field[3] = self.field[2]
                    self.field[2] = self.field[1]
                    self.field[1] = "P"
        
        strikeouts = 0
        while strikeouts < 3:
            prob = random.randint(0, 100)
            if prob < self.teamB.k:
                strikeouts += 1
            else:
                if self.teamB.action == "homerun":
                    self.teamBScore += 1
                elif self.teamB.action == "double":
                    score = len([x for x in self.field.values() if x is not None])
                    self.teamBScore += score
                    self.field[2] = "P"
                elif self.teamB.action == "walk":
                    if self.field[3] == "P":
                        self.teamBScore += 1
                    self.field[3] = self.field[2]
                    self.field[2] = self.field[1]
                    self.field[1] = "P"
        if self.verbose:
            print "{} {} - {} {}".format(self.teamA.name, self.teamAScore, self.teamBScore, self.teamB.name)


Delaware = Team("Delaware", 90, "homerun")
Taters = Team("Taters", 80, "double")
Moonwalkers = Team("Moonwalkers", 60, "walk")

matches = 10000
for x in range(matches):
    match = Match(Delaware, Taters)
    match.sim()

for x in range(matches):
    match = Match(Moonwalkers, Taters)
    match.sim()


for x in range(matches):
    match = Match(Delaware, Moonwalkers)
    match.sim()

print "Delaware {} - {}".format(Delaware.wins, Delaware.losses)
print "Taters {} - {}".format(Taters.wins, Taters.losses)
print "Moonwalkers {} - {}".format(Moonwalkers.wins, Moonwalkers.losses)
