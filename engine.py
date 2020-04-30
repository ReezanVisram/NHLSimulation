import json
import random
from customClasses.playerclasses import Team, Player, Goalie
from customClasses.gameclasses import Game, PlayoffGame, Series
from time import sleep
from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from kivy.clock import mainthread, Clock
from kivy.graphics import *


# These lists are defined at the top following the style of my codebase, but are not used until far later.
teams = []
atlanticTeams = []
metroTeams = []
centralTeams = []
pacificTeams = []
easternPlayoffTeams = []
westernPlayoffTeams = []

# The 'data' parameter refers to the information gotten from 'information.json' on lines 249-256 
def getTeamNames(data):
    teamNames = []
    for team in data['teams']:
        teamNames.append(team['teamName'])

    return teamNames

def getTeamConferences(data):
    teamConferences = []

    for team in data['teams']:
        teamConferences.append(team['conference'])

    return teamConferences

def getTeamDivisions(data):
    teamDivisions = []

    for team in data['teams']:
        teamDivisions.append(team['division'])

    return teamDivisions

# This creats the entire list of all of the players, which are then separated by team
def getPlayersList(teamNames, data):
    playersList = []
    for x in range(len(data['teams'])):
        for i in data['teams'][x]['roster']:
            try:
                playersList.append(Player(teamNames[x], i['playerName'], i['playerPosition'], i['stats']['gamesPlayed'], i['stats']['goals'], i['stats']['assists'], i['stats']['points'], i['stats']['plusMinus'], i['stats']['timeOnIcePerGame'], 0))
            except:
                try:
                    playersList.append(Goalie(teamNames[x], i['playerName'], i['playerPosition'], i['stats']['gamesPlayed'], i['stats']['wins'], i['stats']['losses'], i['stats']['savePercentage'], i['stats']['goalsAgainstAverage'], 0))

                except:
                    continue
    return playersList

def getTeamRoster(currTeamName):
    currTeamObject = Team(currTeamName, [], None, None)
    for player in playersList:
        if player.teamName == currTeamName:
            currTeamObject.roster.append(player)

    return currTeamObject

# There may be a way to do this by removing teams from their respective lists, which could be useful for creating home and away games later.
def createSchedule(atlantic, metro, central, pacific):
    schedule = [[] for i in range(214)]
    extraCentralTeams = []
    gameDays = []

    for atlanticTeam in atlantic:
        atlanticCopy = [x for x in atlantic if x != atlanticTeam]

        for otherAtlanticTeam in atlanticCopy:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)
                while (day in atlanticTeam.gameDays or day in otherAtlanticTeam.gameDays):
                    day = day + 1 if day < (len(schedule) - 1) else 0

                atlanticTeam.gameDays.append(day)
                otherAtlanticTeam.gameDays.append(day)
                schedule[day].append(Game(atlanticTeam, otherAtlanticTeam, day))

        for metroTeam in metro:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)
                while (day in atlanticTeam.gameDays or day in metroTeam.gameDays):
                    day = day + 1 if day < (len(schedule) - 1) else 0

                atlanticTeam.gameDays.append(day)
                metroTeam.gameDays.append(day)
                schedule[day].append(Game(atlanticTeam, metroTeam, day))

        for centralTeam in central:
            day = random.randint(0, len(schedule) - 1)
            while (day in atlanticTeam.gameDays or day in centralTeam.gameDays):
                day = day + 1 if day < (len(schedule) - 1) else 0

            atlanticTeam.gameDays.append(day)
            centralTeam.gameDays.append(day)
            schedule[day].append(Game(atlanticTeam, centralTeam, day))

        for pacificTeam in pacific:
            day = random.randint(0, len(schedule) - 1)
            while (day in atlanticTeam.gameDays or day in pacificTeam.gameDays):
                day = day + 1 if day < (len(schedule) - 1) else 0

            atlanticTeam.gameDays.append(day)
            pacificTeam.gameDays.append(day)
            schedule[day].append(Game(atlanticTeam, pacificTeam, day))

    for metroTeam in metro:
        metroCopy = [x for x in metro if x != metroTeam]
        gameDays = []

        for otherMetroTeam in metroCopy:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)

                while (day in metroTeam.gameDays or day in otherMetroTeam.gameDays):
                    day = day + 1 if day < (len(schedule) - 1) else 0

                metroTeam.gameDays.append(day)
                otherMetroTeam.gameDays.append(day)
                schedule[day].append(Game(metroTeam, otherMetroTeam, day))

        for atlanticTeam in atlantic:
            day = random.randint(0, len(schedule) - 1)

            while (day in metroTeam.gameDays or day in atlanticTeam.gameDays):
                day = random.randint(0, len(schedule) - 1)

            metroTeam.gameDays.append(day)
            atlanticTeam.gameDays.append(day)
            schedule[day].append(Game(metroTeam, atlanticTeam, day))

        for centralTeam in central:
            day = random.randint(0, len(schedule) - 1)

            while (day in metroTeam.gameDays or day in centralTeam.gameDays):
                day = day + 1 if day < (len(schedule) - 1) else 0

            metroTeam.gameDays.append(day)
            centralTeam.gameDays.append(day)
            schedule[day].append(Game(metroTeam, centralTeam, day))

        for pacificTeam in pacific:
            day = random.randint(0, len(schedule) - 1)

            while (day in metroTeam.gameDays or day in pacificTeam.gameDays):
                day = day + 1 if day < (len(schedule) - 1) else 0

            metroTeam.gameDays.append(day)
            pacificTeam.gameDays.append(day)
            schedule[day].append(Game(metroTeam, pacificTeam, day))

    for centralTeam in central:
        centralCopy = [x for x in central if x != centralTeam]
        gameDays = []

        for otherCentralTeam in centralCopy:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)

                while (day in centralTeam.gameDays or day in otherCentralTeam.gameDays):
                    day = day + 1 if day < (len(schedule) - 1) else 0

                centralTeam.gameDays.append(day)
                otherCentralTeam.gameDays.append(day)
                schedule[day].append(Game(centralTeam, otherCentralTeam, day))

        for atlanticTeam in atlantic:
            day = random.randint(0, len(schedule) - 1)

            while (day in centralTeam.gameDays or day in atlanticTeam.gameDays):
                day = day + 1 if day < (len(schedule) - 1) else 0

            centralTeam.gameDays.append(day)
            atlanticTeam.gameDays.append(day)
            schedule[day].append(Game(centralTeam, atlanticTeam, day))

        for metroTeam in metro:
            day = random.randint(0, len(schedule) - 1)

            while (day in centralTeam.gameDays or day in metroTeam.gameDays):
                day = day + 1 if day < (len(schedule) - 1) else 0

            centralTeam.gameDays.append(day)
            metroTeam.gameDays.append(day)
            schedule[day].append(Game(centralTeam, metroTeam, day))

        for pacificTeam in pacific:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)

                while (day in centralTeam.gameDays or day in pacificTeam.gameDays):
                    day = day + 1 if day < (len(schedule) - 1) else 0

                centralTeam.gameDays.append(day)
                pacificTeam.gameDays.append(day)
                schedule[day].append(Game(centralTeam, pacificTeam, day))

        extraCentralTeam = centralCopy[random.randint(0, len(centralCopy) - 1)]

        while (extraCentralTeam in extraCentralTeams):
            extraCentralTeam = central[random.randint(0, len(central) - 1)]

        day = random.randint(0, len(schedule) - 1)

        while (day in centralTeam.gameDays or day in extraCentralTeam.gameDays):
            day = day + 1 if day < (len(schedule) - 1) else 0

        extraCentralTeams.append(extraCentralTeam)
        centralTeam.gameDays.append(day)
        extraCentralTeam.gameDays.append(day)
        schedule[day].append(Game(centralTeam, extraCentralTeam, day))

    for pacificTeam in pacific:
        pacificCopy = [x for x in pacific if x != pacificTeam]
        gameDays = []

        for otherPacificTeam in pacificCopy:
            for games in range(2):
                day = random.randint(0, len(schedule) - 1)

                while (day in pacificTeam.gameDays or day in otherPacificTeam.gameDays):
                    day = day + 1 if day < (len(schedule) - 1) else 0

                pacificTeam.gameDays.append(day)
                otherPacificTeam.gameDays.append(day)
                schedule[day].append(Game(pacificTeam, otherPacificTeam, day))

        for atlanticTeam in atlantic:
            day = random.randint(0, len(schedule) - 1)

            while (day in pacificTeam.gameDays or day in atlanticTeam.gameDays):
                day = day + 1 if day < (len(schedule) - 1) else 0

            pacificTeam.gameDays.append(day)
            atlanticTeam.gameDays.append(day)
            schedule[day].append(Game(pacificTeam, atlanticTeam, day))

        for metroTeam in metro:
            day = random.randint(0, len(schedule) - 1)

            while (day in pacificTeam.gameDays or day in metroTeam.gameDays):
                day = day + 1 if day < (len(schedule) - 1) else 0

            pacificTeam.gameDays.append(day)
            metroTeam.gameDays.append(day)
            schedule[day].append(Game(pacificTeam, metroTeam, day))

        for centralTeam in central:
            day = random.randint(0, len(schedule) - 1)

            while (day in pacificTeam.gameDays or day in centralTeam.gameDays):
                day = day + 1 if day < (len(schedule) - 1) else 0

            pacificTeam.gameDays.append(day)
            centralTeam.gameDays.append(day)
            schedule[day].append(Game(pacificTeam, centralTeam, day))

    return schedule

