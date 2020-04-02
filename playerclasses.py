class Team:
    def __init__(self, name, roster):
        self.name = name
        self.roster = roster

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
    def __init__(self, teamName, playerName, position, gamesPlayed, wins, losses, savePercentage, goalsAgainstAverage):
        self.teamName = teamName
        self.playerName = playerName
        self.position = position
        self.gamesPlayed = gamesPlayed
        self.wins = wins
        self.losses = losses
        self.savePercentage = savePercentage
        self.goalsAgainstAverage = goalsAgainstAverage

    def determinePlayStyle(self):
        pass

    def determineOverall(self):
        self.overall = (self.wins / self.gamesPlayed) + (self.wins * self.savePercentage) - (self.goalsAgainstAverage * (self.losses / self.gamesPlayed)) + 30