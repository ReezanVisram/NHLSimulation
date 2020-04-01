class Team:
    def __init__(self, name, roster):
        self.name = name
        self.roster = roster

class Player:
    def __init__(self, teamName, playerName, position, gamesPlayed, goals, assists, points):
        self.teamName = teamName
        self.playerName = playerName
        self.position = position
        self.gamesPlayed = gamesPlayed
        self.goals = goals
        self.assists = assists
        self.points = points

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