def getForwards(players):
    forwards = []
    for player in players:
        if (player.position == 'LW') or (player.position == 'C') or (player.position == 'RW'):
            forwards.append(player)

    return forwards

def getDefensemen(players):
    defensemen = []
    for player in players:
        if (player.position == 'D'):
            defensemen.append(player)

    return defensemen

def getGoalies(players):
    goalies = []
    for player in players:
        if (player.position == 'G'):
            goalies.append(player)

    return goalies

def rankForwards(forwards):
    forwardRankings = [-1]

    for team in teams:
        for forward in forwards:
            currPlayerPPG = (forward.points / forward.gamesPlayed)
            forwardRankings.append(currPlayerPPG)

    forwardRankings.sort()
    forwardRankings = list(dict.fromkeys(forwardRankings))

    return forwardRankings

def rankDefensemen(defensemen):
    defenseRankings = [-1]


    for defenseman in defensemen:
        currPlayerNormalizedPlusMinus = (defenseman.plusMinus / defenseman.gamesPlayed)
        currPlayerPPG = (defenseman.points / defenseman.gamesPlayed)

        defenseRankings.append(currPlayerNormalizedPlusMinus + currPlayerPPG)

    defenseRankings.sort()
    defenseRankings = list(dict.fromkeys(defenseRankings))

    return defenseRankings

def rankGoalies(goalies):
    goalieRankings = [-1]

    for goalie in goalies:
        currGoalieAdjustedSV = (goalie.savePercentage / goalie.goalsAgainstAverage)

        currGoalieWinPct = (goalie.wins / goalie.gamesPlayed)

        goalieRankings.append(currGoalieAdjustedSV + currGoalieWinPct)

    goalieRankings.sort()
    goalieRankings = list(dict.fromkeys(goalieRankings))

    return goalieRankings

def determineForwardOveralls(forwards, forwardRankings):
    baseOverall = 70
    for rank in range(len(forwardRankings)):
        for forward in forwards:
            currForwardValue = (forward.points / forward.gamesPlayed)
            if (currForwardValue == forwardRankings[rank]):
                nearestMultipleOf14 = 14 * round(rank / 14)
                baseOverall += nearestMultipleOf14 / 14

                forward.overall = baseOverall

                baseOverall = 70

def determineDefenseOveralls(defensemen, defenseRankings):
    baseOverall = 70

    for rank in range(len(defenseRankings)):
        for defenseman in defensemen:
            currDefenseValue = (defenseman.plusMinus / defenseman.gamesPlayed) + (defenseman.points / defenseman.gamesPlayed)
            if (currDefenseValue == defenseRankings[rank]):
                nearestMultipleOf10 = 10 * round(rank / 10)
                baseOverall += nearestMultipleOf10 / 10

                defenseman.overall = baseOverall

                baseOverall = 70

