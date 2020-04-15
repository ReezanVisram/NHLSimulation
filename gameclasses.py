import random
class Game:
    def __init__(self, team1, team2, day, categoryWinners):
        self.team1 = team1
        self.team2 = team2
        self.day = day
        self.categoryWinners = categoryWinners
        self.team1Score = 0
        self.team2Score = 0
    

    def simulateGame(self):
        for period in range(3):
            self.simulatePeriod()

        if (self.team1Score > self.team2Score):
            self.winner = self.team1

        elif (self.team1Score < self.team2Score):
            self.winner = self.team2

        else:
            self.winner = None

    def simulatePeriod(self):
        for minute in range(20):
            goal = self.determineGoal()
            if (goal == self.team1):
                self.team1Score += 1
            elif (goal == self.team2):
                self.team2Score += 1


    def determineCurrTeam1ForwardLine(self):
        currLineChance = random.randint(1, 10)

        if (currLineChance <= 4):
            return 0

        elif (currLineChance <= 7):
            return 1

        elif (currLineChance <= 9):
            return 2

        else:
            return 3

    def determineCurrTeam2ForwardLine(self):
        currLineChance = random.randint(1, 10)

        if (currLineChance <= 4):
            return 0
        
        elif (currLineChance <= 7):
            return 1

        elif (currLineChance <= 9):
            return 2

        else:
            return 3

    def determineGoal(self):
        team1ForwardLineNumber = self.determineCurrTeam1ForwardLine()
        team2ForwardLineNumber = self.determineCurrTeam2ForwardLine()

        team1ActualForwardLine = self.team1.forwardLines[team1ForwardLineNumber]
        team2ActualForwardLine = self.team2.forwardLines[team2ForwardLineNumber]

        team1ForwardLineOverall = self.team1.forwardLineOveralls[team1ForwardLineNumber]
        team2ForwardLineOverall = self.team2.forwardLineOveralls[team2ForwardLineNumber]
        
        if (team1ForwardLineOverall > team2ForwardLineOverall):
            higherTeam = self.team1

        elif (team1ForwardLineOverall < team2ForwardLineOverall):
            higherTeam = self.team2

        else:
            higherTeam = self.team1 if random.randint(0, 1) == 0 else self.team2

        if (higherTeam == self.team1):
            difference = team1ForwardLineOverall - team2ForwardLineOverall
        
        elif (higherTeam == self.team2):
            difference = team2ForwardLineOverall - team1ForwardLineOverall

        goalIsScored = True if random.uniform(0, difference) < difference / 6 else False

        if (goalIsScored):
            return higherTeam


        
