# NHL Simulation

## Installation
1. Clone this repository into a directory using
`$ git clone --recursive https://github.com/ReezanVisram/NHLSimulation.git`

2. Ensure you have the latest version of both Python and Pip Package Manager installed.
Install the latest version of Pip using
`$ python -m pip install --upgrade pip`

3. With the latest version of both Python and Pip installed, run the command
`$ python -m pip install -r requirements.txt`

Optionally, create a Virtual Environment by first installing vritualenv with pip and creating and activating one.

4. Everything is now installed. You are now ready to use the Simulation!

## Usage
1. Run the scraper.py file by going into the directory the Simulation is installed in and using the command
`$ python scraper.py`
This will create the information.json file required for the engine to get all of the information about the players.

More information about the scraper can be found [here].

2. Run the engine.py file, which will create and simulate every single game of the season, output every single team's place at the end of the season, generate the playoff bracket and simulate each playoff series, and crown the eventual Stanley Cup Champion!