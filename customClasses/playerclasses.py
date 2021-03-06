class Team:
    def __init__(self, name, roster, conference, division):
        self.name = name
        self.roster = roster
        self.conference = conference
        self.divison = division
        self.points = 0
        self.currPlayoffRoundWins = 0
        self.wins = 0
        self.losses = 0
        self.overtimeLosses = 0
        self.gameDays = []

    def findPlayerByPosition(self, playerList, position):
        for i in playerList:
            if (i.position == position):
                return i

        return playerList[0]

    # All overalls are created in engine.py before these methods run
    def createGoalieLines(self):
        self.goalieLines = ['G', 'G']

        self.goalies = [player for player in self.roster if player.position == 'G']

        self.goalies.sort(key=lambda x: x.overall, reverse=True)

        self.goalieLines[0] = self.goalies[0]
        self.goalieLines[1] = self.goalies[1]

    def createDefenseLines(self):
        self.defenseLines = [['D', 'D'], ['D', 'D'], ['D', 'D']]

        self.defensemen = [player for player in self.roster if player.position == 'D']

        self.defensemen.sort(key=lambda x: x.overall)

        for i in range(len(self.defenseLines)):
            for j in range(2):
                for defenseman in self.defensemen:
                    self.defenseLines[i][j] = defenseman
                self.defensemen.remove(defenseman)

    def createForwardLines(self):
        self.forwardLines = [['LW', 'C', 'RW'], ['LW', 'C', 'RW'], ['LW', 'C', 'RW'], ['LW', 'C', 'RW']]

        self.forwards = [player for player in self.roster if player.position != 'D' and player.position != 'G']

        self.forwards.sort(key=lambda x: x.overall, reverse=True)

        self.forwardsCopy = self.forwards.copy()

        for i in range(len(self.forwardLines)):
            for j in range(3):
                self.currPlayer = self.findPlayerByPosition(self.forwards, self.forwardLines[i][j])

                self.forwardLines[i][j] = self.currPlayer

                self.forwards.remove(self.currPlayer)

    def createLines(self):
        self.createGoalieLines()
        self.createDefenseLines()
        self.createForwardLines()

    def getOffenseOverall(self):
        lineAverageOveralls = []
        self.teamOffensiveOverall = 0
        for i in range(len(self.forwardLines)):
            currLineOverall = 0
            for j in range(len(self.forwardLines[i])):
                currLineOverall += self.forwardLines[i][j].overall

            currLineAverage = currLineOverall / 3
            lineAverageOveralls.append(currLineAverage)

        self.forwardLineOveralls = lineAverageOveralls

        for overall in range(len(lineAverageOveralls)):
            if (overall == 0):
                self.teamOffensiveOverall += (lineAverageOveralls[overall] * 0.4)

            elif (overall == 1):
                self.teamOffensiveOverall += (lineAverageOveralls[overall] * 0.3)

            elif (overall == 2):
                self.teamOffensiveOverall += (lineAverageOveralls[overall] * 0.2)

            elif (overall == 3):
                self.teamOffensiveOverall += (lineAverageOveralls[overall] * 0.1)

        self.teamOffensiveOverall = round(self.teamOffensiveOverall)

 
    def getDefensiveOverall(self):
        lineAverageOveralls = []
        self.teamDefensiveOverall = 0
        for i in range(len(self.defenseLines)):
            currLineOverall = 0
            for j in range(len(self.defenseLines[i])):
                currLineOverall += self.defenseLines[i][j].overall

            currLineAverage = currLineOverall / 2
            lineAverageOveralls.append(currLineAverage)
        
        self.defenseLineOveralls = lineAverageOveralls

        for overall in range(len(lineAverageOveralls)):
            if (overall == 0):
                self.teamDefensiveOverall += (lineAverageOveralls[overall] * 0.4)

            elif (overall == 1):
                self.teamDefensiveOverall += (lineAverageOveralls[overall] * 0.3)

            elif (overall == 2):
                self.teamDefensiveOverall += (lineAverageOveralls[overall] * 0.3)


        self.teamDefensiveOverall = round(self.teamDefensiveOverall)


    def getGoalieOverall(self):
        self.teamGoalieOverall = 0

        self.teamGoalieOverall += self.goalieLines[0].overall * 0.7
        self.teamGoalieOverall += self.goalieLines[1].overall * 0.3

        self.teamGoalieOverall = round(self.teamGoalieOverall)

    def getAllOveralls(self):
        self.getOffenseOverall()
        self.getDefensiveOverall()
        self.getGoalieOverall()

    def createAllInfo(self):
        self.createLines()
        self.getAllOveralls()                        


class Player:
    def __init__(self, teamName, playerName, position, gamesPlayed, goals, assists, points, plusMinus, timeOnIcePerGame, overall=0, currSeasonGamesPlayed=0, currSeasonGoals=0, currSeasonAssists=0, currSeasonPoints=0):
        self.teamName = teamName
        self.playerName = playerName
        self.position = position
        self.gamesPlayed = gamesPlayed
        self.goals = goals
        self.assists = assists
        self.points = points
        self.plusMinus = plusMinus
        self.timeOnIcePerGame = int(timeOnIcePerGame[0] + timeOnIcePerGame[1])
        self.currSeasonGoals = currSeasonGoals
        self.currSeasonAssists = currSeasonAssists
        self.currSeasonPoints = currSeasonPoints
        self.currSeasonGamesPlayed = currSeasonGamesPlayed

    def getCurrYearStats(self):
        self.currSeasonPoints = self.currSeasonGoals + self.currSeasonAssists

class Goalie:
    def __init__(self, teamName, playerName, position, gamesPlayed, wins, losses, savePercentage, goalsAgainstAverage, overall, currSeasonGamesPlayed=0, currSeasonWins=0, currSeasonSavePercentage=0, currSeasonGoalsAgainstAverage=0):
        self.teamName = teamName
        self.playerName = playerName
        self.position = position
        self.gamesPlayed = gamesPlayed
        self.wins = wins
        self.losses = losses
        self.savePercentage = savePercentage
        self.goalsAgainstAverage = goalsAgainstAverage
        self.overall = 0
        self.currSeasonGamesPlayed = currSeasonGamesPlayed
        self.currSeasonWins = currSeasonWins
        self.currSeasonSavePercentage = currSeasonSavePercentage
        self.currSeasonGoalsAgainstAverage = currSeasonGoalsAgainstAverage
        self.totalShotsFaced = 0
        self.totalSavesMade = 0
        self.totalGoalsAgainst = 0

    def getCurrYearStats(self):
        self.currSeasonSavePercentage = round(self.totalSavesMade / self.totalShotsFaced, 3) if self.totalShotsFaced > 0 else 0
        self.currSeasonGoalsAgainstAverage = round(self.totalGoalsAgainst / self.currSeasonGamesPlayed, 3) if self.currSeasonGamesPlayed > 0 else 0

   