def determineGoalieOveralls(goalies, goalieRankings):
    baseOverall = 70

    for rank in range(len(goalieRankings)):
        for goalie in goalies:
            currGoalieValue = (goalie.savePercentage / goalie.goalsAgainstAverage) + (goalie.wins / goalie.gamesPlayed)

            if (currGoalieValue == goalieRankings[rank]):
                nearestMultipleOf3 = 3 * round(rank / 3)
                baseOverall += nearestMultipleOf3 / 3

                goalie.overall = baseOverall

                baseOverall = 70

def simulateRegularSeason(schedule):
    for day in range(len(schedule)):
        for game in range(len(schedule[day])):
            schedule[day][game].simulateGame()

            for player in schedule[day][game].team1.roster:
                player.currSeasonGamesPlayed += 1

            for player in schedule[day][game].team2.roster:
                player.currSeasonGamesPlayed += 1

            schedule[day][game].winner.points += 2

            if (schedule[day][game].wasOvertime):
                schedule[day][game].loser.points += 2

def determineStandings(teams, atlantic, metro, central, pacific, eastern, western):
    teams.sort(key=lambda x: x.points, reverse=True)

    atlantic.sort(key=lambda x: x.points, reverse=True)
    metro.sort(key=lambda x: x.points, reverse=True)
    central.sort(key=lambda x: x.points, reverse=True)
    pacific.sort(key=lambda x: x.points, reverse=True)

    eastern.sort(key=lambda x: x.points, reverse=True)
    western.sort(key=lambda x: x.points, reverse=True)

def getPlayoffTeams(atlantic, metro, central, pacific, eastern, western):
    global easternPlayoffTeams, westernPlayoffTeams
    for playoffTeam in range(3):
        easternPlayoffTeams.append(atlantic[playoffTeam])
        easternPlayoffTeams.append(metro[playoffTeam])

        westernPlayoffTeams.append(central[playoffTeam])
        westernPlayoffTeams.append(pacific[playoffTeam])

    for wildcard in range(2):
        for easternTeam in eastern:
            if easternTeam not in easternPlayoffTeams:
                easternPlayoffTeams.append(easternTeam)
                break

        for westernTeam in western:
            if westernTeam not in westernPlayoffTeams:
                westernPlayoffTeams.append(westernTeam)
                break
# Creates all of the actual lists of teams and players
with open('information.json') as inputFile:
    data = json.load(inputFile)
    teamNames = getTeamNames(data)
    teamConferences = getTeamConferences(data)
    teamDivisions = getTeamDivisions(data)
    playersList = getPlayersList(teamNames, data)

forwards = getForwards(playersList)
defensemen = getDefensemen(playersList)
goalies = getGoalies(playersList)

for i in teamNames:
    teams.append(getTeamRoster(i))

for team in range(len(teams)):
    teams[team].conference = teamConferences[team]
    teams[team].division = teamDivisions[team]

forwardRankings = rankForwards(forwards)
defenseRankings = rankDefensemen(defensemen)
goalieRankings = rankGoalies(goalies)

determineForwardOveralls(forwards, forwardRankings)
determineDefenseOveralls(defensemen, defenseRankings)
determineGoalieOveralls(goalies, goalieRankings)

# Determines what division every team is in to later create the schedule with the above createSchedule function
for team in teams:
    if (team.division == 'Atlantic'):
        atlanticTeams.append(team)
    elif (team.division == 'Metropolitan'):
        metroTeams.append(team)
    elif (team.division == 'Central'):
        centralTeams.append(team)
    elif (team.division == 'Pacific'):
        pacificTeams.append(team)
    else:
        print(team.name + "'s division is not valid " + team.conference)

easternTeams = atlanticTeams + metroTeams
westernTeams = centralTeams + pacificTeams

# Uses the method defined in the Team class
for i in teams:
    i.createAllInfo()

# Initializes empty lists down here because it makes more sense here
easternRound1Winners = []
westernRound1Winners = []

easternRound2Winners = []
westernRound2Winners = []

easternChampion = None
westernChampion = None

def generateRound1(atlantic, metro, central, pacific, eastern, western):
    atlantic.sort(key=lambda x: x.points, reverse=True)
    metro.sort(key=lambda x: x.points, reverse=True)
    central.sort(key=lambda x: x.points, reverse=True)
    pacific.sort(key=lambda x: x.points, reverse=True)
    eastern.sort(key=lambda x: x.points, reverse=True)
    western.sort(key=lambda x: x.points, reverse=True)
    # Pairs are made manually for now
    pairs = []
    currPair = [eastern[0], eastern[7]]
    pairs.append(currPair)
    currPair = [atlantic[1], atlantic[2]]
    pairs.append(currPair)
    currPair = [eastern[1], eastern[6]]
    pairs.append(currPair)
    currPair = [metro[1], metro[2]]
    pairs.append(currPair)

    currPair = [western[0], western[7]]
    pairs.append(currPair)
    currPair = [pacific[1], pacific[2]]
    pairs.append(currPair)
    currPair = [western[1], western[6]]
    pairs.append(currPair)
    currPair = [central[1], central[2]]
    pairs.append(currPair)

    round1 = []

    for pair in pairs:
        seriesSchedule = []
        gameDay = random.randint(0, 1)

        for day in range(7):
            seriesSchedule.append(PlayoffGame(pair[0], pair[1], gameDay))
            gameDay += 2

        round1.append(Series(seriesSchedule))

    return round1

def simulateRound1(round1):
    global easternRound1Winners, westernRound1Winners
    for series in round1:
        series.simulateSeries()

        print(series.seriesWinner.name, "beat the", series.seriesLoser.name, "in their first round matchup. The series went", series.gamesPlayed, "games")
        
        if (series.seriesWinner.conference == "Eastern"):
            easternRound1Winners.append(series.seriesWinner)

        else:
            westernRound1Winners.append(series.seriesWinner)

    print()
    print()

