class Team:
    def __init__(self, name, roster, conference, division):
        self.name = name
        self.roster = roster
        self.conference = conference
        self.divison = division
        self.points = 0

    def findPlayerByPosition(self, playerList, position):
        for i in playerList:
            if (i.position == position):
                return i

        return playerList[0]

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

        self.forwards = [player for player in self.roster if player.position != 'D']

        for player in self.forwards:
            if (player.position == 'G'):
                self.forwards.remove(player)

        self.forwards.sort(key=lambda x: x.overall, reverse=True)

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
    def __init__(self, teamName, playerName, position, gamesPlayed, goals, assists, points, plusMinus, timeOnIcePerGame, overall):
        self.teamName = teamName
        self.playerName = playerName
        self.position = position
        self.gamesPlayed = gamesPlayed
        self.goals = goals
        self.assists = assists
        self.points = points
        self.plusMinus = plusMinus
        self.timeOnIcePerGame = int(timeOnIcePerGame[0] + timeOnIcePerGame[1])
        self.overall = 0

class Goalie:
    def __init__(self, teamName, playerName, position, gamesPlayed, wins, losses, savePercentage, goalsAgainstAverage, overall):
        self.teamName = teamName
        self.playerName = playerName
        self.position = position
        self.gamesPlayed = gamesPlayed
        self.wins = wins
        self.losses = losses
        self.savePercentage = savePercentage
        self.goalsAgainstAverage = goalsAgainstAverage
        self.overall = 0

   