import io
import csv
import sys
import math
import time
import logging
import datetime
import textAdventureFormatting
import textAdventureSceneLoader

def loggingWrapper(text):
    loggingCsv.info(text)
    loggingLog.info(str(datetime.datetime.now()) + " -- " + text)

class csvFormatter(logging.Formatter):
    def __init__(self):
        super().__init__()
        self.output = io.StringIO()
        self.writer = csv.writer(self.output, quoting=csv.QUOTE_ALL)

    def format(self, record):
        self.writer.writerow([record.levelname, datetime.datetime.now(), record.msg])
        data = self.output.getvalue()
        self.output.truncate(0)
        self.output.seek(0)
        return data.strip()

def setup_logger(name, log_file, formatter = False, level=logging.INFO):
    handler = logging.FileHandler(log_file)        

    if formatter:
        handler.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(level)
    logger.addHandler(handler)

    return logger

loggingCsv = setup_logger("loggingCsv", "logger.csv", csvFormatter())
loggingLog = setup_logger("loggingLog", "logger.log")

def inputWrapper(text):
    gameState.lastRepeated = ""
    return input(text)

class gameState:
    def __init__(self, name, mode):
        self._name = name
        self._hp = textAdventureSceneLoader.Difficulty[mode.upper()].value

    inventory = {}
    lastRepeated = ""
    scene = 0

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, newValue):
        self._name = newValue

    @property
    def hp(self):
        return self._hp

    @hp.setter
    def hp(self, newValue):
        self._hp = newValue

    def takeDamange(self, amount):
        self._hp -= amount

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

gameScenes = textAdventureSceneLoader.getScene("montyPython")

def getCurrentScene(sceneNum):
    for scene in gameScenes:
        if scene.sceneCode == sceneNum:
            return scene

    loggingWrapper("Tried to load non-existant scene - #" + str(sceneNum))
    sys.exit()

def doTurn():
    scene = getCurrentScene(gameState.scene)

    loggingWrapper("Arrived at: #" + str(scene.sceneCode) + " - " + scene.area + " - Player HP: " + str(gameState.hp))

    if(scene.asciiFile):
        gameState.lastRepeated = textAdventureFormatting.displayAscii(scene.asciiFile)

    for text in scene.preText:
        gameState.lastRepeated = textAdventureFormatting.gamePrint(text, "*", gameState.lastRepeated)

    print("")
    optionText = ""
    options = []
    for option in scene.options:
        optionText += option.name.capitalize() + " "
        options.append(option.name.lower())

    playerInput = ""
    while playerInput not in options:
        playerInput = inputWrapper(scene.optionText + " - (" + optionText[:-1] + ") --> ").lower()

    textAdventureFormatting.delay(1, 5)

    for option in scene.options:
        if option.name.lower() == playerInput:
            outputText = option.text
            if option.damage > 0:
                gameState.takeDamange(option.damage)
                if gameState.hp <= 0:
                    outputText = option.deathText
            
            gameState.lastRepeated = textAdventureFormatting.gamePrint(outputText.replace("%name%", gameState.name).replace("%weapon%", gameState.inventory["weapon"] if "weapon" in gameState.inventory else "Sword"), "#" if option.damage == 0 else "!", gameState.lastRepeated)
            gameState.scene = option.outcome
            loggingWrapper("Made choice: " + option.name.capitalize() + " and " + ("moving to scene #" + str(gameState.scene)))

            #scene specific actions
            if scene.sceneCode == 0:
                gameState.inventory["weapon"] = (option.name.lower().replace("excalibur", "knife").capitalize())
                loggingWrapper("Added: '" + option.name.capitalize() + "' to player inventory")

gameState = gameState("Sir Arthur", "easy")

def main():

    textAdventureFormatting.displayAscii("god.txt")

    gameState.lastRepeated = textAdventureFormatting.gamePrint("Welcome, Knight. You have been summoned to be part of King Arthur's Quest for the Holy Grail. Unfortunately, the animator has been sacked, and those reponsible for his sacking sacked, so all we have is this text and some storyboard images. What is thy name?", "@", gameState.lastRepeated)
    gameState.name = inputWrapper(" --> ")
    gameState.lastRepeated = textAdventureFormatting.gamePrint("Glad to see you arrived safely, " + gameState.name + ". What difficulty of journey do you fancy?", "$", gameState.lastRepeated)
    
    difficultyText = ""
    for diff in textAdventureSceneLoader.Difficulty:
        difficultyText += diff.name.lower().capitalize() + " "

    difficultyInput = inputWrapper("(" + difficultyText[:-1] + ") --> ").lower()
    if difficultyInput.upper() in textAdventureSceneLoader.Difficulty.__members__:
        gameState.lastRepeated = textAdventureFormatting.gamePrint("The difficulty has been adjusted accordingly, sire.", "$", gameState.lastRepeated)
        gameState.hp = textAdventureSceneLoader.Difficulty[difficultyInput.upper()].value
    else:
        gameState.lastRepeated = textAdventureFormatting.gamePrint("Since it seems you cannot even pick between 3 clear options easily, we'll set the difficulty to easy for you, sire.", "!", gameState.lastRepeated)

    loggingWrapper("Game initialized with name: " + gameState.name + " and difficulty lives at: " + str(gameState.hp))
    textAdventureFormatting.delay(1, 1)
    inputWrapper("Hit \"Enter\" to continue... ")
    textAdventureFormatting.delay(1, 15)

    while gameState.hp > 0:
        doTurn()
        inputWrapper("Hit \"Enter\" to continue... ")
        textAdventureFormatting.delay(1, 15)

        if getCurrentScene(gameState.scene).area == "ending":
            break

    textAdventureFormatting.delay(1, 15)

    if gameState.hp <= 0:
        gameState.lastRepeated = textAdventureFormatting.gamePrint("You have succumed to your physical and/or mental wounds. Restart to try again - maybe on an eaiser difficulty", "%", gameState.lastRepeated)
    else:
        scene = getCurrentScene(gameState.scene)
        if(scene.asciiFile):
            gameState.lastRepeated = textAdventureFormatting.displayAscii(scene.asciiFile)

        for text in scene.preText:
            gameState.lastRepeated = textAdventureFormatting.gamePrint(text, "*", gameState.lastRepeated)
    
    textAdventureFormatting.delay(10, 5)
    loggingWrapper("Game " + gameState.name + " finished with " + str(gameState.hp) + " HP left on scene: " + str(gameState.scene))


if __name__ == "__main__":
    main()