def generateRound2(eastern, western):
    pairs = []
    round2 = []

    currPair = [eastern[0], eastern[1]]
    pairs.append(currPair)
    currPair = [eastern[2], eastern[3]]
    pairs.append(currPair)

    currPair = [western[0], western[1]]
    pairs.append(currPair)
    currPair = [western[2], western[3]]
    pairs.append(currPair)

    for pair in pairs:
        seriesSchedule = []
        gameDay = random.randint(0, 1)

        for day in range(7):
            seriesSchedule.append(PlayoffGame(pair[0], pair[1], gameDay))
            gameDay += 2
        
        round2.append(Series(seriesSchedule))

    return round2

def simulateRound2(round2):
    global easternRound2Winners, westernRound2Winners
    for series in round2:
        series.simulateSeries()

        print(series.seriesWinner.name, "beat the", series.seriesLoser.name, "in their second round matchup. The series went", series.gamesPlayed, "games")

        if (series.seriesWinner.conference == 'Eastern'):
            easternRound2Winners.append(series.seriesWinner)

        else:
            westernRound2Winners.append(series.seriesWinner)

    print()
    print()

def generateRound3(eastern, western):
    gameDay = 0
    easternFinals = []
    round3 = []

    for day in range(7):
        easternFinals.append(PlayoffGame(eastern[0], eastern[1], gameDay))
        gameDay += 2
    
    round3.append(Series(easternFinals))

    gameday = 1
    westernFinals = []

    for day in range(7):
        westernFinals.append(PlayoffGame(western[0], western[1], gameDay))
        gameDay += 2

    round3.append(Series(westernFinals))

    return round3

def simulateRound3(round3):
    global easternChampion, westernChampion
    for series in round3:
        series.simulateSeries()

        print(series.seriesWinner.name, "beat the", series.seriesLoser.name, "in their third round matchup. The series went", series.gamesPlayed, "games")

        if (series.seriesWinner.conference == 'Eastern'):
            easternChampion = series.seriesWinner

        else:
            westernChampion = series.seriesWinner

def generateStanleyCupFinals(eastern, western):
    gameDay = 0
    seriesSchedule = []
    cupFinals = []

    for day in range(7):
        seriesSchedule.append(PlayoffGame(eastern, western, gameDay))
        gameDay += 2

    cupFinals.append(Series(seriesSchedule))

    return cupFinals

def simulateStanleyCupFinals(stanleyCupFinals):
    for series in stanleyCupFinals:
        series.simulateSeries()

    return series.seriesWinner

currTeam = ''
currPlayer = ''
dayStopped = 0
weeks = []
currWeek = 0
dayStopped = 0
gameStopped = 0
finishedRegularSeason = False

round1 = None
round1Generated = False
finishedRound1 = False

round2 = None
round2Generated = False
finishedRound2 = False

round3 = None
round3Generated = False
finishedRound3 = False

round4 = None
round4Generated = False
finishedRound4 = False

seasonSchedule = createSchedule(atlanticTeams, metroTeams, centralTeams, pacificTeams)

simScreenWasSwitched = False

class OneWeek(Widget):
    pass

class CalendarComponent(Widget):
    pass

class Manager(ScreenManager):
    pass

class MainMenuScreen(Screen):
    pass

class AboutScreen(Screen):
    pass

class AdditionalInformationScreen(Screen):
    pass

