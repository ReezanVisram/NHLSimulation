class Game:
    def __init__(self, team1, team2, day, categoryWinners):
        self.team1 = team1
        self.team2 = team2
        self.day = day
        self.categoryWinners = categoryWinners
    
    def compareOffense(self):
        if (self.team1.teamOffensiveOverall > self.team2.teamOffensiveOverall):
            self.categoryWinners.append(self.team1)
        elif (self.team2.teamOffensiveOverall > self.team1.teamOffensiveOverall):
            self.categoryWinners.append(self.team2)
        

    def compareDefense(self):
        if (self.team1.teamDefensiveOverall > self.team2.teamDefensiveOverall):
            self.categoryWinners.append(self.team1)
        elif (self.team2.teamDefensiveOverall > self.team1.teamDefensiveOverall):
            self.categoryWinners.append(self.team2)

    def compareGoalies(self):
        if (self.team1.teamGoalieOverall > self.team2.teamGoalieOverall):
            self.categoryWinners.append(self.team1)
        elif (self.team2.teamGoalieOverall > self.team1.teamGoalieOverall):
            self.categoryWinners.append(self.team2)


    def determineWinner(self):
        self.compareOffense()
        self.compareDefense()
        self.compareGoalies()

        team1WinCount = 0
        team2WinCount = 0

        for categoryWinner in self.categoryWinners:
            if (categoryWinner == self.team1):
                team1WinCount += 1
            elif (categoryWinner == self.team2):
                team2WinCount += 1

        if (team1WinCount > team2WinCount):
            self.winner = self.team1

        elif (team2WinCount > team1WinCount):
            self.winner = self.team2

        else:
            self.winner = None
            

