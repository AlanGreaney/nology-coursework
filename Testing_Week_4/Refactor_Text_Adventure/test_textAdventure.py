import os
import time
import pytest

import textAdventureSceneLoader
import textAdventureFormatting
import textAdventureMain


@pytest.mark.parametrize("inputs, expected_output", [
    #(input text, character), (number of lines, number of characters)
    (("test", "*"), (5, 755)),
    (("A slightly longer line of text", "$"), (5, 755)),
    (("Just enough text to make a second line. Just enough text to make a second line. Just enough text to make a second line. Just enough text to make a second line. Just enough text to make a second line. ", "!"), (6, 906)),
    (("The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).", "*"), (8, 1208)),
]) 
def test_string_formatting(capfd, inputs, expected_output):

    textAdventureFormatting.gamePrint(inputs[0], inputs[1])
    out, err = capfd.readouterr() #reads the stdout

    assert len(out.splitlines()) == expected_output[0] #check the number of lines in the output
    assert len(out) == expected_output[1] #length of the outputted text
    assert out.count(inputs[1]) > 150 #expect a high number of out selected ring character


def test_ascii_formatting(capfd):
    textAdventureFormatting.displayAscii("bridge1.txt")
    out, err = capfd.readouterr() #reads the stdout

    assert len(out.splitlines()) == 34
    assert len(out) == 4984

    textAdventureFormatting.displayAscii("god.txt")
    out, err = capfd.readouterr() #reads the stdout

    assert len(out.splitlines()) == 35
    assert len(out) == 5135


def test_scene_loader():
    mpScene = textAdventureSceneLoader.getScene("montyPython")

    assert len(mpScene) == 20
    assert len(mpScene[0].options) == 5

    assert mpScene[1].area == "Outlying Lands"
    assert mpScene[2].sceneCode == 2
    assert mpScene[3].optionText == "Which bodypart do you aim for?"
    assert mpScene[4].preText == ["The Black Knight is standing still, barely concious. it would be easy to take him out at this point. However, you feel sorry for the Knight and his tiny bridge, and feel you must take pity on him, and not inflict a mortal wound."]
    assert mpScene[5].asciiFile == "blackKnight.txt"

    assert mpScene[6].options[0].name == "Head"
    assert len(mpScene[6].options[0].text) == 488
    assert mpScene[6].options[0].outcome == 5
    assert mpScene[6].options[0].damage == 1
    assert len(mpScene[6].options[0].deathText) == 456
    assert "big metal helmet" in mpScene[6].options[0].deathText 


def test_difficulty():
    assert textAdventureSceneLoader.Difficulty["EASY"].value == 5
    assert textAdventureSceneLoader.Difficulty["MEDIUM"].value == 3
    assert textAdventureSceneLoader.Difficulty["HARD"].value == 1


def test_game_state():
    testGameState = textAdventureMain.gameStateClass("Sir Test", "medium")

    assert testGameState.scene == 0
    assert testGameState.lastRepeated == ""
    assert testGameState.name == "Sir Test"
    assert testGameState.hp == textAdventureSceneLoader.Difficulty["MEDIUM"].value
    testGameState.takeDamange(1)
    assert testGameState.hp == textAdventureSceneLoader.Difficulty["MEDIUM"].value - 1


def test_main_game_scene():
    sceneNum = 5
    testScene = textAdventureMain.getCurrentScene(sceneNum)

    assert testScene.area == "plains_rt2"
    assert testScene.sceneCode == sceneNum
    assert len(testScene.options) == 3


#https://docs.pytest.org/en/latest/how-to/monkeypatch.html
def test_turn_take(monkeypatch, capfd):
    currentScene = textAdventureMain.getCurrentScene(textAdventureMain.gameState.scene)

    assert currentScene.area == "Armory"
    assert currentScene.sceneCode == 0
    assert len(currentScene.options) == 5

    #automatically inputs "Sword" to user input
    #note: if wanted to use multiple inputs: https://pavolkutaj.medium.com/simulating-single-and-multiple-inputs-using-pytest-and-monkeypatch-6968274f7eb9
    #inputs = iter(['input1', 'input2'])
    monkeypatch.setattr('builtins.input', lambda _: "Sword") 
    textAdventureMain.doTurn() #main "turn taking" function
    out, err = capfd.readouterr()

    nextScene = textAdventureMain.getCurrentScene(textAdventureMain.gameState.scene)
    
    #ensure we have moved to the next scene
    assert nextScene.area == "Outlying Lands"
    assert nextScene.sceneCode == 1
    assert len(nextScene.options) == 3

    #ensure the output for option "sword" was shown in the prints
    assert "The classic melee weapon" in out



def test_logs():
    #methodology:
    #1. check both log files exist
    #2. append a test log with a unique timestamp identifier via the logging method
    #3. read the files to ensure it was properly added
    logfile1 = "./logger.log"
    logfile2 = "./logger.csv"

    assert os.path.exists(logfile1)
    assert os.path.exists(logfile2)

    testText = "Testing Log @ " + str(time.time())
    textAdventureMain.loggingWrapper(testText)

    with open(logfile1, encoding="utf-8") as fileObj:
        for line in fileObj:
            pass
        last_line = line

        assert testText in last_line


    with open(logfile2, encoding="utf-8") as fileObj:
        for line in fileObj:
            pass
        last_line = line

        assert testText in last_line