class TeamHomeScreen(Screen):
    @mainthread
    def on_enter(self):
        self.ids.TeamHomeScreenTitle.text = currTeam
        self.ids.TeamHomeScreenLogo.source = str('imgs/' + currTeam + '.png')
        
        self.separateIntoWeeks(seasonSchedule)
        self.updateRecord()

        self.currWeek = currWeek

        self.populateWeek(self.currWeek)

        self.game = 0
        self.day = 0
        self.weekHasChanged = False

        self.simulationIsStopped = True

    def on_leave(self):
        global currWeek, simScreenWasSwitched, dayStopped, gameStopped
        currWeek = self.currWeek
        simScreenWasSwitched = True

        dayStopped = self.day
        gameStopped = self.game

    def goToAdditionalInformation(self):
        if (self.simulationIsStopped):
            self.manager.current = 'AdditionalInformationScreen'

        else:
            print("Stop the simulation first please")

    def stopSimulation(self):
        self.simulationIsStopped = True
        
    def runSimulation(self):
        self.simulationIsStopped = False
        Clock.schedule_interval(self.simulate, 0.2)
        
    def updateRecord(self):
        for team in teams:
            if (team.name == currTeam):
                currTeamWins = team.wins
                currTeamLosses = team.losses
                currTeamOvertimeLosses = team.overtimeLosses

        recordString = '{}-{}-{}'.format(currTeamWins, currTeamLosses, currTeamOvertimeLosses)
       
        self.ids.CurrTeamRecord.text = recordString

    def simulate(self, dt):
        global finishedRegularSeason, round1, round1Generated, finishedRound1, round2, round2Generated, finishedRound2, round3, round3Generated, finishedRound3, round4, round4Generated, finishedRound4
        if (not self.simulationIsStopped) and (not finishedRegularSeason):
            global simScreenWasSwitched, dayStopped, gameStopped, seasonSchedule

            if (simScreenWasSwitched):
                self.day = dayStopped
                self.game = gameStopped
                simScreenWasSwitched = False

            seasonSchedule[self.day][self.game].simulateGame()

            seasonSchedule[self.day][self.game].winner.wins += 1
            if (not seasonSchedule[self.day][self.game].wasOvertime):
                seasonSchedule[self.day][self.game].loser.losses += 1

            else:
                seasonSchedule[self.day][self.game].loser.overtimeLosses += 1

            self.updateRecord()

            if (self.day % 7 == 0):
                self.ids.MainCalendar.ids.Sunday.ids.CalendarLogo.source = 'imgs/gray.png'

            elif (self.day % 7 == 1):
                self.ids.MainCalendar.ids.Monday.ids.CalendarLogo.source = 'imgs/gray.png'
            
            elif (self.day % 7 == 2):
                self.ids.MainCalendar.ids.Tuesday.ids.CalendarLogo.source = 'imgs/gray.png'

            elif (self.day % 7 == 3):
                self.ids.MainCalendar.ids.Wednesday.ids.CalendarLogo.source = 'imgs/gray.png'

            elif (self.day % 7 == 4):
                self.ids.MainCalendar.ids.Thursday.ids.CalendarLogo.source = 'imgs/gray.png'
            
            elif (self.day % 7 == 5):
                self.ids.MainCalendar.ids.Friday.ids.CalendarLogo.source = 'imgs/gray.png'

            elif (self.day % 7 == 6):
                self.ids.MainCalendar.ids.Saturday.ids.CalendarLogo.source = 'imgs/gray.png'

            if (seasonSchedule[self.day][self.game].team1.name == currTeam or seasonSchedule[self.day][self.game].team2.name == currTeam):
                if (self.day % 7 == 0):
                    if (seasonSchedule[self.day][self.game].winner.name == currTeam):
                        self.ids.MainCalendar.ids.Sunday.ids.GameScore.text = 'W \n {} - {}'.format(seasonSchedule[self.day][self.game].team1Score, seasonSchedule[self.day][self.game].team2Score)
                
                    else:
                        self.ids.MainCalendar.ids.Sunday.ids.GameScore.text = 'L \n {} - {}'.format(seasonSchedule[self.day][self.game].team1Score, seasonSchedule[self.day][self.game].team2Score)

                elif (self.day % 7 == 1):
                    if (seasonSchedule[self.day][self.game].winner.name == currTeam):
                        self.ids.MainCalendar.ids.Monday.ids.GameScore.text = 'W \n {} - {}'.format(seasonSchedule[self.day][self.game].team1Score, seasonSchedule[self.day][self.game].team2Score)
                
                    else:
                        self.ids.MainCalendar.ids.Monday.ids.GameScore.text = 'L \n {} - {}'.format(seasonSchedule[self.day][self.game].team1Score, seasonSchedule[self.day][self.game].team2Score)

                elif (self.day % 7 == 2):
                    if (seasonSchedule[self.day][self.game].winner.name == currTeam):
                        self.ids.MainCalendar.ids.Tuesday.ids.GameScore.text = 'W \n {} - {}'.format(seasonSchedule[self.day][self.game].team1Score, seasonSchedule[self.day][self.game].team2Score)
                
                    else:
                        self.ids.MainCalendar.ids.Tuesday.ids.GameScore.text = 'L \n {} - {}'.format(seasonSchedule[self.day][self.game].team1Score, seasonSchedule[self.day][self.game].team2Score)

                elif (self.day % 7 == 3):
                    if (seasonSchedule[self.day][self.game].winner.name == currTeam):
                        self.ids.MainCalendar.ids.Wednesday.ids.GameScore.text = 'W \n {} - {}'.format(seasonSchedule[self.day][self.game].team1Score, seasonSchedule[self.day][self.game].team2Score)
                
                    else:
                        self.ids.MainCalendar.ids.Wednesday.ids.GameScore.text = 'L \n {} - {}'.format(seasonSchedule[self.day][self.game].team1Score, seasonSchedule[self.day][self.game].team2Score)

                elif (self.day % 7 == 4):
                    if (seasonSchedule[self.day][self.game].winner.name == currTeam):
                        self.ids.MainCalendar.ids.Thursday.ids.GameScore.text = 'W \n {} - {}'.format(seasonSchedule[self.day][self.game].team1Score, seasonSchedule[self.day][self.game].team2Score)
                
                    else:
                        self.ids.MainCalendar.ids.Thursday.ids.GameScore.text = 'L \n {} - {}'.format(seasonSchedule[self.day][self.game].team1Score, seasonSchedule[self.day][self.game].team2Score)

                elif (self.day % 7 == 5):
                    if (seasonSchedule[self.day][self.game].winner.name == currTeam):
                        self.ids.MainCalendar.ids.Friday.ids.GameScore.text = 'W \n {} - {}'.format(seasonSchedule[self.day][self.game].team1Score, seasonSchedule[self.day][self.game].team2Score)
                
                    else:
                        self.ids.MainCalendar.ids.Friday.ids.GameScore.text = 'L \n {} - {}'.format(seasonSchedule[self.day][self.game].team1Score, seasonSchedule[self.day][self.game].team2Score)

                elif (self.day % 7 == 6):
                    if (seasonSchedule[self.day][self.game].winner.name == currTeam):
                        self.ids.MainCalendar.ids.Saturday.ids.GameScore.text = 'W \n {} - {}'.format(seasonSchedule[self.day][self.game].team1Score, seasonSchedule[self.day][self.game].team2Score)
                
                    else:
                        self.ids.MainCalendar.ids.Saturday.ids.GameScore.text = 'L \n {} - {}'.format(seasonSchedule[self.day][self.game].team1Score, seasonSchedule[self.day][self.game].team2Score)


            if (self.game < len(seasonSchedule[self.day]) - 1):
                self.game += 1
            
            else:
                if (self.day % 7 == 6):
                    self.currWeek += 1
                    self.populateWeek(self.currWeek)

                self.game = 0
                self.day += 1

    def separateIntoWeeks(self, stageToSeparate):
        global weeks, seasonSchedule, finishedRegularSeason
        currWeek = []

        for day in range(len(stageToSeparate)):
            currWeek.append(stageToSeparate[day])

            if (day % 7 == 0) and (day > 0):
                weeks.append(currWeek)
                currWeek = []

            if (day >= len(stageToSeparate)):
                finishedRegularSeason = True

    def populateWeek(self, currWeek):
        global weeks, finishedRegularSeason

        self.sundayImg = 'imgs/white.png'
        self.mondayImg = 'imgs/white.png'
        self.tuesdayImg = 'imgs/white.png'
        self.wednesdayImg = 'imgs/white.png'
        self.thursdayImg = 'imgs/white.png'
        self.fridayImg = 'imgs/white.png'
        self.saturdayImg = 'imgs/white.png'

        self.ids.MainCalendar.ids.Sunday.ids.GameScore.text = ''
        self.ids.MainCalendar.ids.Monday.ids.GameScore.text = ''
        self.ids.MainCalendar.ids.Tuesday.ids.GameScore.text = ''
        self.ids.MainCalendar.ids.Wednesday.ids.GameScore.text = ''
        self.ids.MainCalendar.ids.Thursday.ids.GameScore.text = ''
        self.ids.MainCalendar.ids.Friday.ids.GameScore.text = ''
        self.ids.MainCalendar.ids.Saturday.ids.GameScore.text = ''

        try:
            for day in range(len(weeks[currWeek])):
                for game in range(len(weeks[currWeek][day])):
                        if (currWeek == 0):
                            if (weeks[currWeek][day][game].team1.name == currTeam):
                                if (day % 7 == 0):
                                    self.sundayImg = str('imgs/' + weeks[currWeek][day][game].team2.name + '.png')

                                elif (day % 7 == 1):
                                    self.mondayImg = str('imgs/' + weeks[currWeek][day][game].team2.name + '.png')

                                elif (day % 7 == 2):
                                    self.tuesdayImg = str('imgs/' + weeks[currWeek][day][game].team2.name + '.png')

                                elif (day % 7 == 3):
                                    self.wednesdayImg = str('imgs/' + weeks[currWeek][day][game].team2.name + '.png')    

                                elif (day % 7 == 4):
                                    self.thursdayImg = str('imgs/' + weeks[currWeek][day][game].team2.name + '.png')

                                elif (day % 7 == 5):
                                    self.fridayImg = str('imgs/' + weeks[currWeek][day][game].team2.name + '.png')

                                elif (day % 7 == 6):
                                    self.saturdayImg = str('imgs/' + weeks[currWeek][day][game].team2.name + '.png')

                            elif (weeks[currWeek][day][game].team2.name == currTeam):
                                if (day % 7 == 0):
                                    self.sundayImg = str('imgs/' + weeks[currWeek][day][game].team1.name + '.png')

                                elif (day % 7 == 1):
                                    self.mondayImg = str('imgs/' + weeks[currWeek][day][game].team1.name + '.png')

                                elif (day % 7 == 2):
                                    self.tuesdayImg = str('imgs/' + weeks[currWeek][day][game].team1.name + '.png')

                                elif (day % 7 == 3):
                                    self.wednesdayImg = str('imgs/' + weeks[currWeek][day][game].team1.name + '.png')

                                elif (day % 7 == 4):
                                    self.thursdayImg = str('imgs/' + weeks[currWeek][day][game].team1.name + '.png')

                                elif (day % 7 == 5):
                                    self.fridayImg = str('imgs/' + weeks[currWeek][day][game].team1.name + '.png')    

                                elif (day % 7 == 6):
                                    self.saturdayImg = str('imgs/' + weeks[currWeek][day][game].team1.name + '.png')    

                        else:
                            if (weeks[currWeek][day][game].team1.name == currTeam):
                                if (day + 1 % 7 == 0):
                                    self.sundayImg = str('imgs/' + weeks[currWeek][day][game].team2.name + '.png')

                                elif (day + 1 % 7 == 1):
                                    self.mondayImg = str('imgs/' + weeks[currWeek][day][game].team2.name + '.png')

                                elif (day + 1 % 7 == 2):
                                    self.tuesdayImg = str('imgs/' + weeks[currWeek][day][game].team2.name + '.png')

                                elif (day + 1 % 7 == 3):
                                    self.wednesdayImg = str('imgs/' + weeks[currWeek][day][game].team2.name + '.png')    

                                elif (day + 1 % 7 == 4):
                                    self.thursdayImg = str('imgs/' + weeks[currWeek][day][game].team2.name + '.png')

                                elif (day + 1 % 7 == 5):
                                    self.fridayImg = str('imgs/' + weeks[currWeek][day][game].team2.name + '.png')

                                elif (day + 1 % 7 == 6):
                                    self.saturdayImg = str('imgs/' + weeks[currWeek][day][game].team2.name + '.png')

                            elif (weeks[currWeek][day][game].team2.name == currTeam):
                                if (day + 1 % 7 == 0):
                                    self.sundayImg = str('imgs/' + weeks[currWeek][day][game].team1.name + '.png')

                                elif (day + 1 % 7 == 1):
                                    self.mondayImg = str('imgs/' + weeks[currWeek][day][game].team1.name + '.png')

                                elif (day + 1 % 7 == 2):
                                    self.tuesdayImg = str('imgs/' + weeks[currWeek][day][game].team1.name + '.png')

                                elif (day + 1 % 7 == 3):
                                    self.wednesdayImg = str('imgs/' + weeks[currWeek][day][game].team1.name + '.png')

                                elif (day + 1 % 7 == 4):
                                    self.thursdayImg = str('imgs/' + weeks[currWeek][day][game].team1.name + '.png')

                                elif (day + 1 % 7 == 5):
                                    self.fridayImg = str('imgs/' + weeks[currWeek][day][game].team1.name + '.png')    

                                elif (day + 1 % 7 == 6):
                                    self.saturdayImg = str('imgs/' + weeks[currWeek][day][game].team1.name + '.png')    

            self.ids.MainCalendar.ids.Sunday.ids.CalendarLogo.source = self.sundayImg
            self.ids.MainCalendar.ids.Monday.ids.CalendarLogo.source = str(self.mondayImg)
            self.ids.MainCalendar.ids.Tuesday.ids.CalendarLogo.source = str(self.tuesdayImg)
            self.ids.MainCalendar.ids.Wednesday.ids.CalendarLogo.source = str(self.wednesdayImg)
            self.ids.MainCalendar.ids.Thursday.ids.CalendarLogo.source = str(self.thursdayImg)
            self.ids.MainCalendar.ids.Friday.ids.CalendarLogo.source = str(self.fridayImg)
            self.ids.MainCalendar.ids.Saturday.ids.CalendarLogo.source = str(self.saturdayImg)

        except IndexError:
            print("Regular season finished!")
            finishedRegularSeason = True

