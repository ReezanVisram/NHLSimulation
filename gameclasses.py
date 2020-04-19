import random
class Game:
    def __init__(self, team1, team2, day, team1Score=0, team2Score=0, wasOvertime=False):
        self.team1 = team1
        self.team2 = team2
        self.day = day
        self.team1Score = team1Score
        self.team2Score = team2Score
        self.wasOvertime = wasOvertime
    
    def simulateGame(self):
        for period in range(3): 
            self.simulatePeriod()

        if (self.team1Score > self.team2Score):
            self.winner = self.team1

        elif (self.team1Score < self.team2Score):
            self.winner = self.team2

        else:
            self.simulateOvertime()

            if (self.team1Score > self.team2Score):
                self.winner = self.team1
                self.wasOvertime = True
            
            elif (self.team1Score < self.team2Score):
                self.winner = self.team2
                self.wasOvertime = True

            else:
                threeRoundWinner = self.simulateShootout()

                if (threeRoundWinner):
                    self.winner = self.team1 if self.team1Shootout > self.team2Shootout else self.team2

                else:
                    self.winner = self.team1 if random.randint(0, 1) == 0 else  self.team2

        if (self.wasOvertime):
            self.determineLoser()

    def determineLoser(self):
        if (self.winner == self.team1):
            self.loser = self.team2
        
        else:
            self.loser = self.team1

    def simulatePeriod(self):
        for minute in range(20):
            if (minute % 3 == 0): # Arbitrarily chose 3 minutes as the length of a shift
                self.lineChange()
            goal = self.determineGoal()
            if (goal == self.team1):
                self.team1Score += 1
            elif (goal == self.team2):
                self.team2Score += 1

    def simulateOvertime(self):
        for minute in range(5):
            goal = self.determineGoal()
            if (goal == self.team1):
                self.team1Score += 1
                break
            elif (goal == self.team2):
                self.team2Score += 1
                break

    def simulateShootout(self):
        self.team1Shootout = 0
        self.team2Shootout = 0
        for shootoutRound in range(3):
            team1Shooter = self.team1.forwardsCopy[shootoutRound]

            overallDifference = team1Shooter.overall - self.team2.goalieLines[0].overall

            if (overallDifference > 8):
                self.team1Shootout += 1

            team2Shooter = self.team2.forwardsCopy[shootoutRound]
            overallDifference = team2Shooter.overall - self.team1.goalieLines[0].overall

            if (overallDifference > 8):
                self.team2Shootout += 1

        if (self.team1Shootout != self.team2Shootout):
            return True

        else:
            return False

    # Line changes are completely random for now, will change to include matchups and situational changes, as well as Special Teams
    def determineCurrTeamForwardLine(self):
        currLineChance = random.randint(1, 10)

        if (currLineChance <= 4):
            return 0

        elif (currLineChance <= 7):
            return 1

        elif (currLineChance <= 9):
            return 2

        else:
            return 3

    def determineCurrTeamDefenseLine(self):
        currLineChance = random.randint(1, 10)

        if (currLineChance <= 4):
            return 0
        
        elif (currLineChance <= 7):
            return 1

        else:
            return 2

    def lineChange(self):
        self.team1ForwardLineNumber = self.determineCurrTeamForwardLine()
        self.team2ForwardLineNumber = self.determineCurrTeamForwardLine()

        self.team1DefenseLineNumber = self.determineCurrTeamDefenseLine()
        self.team2DefenseLineNumber = self.determineCurrTeamDefenseLine()

        self.team1ActualForwardLine = self.team1.forwardLines[self.team1ForwardLineNumber]
        self.team2ActualForwardLine = self.team2.forwardLines[self.team2ForwardLineNumber]

        self.team1ActualDefenseLine = self.team1.defenseLines[self.team1DefenseLineNumber]
        self.team2ActualDefenseLine = self.team2.defenseLines[self.team2DefenseLineNumber]

        self.team1ForwardLineOverall = self.team1.forwardLineOveralls[self.team1ForwardLineNumber]
        self.team2ForwardLineOverall = self.team2.forwardLineOveralls[self.team2ForwardLineNumber]

        self.team1DefenseLineOverall = self.team1.defenseLineOveralls[self.team1DefenseLineNumber]
        self.team2DefenseLineOverall = self.team2.defenseLineOveralls[self.team2DefenseLineNumber]

    # More functionality to be added to determine who scored and when (Foundations already in)
    def determineGoal(self):
        if (self.team1ForwardLineOverall > self.team2ForwardLineOverall):
            higherTeam = self.team1
            lowerTeam = self.team2

        elif (self.team1ForwardLineOverall < self.team2ForwardLineOverall):
            higherTeam = self.team2
            lowerTeam = self.team2

        else:
            higherTeam = self.team1 if random.randint(0, 1) == 0 else self.team2
            if (higherTeam == self.team1):
                lowerTeam = self.team2
            else:
                lowerTeam = self.team1

        if (higherTeam == self.team1):
            difference = self.team1ForwardLineOverall - self.team2ForwardLineOverall
        
        elif (higherTeam == self.team2):
            difference = self.team2ForwardLineOverall - self.team1ForwardLineOverall

        goalCouldBeScored = True if random.uniform(0, difference) > difference * 0.6 else False

        if (goalCouldBeScored):
            if (higherTeam == self.team1):
                getsPastDefense = True if random.uniform(0, self.team2DefenseLineOverall) > self.team2DefenseLineOverall * 0.6 else False

            else:
                getsPastDefense = True if random.uniform(0, self.team1DefenseLineOverall) > self.team1DefenseLineOverall * 0.6 else False

            if (getsPastDefense):
                getsPastGoalie = True if random.uniform(0, lowerTeam.goalieLines[0].overall) > lowerTeam.goalieLines[0].overall * 0.6 else False

                if (getsPastGoalie):
                    return higherTeam

# Extends Game class
class PlayoffGame(Game):
    def simulateGame(self):
        for period in range(3):
            self.simulatePeriod()

        if (self.team1Score > self.team2Score):
            self.winner = self.team1

        elif (self.team1Score < self.team2Score):
            self.winner = self.team2

        else:
            for overtime in range(6):
                self.simulateOvertime()

                if (self.team1Score > self.team2Score):
                    self.winner = self.team1
                    break

                elif (self.team1Score < self.team2Score):
                    self.winner = self.team2
                    break
                    
                else:
                    self.winner = self.team1 if random.randint(0, 1) == 0 else self.team2

class Series:
    def __init__(self, games, team1Wins=0, team2Wins=0):
        self.games = games
        self.team1Wins = team1Wins
        self.team2Wins = team2Wins

    def simulateSeries(self):
        for game in range(len(self.games)):
            self.games[game].simulateGame()

            if (self.games[game].winner == self.games[game].team1):
                self.team1Wins += 1
            
            else:
                self.team2Wins += 1

            if (self.team1Wins >= 4):
                self.seriesWinner = self.games[game].team1
                self.seriesLoser = self.games[game].team2
                self.gamesPlayed = game + 1
                break

            elif (self.team2Wins >= 4):
                self.seriesWinner = self.games[game].team2
                self.seriesLoser = self.games[game].team1
                self.gamesPlayed = game + 1
                break