class ChooseTeamScreen(Screen):
    def __init__(self, **kwargs):
        super(ChooseTeamScreen, self).__init__(**kwargs)
        self.currTeam = ''

    def getCurrTeam(self, instance):
        global currTeam
        currTeam = instance.text
        self.manager.current = 'TeamHomeScreen'

class CurrentTeamForwardLineScreen(Screen):
    def getCurrPlayer(self, instance):
        global currPlayer
        currPlayer = instance.text
        self.manager.current = 'CurrentPlayerInfoScreen'

    @mainthread
    def on_enter(self):
        for team in teams:
            if team.name == currTeam:
                currTeamForwardLines = team.forwardLines
                break

        self.ids.FirstLineLW.text = currTeamForwardLines[0][0].playerName
        self.ids.FirstLineC.text = currTeamForwardLines[0][1].playerName
        self.ids.FirstLineRW.text = currTeamForwardLines[0][2].playerName
        self.ids.SecondLineLW.text = currTeamForwardLines[1][0].playerName
        self.ids.SecondLineC.text = currTeamForwardLines[1][1].playerName
        self.ids.SecondLineRW.text = currTeamForwardLines[1][2].playerName
        self.ids.ThirdLineLW.text = currTeamForwardLines[2][0].playerName
        self.ids.ThirdLineC.text = currTeamForwardLines[2][1].playerName
        self.ids.ThirdLineRW.text = currTeamForwardLines[2][2].playerName
        self.ids.FourthLineLW.text = currTeamForwardLines[3][0].playerName
        self.ids.FourthLineC.text = currTeamForwardLines[3][1].playerName
        self.ids.FourthLineRW.text = currTeamForwardLines[3][2].playerName

        self.ids.TeamForwardLinesLogo.source = 'imgs/' + currTeam + '.png'

class CurrentTeamDefenseLineScreen(Screen):

    def getCurrPlayer(self, instance):
        global currPlayer
        currPlayer = instance.text
        self.manager.current = 'CurrentPlayerInfoScreen'

    @mainthread
    def on_enter(self):
        for team in teams:
            if (team.name == currTeam):
                currTeamDefenseLines = team.defenseLines
                break

        self.ids.FirstLineLD.text = currTeamDefenseLines[0][0].playerName
        self.ids.FirstLineRD.text = currTeamDefenseLines[0][1].playerName
        self.ids.SecondLineLD.text = currTeamDefenseLines[1][0].playerName
        self.ids.SecondLineRD.text = currTeamDefenseLines[1][1].playerName
        self.ids.ThirdLineLD.text = currTeamDefenseLines[2][0].playerName
        self.ids.ThirdLineRD.text = currTeamDefenseLines[2][1].playerName

        self.ids.TeamDefenseLinesLogo.source = 'imgs/' + currTeam + '.png'

class CurrentTeamGoalieLineScreen(Screen):
    def getCurrPlayer(self, instance):
        global currPlayer
        currPlayer = instance.text
        self.manager.current = 'CurrentPlayerInfoScreen'

    @mainthread
    def on_enter(self):
        for team in teams:
            if (team.name == currTeam):
                currTeamGoalies = team.goalieLines
                break

        self.ids.StartingGoalie.text = currTeamGoalies[0].playerName
        self.ids.BackupGoalie.text = currTeamGoalies[1].playerName

        self.ids.TeamGoalieLinesLogo.source = 'imgs/' + currTeam + '.png'

class CurrentPlayerInfoScreen(Screen):
    @mainthread
    def on_enter(self):
        self.currSeason = 0
        self.currPlayerName = currPlayer
        self.isGoalie = False

        self.getCurrentPlayerInfo()

        self.changeSeason()

    def getCurrentPlayerInfo(self):
        for player in playersList:
            if (player.playerName == currPlayer):
                try:
                    self.currPlayerOverall = player.overall
                    self.currPlayerLastSeasonGamesPlayed = player.gamesPlayed
                    self.currPlayerLastSeasonGoals = player.goals
                    self.currPlayerLastSeasonAssists = player.assists
                    self.currPlayerLastSeasonPoints = player.points

                    self.currPlayerCurrSeasonGamesPlayed = player.currSeasonGamesPlayed
                    self.currPlayerCurrSeasonGoals = player.currSeasonGoals
                    self.currPlayerCurrSeasonAssists = player.currSeasonAssists
                    self.currPlayerCurrSeasonPoints = player.currSeasonPoints

                except:
                    self.currPlayerOverall = player.overall
                    self.currPlayerLastSeasonGamesPlayed = player.gamesPlayed
                    self.currPlayerLastSeasonWins = player.wins
                    self.currPlayerLastSeasonSavePerecentage = player.savePercentage
                    self.currPlayerLastSeasonGoalsAgainstAverage = player.goalsAgainstAverage

                    self.currPlayerCurrSeasonGamesPlayed = player.currSeasonGamesPlayed
                    self.currPlayerCurrSeasonWins = player.currSeasonWins
                    self.currPlayerCurrSeasonSavePerecentage = player.currSeasonSavePercentage
                    self.currPlayerCurrSeasonGoalsAgainstAverage = player.currSeasonGoalsAgainstAverage

                    self.isGoalie = True
                
                finally:
                    break

        self.ids.CurrentPlayerName.text = currPlayer + ' - ' + str(self.currPlayerOverall) + ' Overall.'
        self.ids.CurrentPlayerInformationLogo.source = 'imgs/' + currTeam + '.png'

    def changeSeason(self):
        if (self.currSeason == 1):
            self.ids.LatestSeason.text = '2019-2020'

            if (not self.isGoalie):
                self.ids.GamesPlayed.text = 'Games Played: '
                self.ids.LatestSeasonGamesPlayed.text = str(self.currPlayerLastSeasonGamesPlayed)

                self.ids.Stat1.text = 'Goals: '
                self.ids.LatestStat1.text = str(self.currPlayerLastSeasonGoals)

                self.ids.Stat2.text = 'Assists: '
                self.ids.LatestStat2.text = str(self.currPlayerLastSeasonAssists)

                self.ids.Stat3.text = 'Points'
                self.ids.LatestStat3.text = str(self.currPlayerLastSeasonPoints)

            else:
                self.ids.GamesPlayed.text = 'Games Played: '
                self.ids.LatestSeasonGamesPlayed.text = str(self.currPlayerLastSeasonGamesPlayed)

                self.ids.Stat1.text = 'Wins: '
                self.ids.LatestStat1.text = str(self.currPlayerLastSeasonWins)

                self.ids.Stat2.text = 'Save Percentage: '
                self.ids.LatestStat2.text = str(self.currPlayerLastSeasonSavePerecentage)

                self.ids.Stat3.text = 'Goals Against Average: '
                self.ids.LatestStat3.text = str(self.currPlayerLastSeasonGoalsAgainstAverage)

        if (self.currSeason == 0):
            self.ids.LatestSeason.text = '2020-2021'

            if (not self.isGoalie):
                self.ids.GamesPlayed.text = 'Games Played: '
                self.ids.LatestSeasonGamesPlayed.text = str(self.currPlayerCurrSeasonGamesPlayed)

                self.ids.Stat1.text = 'Goals: '
                self.ids.LatestStat1.text = str(self.currPlayerCurrSeasonGoals)

                self.ids.Stat2.text = 'Assists: '
                self.ids.LatestStat2.text = str(self.currPlayerCurrSeasonAssists)

                self.ids.Stat3.text = 'Points'
                self.ids.LatestStat3.text = str(self.currPlayerCurrSeasonPoints)

            else:
                self.ids.GamesPlayed.text = 'Games Played: '
                self.ids.LatestSeasonGamesPlayed.text = str(self.currPlayerCurrSeasonGamesPlayed)

                self.ids.Stat1.text = 'Wins: '
                self.ids.LatestStat1.text = str(self.currPlayerCurrSeasonWins)

                self.ids.Stat2.text = 'Save Percentage: '
                self.ids.LatestStat2.text = str(self.currPlayerCurrSeasonSavePerecentage)

                self.ids.Stat3.text = 'Goals Against Average: '
                self.ids.LatestStat3.text = str(self.currPlayerCurrSeasonGoalsAgainstAverage)

        if (self.currSeason == 0):
            self.currSeason = 1

        else:
            self.currSeason = 0

class LeagueStandingsScreen(Screen):
    @mainthread
    def on_enter(self):
        self.conferences = ["Eastern", "Western"]

        for team in teams:
            if (team.name == currTeam):
                self.currConference = self.conferences.index(team.conference)
                break
    
        self.populateConference()

    def populateConference(self):
        global atlanticTeams, metroTeams
        self.ids.CurrConference.text = '{} Conference'.format(self.conferences[self.currConference])

        divOneTop3String  = ''
        divTwoTop3String = ''
        remainingConferenceString = ''

        divOneTop3 = []
        divTwoTop3 = []
        conferenceTeamsRemaining = []

        if (self.currConference == 0):
            self.ids.DivOne.text = "Atlantic Division"
            self.ids.DivTwo.text = "Metropolitan Division"

            atlanticTeams.sort(key=lambda x: x.points, reverse=True)
            metroTeams.sort(key=lambda x: x.points, reverse=True)
            easternTeams.sort(key=lambda x: x.points, reverse=True)

            for team in range(3):
                divOneTop3.append(atlanticTeams[team])
                divTwoTop3.append(metroTeams[team])

            for team in easternTeams:
                if (team in divOneTop3 or team in divTwoTop3):
                    pass

                else:
                    conferenceTeamsRemaining.append(team)

            for atlanticTeam in range(len(divOneTop3)):
                divOneTop3String += ('{}. {} - {} points\n'.format(atlanticTeam + 1, divOneTop3[atlanticTeam].name, divOneTop3[atlanticTeam].points))

            for metroTeam in range(len(divTwoTop3)):
                divTwoTop3String += ('{}. {} - {} points\n'.format(metroTeam + 1, divTwoTop3[metroTeam].name, divTwoTop3[metroTeam].points))

            for easternTeam in range(len(conferenceTeamsRemaining)):
                remainingConferenceString +=('{}. {} - {} points\n\n'.format(easternTeam + 1, conferenceTeamsRemaining[easternTeam].name, conferenceTeamsRemaining[easternTeam].points))

        else:
            self.ids.DivOne.text = "Central Division"
            self.ids.DivTwo.text = "Pacific Division"

            centralTeams.sort(key=lambda x: x.points, reverse=True)
            pacificTeams.sort(key=lambda x: x.points, reverse=True)
            westernTeams.sort(key=lambda x: x.points, reverse=True)

            for team in range(3):
                divOneTop3.append(centralTeams[team])
                divTwoTop3.append(pacificTeams[team])

            for team in westernTeams:
                if (team in divOneTop3 or team in divTwoTop3):
                    pass

                else:
                    conferenceTeamsRemaining.append(team)

            for centralTeam in range(len(divOneTop3)):
                divOneTop3String += ('{}. {} - {} points\n'.format(centralTeam + 1, divOneTop3[centralTeam].name, divOneTop3[centralTeam].points))

            for pacificTeam in range(len(divTwoTop3)):
                divTwoTop3String += ('{}. {} - {} points\n'.format(pacificTeam + 1, divTwoTop3[pacificTeam].name, divTwoTop3[pacificTeam].points))

            for westernTeam in range(len(conferenceTeamsRemaining)):
                remainingConferenceString +=('{}. {} - {} points\n\n'.format(westernTeam + 1, conferenceTeamsRemaining[westernTeam].name, conferenceTeamsRemaining[westernTeam].points))

        self.ids.DivOneTopThree.text = divOneTop3String
        self.ids.DivTwoTopThree.text = divTwoTop3String
        self.ids.RestOfConferenceTeams.text = remainingConferenceString

    def changeConference(self):
        if (self.currConference == 0):
            self.currConference = 1

        else:
            self.currConference = 0

        self.populateConference()

class NHLSimulationApp(App):
    def build(self):
        return Manager()

if __name__ == '__main__':
    NHLSimulationApp().run()