import os
from enum import Enum

class Difficulty(Enum):
    EASY = 5
    MEDIUM = 3
    HARD = 1

class option:
    def __init__(self, name, text, outcome, damage = 0, deathText = ""):
        self.name = name #for player selecting and logging
        self.text = text #whats shown when this option selected
        self.outcome = outcome #the next scene to go to if this option is selected
        self.damage = damage #how much damage they take if picking this option
        self.deathText = deathText #the text to show instead if they die to this option
        #self.hidden = False #unused currently, but could allow for hidden options

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

class scene:
    def __init__(self, area, sceneCode, optionText, preText, options, asciiFile = False):
        self.area = area #only for logging purposes
        self.sceneCode = sceneCode
        self.optionText = optionText #what they see next to input prompt
        self.preText = preText #what shows before the option input
        self.options = options #available options and their outcomes
        self.asciiFile = asciiFile #ascii file to show, if any

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

def loadMontyPython():
    gameScenesMontyPython = []

    gameScenesMontyPython.append(scene("Armory", 0, "What will you take?",
                        #filler text
                        ["Before setting out on your journey, it would be wise to pick a weapon. In the Castle's Armory there are Swords, Bows, Spears, Maces, and Axes available to choose. Which weapon suits you best?", ], 
                        #options
                        [option("Sword", "A fine choice. The classic melee weapon, versatile in all situations.", 1), 
                        option("Bow&Arrow", "A questionable choice for such a small party, you will not have much protection.", 1), 
                        option("Mace", "A Mace - Slower but more punishing when a hit does land.", 1),
                        option("Spear", "A better choice than most realize - the spear allows for short and long range (if your arm is trained to throw, at least)", 1),
                        option("Excalibur", "You remember the legend of Excalibur, the Sword stuck in the rock, the only one able to pull \
                        it out said to be worthy of becoming King. You make your way into the courtyard to attempt pulling it out. \
                        Try as you might, your pulls prove fruitless - in fact, it seems the sword retracts deeper into the rock with every touch\
                        Suddnely, you lose your grip and fall back, hitting your head on the rock as you fall. Dazed and confused for some time, \
                        the party hands you a small knife before setting off, thinking that is all you can handle.", 1, 1, "You remember the legend of Excalibur, the Sword stuck in the rock, the only one able to pull \
                        it out said to be worthy of becoming King. You make your way into the courtyard to attempt pulling it out. \
                        Try as you might, your pulls prove fruitless - in fact, it seems the sword retracts deeper into the rock with every touch\
                        Suddnely, you lose your grip and fall back, hitting your head on the rock as you fall. Your skull knocked open by the violent fall, the party \
                        leaves you for the dead-cart in the middle of the courtyard.")],
                        "sword.txt"))

    gameScenesMontyPython.append(scene("Outlying Lands", 1, "Which direction do you go?",
                        #filler text
                        ["It's time for the party to set off - the band of 12 men ask for your input on where to go. You can choose to not answer, or think over the two immediate choices:", 
                        "The Plains. Filled with commoners and other castles, both of whom may dislike your group. However, food is plentiful, and safe rest available most every night.", 
                        "The forest - unknown creatures, vagabonds, and other parties of adventureres may roam these dark lands."], 
                        #options
                        [option("Plains", "You suggest to stay in the open plains, where travel can be faster. The party agrees, and you set off.", 2), 
                        option("Forest", "You convince the party that venturing into the forest is worth the trouble it may cause - they cautiosly agree, and follow you in", 3), 
                        option("Abstain", "You stare blankly back at the party, saying nothing. The party conitnues to try and elecit a response, \
                        but you sit there silently like your microphone is muted in a Zoom call. King Arthur smacks you upside the head, \
                        and you fall over leaning torwards the plains - the party decides to go that way.", 2, 1, "You stare blankly back at the party, saying nothing. The party conitnues to try and elecit a response, \
                        but you sit there silently like your microphone is muted in a Zoom call. King Arthur smacks you upside the head, \
                        and you collapse to the ground, smacking your head on a rock. The party leaves your body as it lays, as they head off to the plains.")],
                        "fork.txt"))

    gameScenesMontyPython.append(scene("plains_rt1", 2, "How do you insult the Frenchman?",
                        #filler text
                        ["Venturing into the plains, you and your party safely pass through multiple small villages, assisting in witch hunts and requestitioning some bread from the locals.", 
                        "Eventually, you come across a castle that blocks the way. For some reason, a French Guard is at the gate. He sneers, \"ah, you English types-a!\" in a silly accent. \"I blow my nose at you, \
                        so-called Arthur King and " + "%name%" + ", and all your silly English k-nnnnniggets.\"",
                        "In order to get through, you'll need to insult the Frenchman back."], 
                        #options
                        [option("Quest", "Instead of trying to stoop to the level of the Frenchman's insults, you instead try to reason with him. \"We are on a quest for the holy grail! A quest from god!\" you say. \
                        The Frenchman replies - \"Well we've already got one. In fact, we've got many, you English Farts. Here, take one and go away\". Before you have time to react, an obviously fake but still quite large \
                        cup is hurled over the wall directly at you, smashing into your skull and knocking you onto the ground, where you hit your head on a rock. While unconcious, the french continue to mock your presence. \
                        Luckily, the rest of the party has constructed a large wooden cow, which they use to sneak around the castle blocking the way later in the day.", 6, 1, "Instead of trying to stoop to the level of the Frenchman's insults, you instead try to reason with him. \"We are on a quest for the holy grail! A quest from god!\" you say. \
                        The Frenchman replies - \"Well we've already got one. In fact, we've got many, you English Farts. Here, take one and go away\". Before you have time to react, an obviously fake but still quite large \
                        cup is hurled over the wall directly at you, smashing into your skull and knocking you onto the ground, where you hit your head on a rock. The fall kills you instantly, and the rest of the party runs away, and worst of all, \
                        the French squad in the castle now has a nice dinner of beef, using the cow they were planning to launch torwards you via catapult."), 
                        option("French", "You attempt to make fun of everything you can think of about the Frenchman. The accent, the lands, their smell - and none of it affects the Frenchman. \
                        \"I don't wanna talk to you no more, you empty headed animal food trough wiper!\" - The gaurds get so bored of your lame insults that they retreat inside, leaving time for you and the party to sneak around the outsite of the castle instead.", 6), 
                        option("Mother", "You attempt your best your mom jokes, but the Frenchman one-ups each one. His final best, \"Your mother was a hamster and your father smelt of elderberries!\" \
                        sends the guard into such a fit of laughter that you and the rest of the party make haste through the center of the courtyard and past the castle before the garrison.", 6)],
                        "french.txt"))

    gameScenesMontyPython.append(scene("blackKnight1_rt2", 3, "Which bodypart do you aim for?",
                        #filler text
                        ["Venturing into the forest, you soon come across a bridge over a tiny river, nay, but a stream. However, a Knight dressed in all black blocks the way", 
                        "\"Halt. You must battle me to cross the river\" - Knight. \"Well, it's really just a stream, good sir. If it bothers you that much for us to make use of your bridge, we can just go around\". \"IMPOSSIBLE! You MUST cross the bridge\
                        to get through these woods, and for that, we must duel!\"", 
                        "The knight charges you, sword drawn, but looks to be of bad stance and atheleticsm. Where will you attempt to strike him?"], 
                        #options
                        [option("Head", "As the Black Knight rapidly approaches, you smash your " + "%weapon%" + " into the knight's head, dazing him. Upon doing this though, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. Luckily, you recover quickly from this fall while the Black Knight is still dazed and confused", 4.1, 1, "As the Black Knight rapidly approaches, you smash your " + "%weapon%" + " into the knight's head, dazing him. Upon doing this though, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. Your fall is more traumatic than the hit on the Black Knight, and the rest of the party eventually takes him out, but not before you succumb to the bleeding from your head"), 
                        option("Arm", "As the Black Knight rapidly approaches, you expertly slice off one of the Black Knights arm's as he charges past, taking no injury of your own.", 4.2), 
                        option("Leg", "As the Black Knight rapidly approaches, you expertly slice off one of the Black Knights legs's as he charges past, taking no injury of your own.", 4.3)],
                        "blackKnight.txt"))

    gameScenesMontyPython.append(scene("blackKnight2_head_rt2", 4.1, "Where do you target now?",
                        #filler text
                        ["The Black Knight is standing still, barely concious. it would be easy to take him out at this point. However, you feel sorry for the Knight and his tiny bridge, and feel you must take pity on him, and not inflict a mortal wound.", ], 
                        #options
                        [option("Head", "You rush the Knight and foolishly you smash your " + "%weapon%" + " into the knight's head again, even though he was basically standing still, limbs free for the taking. Upon doing this, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. The Black Knight also collapses, for much longer than yourself.", 5, 1, "You rush the Knight and foolishly you smash your " + "%weapon%" + " into the knight's head again, even though he was basically standing still, limbs free for the taking. Upon doing this, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. The Black Knight collapses, but so do you, seemingly for good, as the party leave you as a warning for those who dare fight over the tiny bridge."), 
                        option("Arm", "Just as the Black Knight seems to be recovering, you rush him and slice off both his arms in his confused state. \"Aye, have at ye! It's just a flesh wound\" explains the armless knight. He meekly attempts to kick you, \
                        but a quick kick back knocks him over, and he is unable to get up quickly before you and the rest of the party are able to cross his tiny bridge and continue upon your quest, though calls of being a coward continue to come from the Black Knight for some time.", 5), 
                        option("Leg", "Just as the Black Knight seems to be recovering, you rush him and slice off both his legs in his confused state. \"Aye, have at ye! It's just a flesh wound\" explains the legless knight. He meekly attempts to hop torwards you, \
                        but the entire party is easily able to outpace him over his own bridge, and you conintue upon your quest, despite the calls of being a coward that continue to come from the leglesss Black Knight in the distance.", 5)],
                        "blackKnight.txt"))

    gameScenesMontyPython.append(scene("blackKnight2_arm_rt2", 4.2, "Where do you strike?",
                        #filler text
                        ["Now one armed, the Black Knight seems quite keen to continue fighting, and charges you again, with cries of \"Tis only a flesh wound! Continue!\""], 
                        #options
                        [option("Head", "As the Black Knight rapidly approaches, you smash your " + "%weapon%" + " into the knight's head, dazing him. Upon doing this though, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. Luckily, you recover quickly from this fall while the Black Knight is still dazed and confused, and the \
                        rest of the party is able to cross the small bridge and conintue the quest.", 5, 1, "As the Black Knight rapidly approaches, you smash your " + "%weapon%" + " into the knight's head, dazing him. Upon doing this though, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. Your fall is more traumatic than the hit on the Black Knight, and the rest of the party eventually takes him out, but not before you succumb to the bleeding from your head"), 
                        option("Arm", "Just as the Black Knight seems to be recovering, you rush him and slice off his other arm in his weakend state. \"Aye, have at ye! It's just a flesh wound\" explains the armless knight. He meekly attempts to kick you, \
                        but a quick kick back knocks him over, and he is unable to get up quickly before you and the rest of the party are able to cross his tiny bridge and continue upon your quest, though calls of being a coward continue to come from the Black Knight for some time.", 5), 
                        option("Leg", "Just as the Black Knight seems to be recovering, you rush him and slice off his leg in his weakend state. \"Aye, have at ye! It's just a flesh wound\" explains the half-limbed knight. He meekly attempts to hop torwards you, \
                        but the entire party is easily able to outpace him over his own bridge, and you conintue upon your quest, despite the calls of being a coward that continue to come from the Black Knight in the distance.", 5)],
                        "blackKnight.txt"))

    gameScenesMontyPython.append(scene("blackKnight2_leg_rt2", 4.3, "Where do you strike?",
                        #filler text
                        ["Now one legged, the Black Knight seems quite keen to continue fighting as he hops torwards you, with cries of \"Tis only a flesh wound! Continue!\""], 
                        #options
                        [option("Head", "As the Black Knight rapidly approaches, you smash your " + "%weapon%" + " into the knight's head, dazing him. Upon doing this though, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. Luckily, you recover quickly from this fall while the Black Knight is still dazed and confused, and the \
                        rest of the party is able to cross the small bridge and conintue the quest.", 5, 1, "As the Black Knight rapidly approaches, you smash your " + "%weapon%" + " into the knight's head, dazing him. Upon doing this though, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. Your fall is more traumatic than the hit on the Black Knight, and the rest of the party eventually takes him out, but not before you succumb to the bleeding from your head"), 
                        option("Arm", "Just as the Black Knight seems to be recovering, you rush him and slice off his arm in his weakend state. \"Aye, have at ye! It's just a flesh wound\" explains the half-limbed knight. He meekly attempts to kick you, \
                        but a quick kick back knocks him over, and he is unable to get up quickly before you and the rest of the party are able to cross his tiny bridge and continue upon your quest, though calls of being a \
                        coward continue to come from the Black Knight for some time.", 5), 
                        option("Leg", "Just as the Black Knight seems to be recovering, you rush him and slice off his other leg in his weakend state. \"Aye, have at ye! It's just a flesh wound\" explains the leglesss knight. He meekly attempts to hop torwards you, \
                        but the entire party is easily able to outpace him over his own bridge, and you conintue upon your quest, despite the calls of being a coward that continue to come from the leglesss Black Knight in the distance. You also take a Red Herring from \
                        the knight's food stores - he shan't need them much longer", 5)],
                        "blackKnight.txt"))

    gameScenesMontyPython.append(scene("plains_rt2", 5, "How do you insult the Frenchman?",
                        #filler text
                        ["Emerging from the forest into the plains, you and your party safely pass through multiple small villages, assisting in witch hunts and requestitioning some bread from the locals.", 
                        "Eventually, you come across a castle that blocks the way. For some reason, a French Guard is at the gate. He sneers, \"ah, you English types-a!\" in a silly accent. \"I blow my nose at you, \
                        so-called Arthur King and " + "%name%" + ", and all your silly English k-nnnnniggets.\"",
                        "In order to get through, you'll need to insult the Frenchman back."], 
                        #options
                        [option("Quest", "Instead of trying to stoop to the level of the Frenchman's insults, you instead try to reason with him. \"We are on a quest for the holy grail! A quest from god!\" you say. \
                        The Frenchman replies - \"Well we've already got one. In fact, we've got many, you English Farts. Here, take one and go away\". Before you have time to react, an obviously fake but still quite large \
                        cup is hurled over the wall directly at you, smashing into your skull and knocking you onto the ground, where you hit your head on a rock. While unconcious, the french continue to mock your presence. \
                        Luckily, the rest of the party has constructed a large wooden cow, which they use to sneak around the castle blocking the way later in the day.", 8, 1, "Instead of trying to stoop to the level of the Frenchman's insults, you instead try to reason with him. \"We are on a quest for the holy grail! A quest from god!\" you say. \
                        The Frenchman replies - \"Well we've already got one. In fact, we've got many, you English Farts. Here, take one and go away\". Before you have time to react, an obviously fake but still quite large \
                        cup is hurled over the wall directly at you, smashing into your skull and knocking you onto the ground, where you hit your head on a rock. The fall kills you instantly, and the rest of the party runs away, and worst of all, \
                        the French squad in the castle now has a nice dinner of beef, using the cow they were planning to launch torwards you via catapult."), 
                        option("French", "You attempt to make fun of everything you can think of about the Frenchman. The accent, the lands, their smell - and none of it affects the Frenchman. \
                        \"I don't wanna talk to you no more, you empty headed animal food trough wiper!\" - The gaurds get so bored of your lame insults that they retreat inside, leaving time for you and the party to sneak around the outsite of the castle instead.", 8), 
                        option("Mother", "You attempt your best your mom jokes, but the Frenchman one-ups each one. His final best, \"Your mother was a hamster and your father smelt of elderberries!\" \
                        sends the guard into such a fit of laughter that you and the rest of the party make haste through the center of the courtyard and past the castle before the garrison.", 8)],
                        "french.txt"))

    gameScenesMontyPython.append(scene("blackKnight1_rt1", 6, "Which bodypart do you aim for?",
                        #filler text
                        ["Venturing into the forest, you soon come across a bridge over a tiny river, nay, but a stream. However, a Knight dressed in all black blocks the way", 
                        "\"Halt. You must battle me to cross the river\" - Knight. \"Well, it's really just a stream, good sir. If it bothers you that much for us to make use of your bridge, we can just go around\". \"IMPOSSIBLE! You MUST cross the bridge\
                        to get through these woods, and for that, we must duel!\"", 
                        "The knight charges you, sword drawn, but looks to be of bad stance and atheleticsm. Where will you attempt to strike him?"], 
                        #options
                        [option("Head", "As the Black Knight rapidly approaches, you smash your " + "%weapon%" + " into the knight's head, dazing him. Upon doing this though, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. Luckily, you recover quickly from this fall while the Black Knight is still dazed and confused", 7.1, 1, "As the Black Knight rapidly approaches, you smash your " + "%weapon%" + " into the knight's head, dazing him. Upon doing this though, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. Your fall is more traumatic than the hit on the Black Knight, and the rest of the party eventually takes him out, but not before you succumb to the bleeding from your head"), 
                        option("Arm", "As the Black Knight rapidly approaches, you expertly slice off one of the Black Knights arm's as he charges past, taking no injury of your own.", 7.2), 
                        option("Leg", "As the Black Knight rapidly approaches, you expertly slice off one of the Black Knights legs's as he charges past, taking no injury of your own.", 7.3)],
                        "blackKnight.txt"))

    gameScenesMontyPython.append(scene("blackKnight2_head_rt1", 7.1, "Where do you target now?",
                        #filler text
                        ["The Black Knight is standing still, barely concious. it would be easy to take him out at this point. However, you feel sorry for the Knight and his tiny bridge, and feel you must take pity on him, and not inflict a mortal wound.", ], 
                        #options
                        [option("Head", "You rush the Knight and foolishly you smash your " + "%weapon%" + " into the knight's head again, even though he was basically standing still, limbs free for the taking. Upon doing this, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. The Black Knight also collapses, for much longer than yourself.", 8, 1, "You rush the Knight and foolishly you smash your " + "%weapon%" + " into the knight's head again, even though he was basically standing still, limbs free for the taking. Upon doing this, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. The Black Knight collapses, but so do you, seemingly for good, as the party leave you as a warning for those who dare fight over the tiny bridge."), 
                        option("Arm", "Just as the Black Knight seems to be recovering, you rush him and slice off both his arms in his confused state. \"Aye, have at ye! It's just a flesh wound\" explains the armless knight. He meekly attempts to kick you, \
                        but a quick kick back knocks him over, and he is unable to get up quickly before you and the rest of the party are able to cross his tiny bridge and continue upon your quest, though calls of being a \
                        coward continue to come from the Black Knight for some time.", 8), 
                        option("Leg", "Just as the Black Knight seems to be recovering, you rush him and slice off both his legs in his confused state. \"Aye, have at ye! It's just a flesh wound\" explains the legless knight. He meekly attempts to hop torwards you, \
                        but the entire party is easily able to outpace him over his own bridge, and you conintue upon your quest, despite the calls of being a coward that continue to come from the leglesss Black Knight in the distance.", 8)],
                        "blackKnight.txt"))

    gameScenesMontyPython.append(scene("blackKnight2_arm_rt1", 7.2, "Where do you strike?",
                        #filler text
                        ["Now one armed, the Black Knight seems quite keen to continue fighting, and charges you again, with cries of \"Tis only a flesh wound! Continue!\""], 
                        #options
                        [option("Head", "As the Black Knight rapidly approaches, you smash your " + "%weapon%" + " into the knight's head, dazing him. Upon doing this though, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. Luckily, you recover quickly from this fall while the Black Knight is still dazed and confused, and the \
                        rest of the party is able to cross the small bridge and conintue the quest.", 8, 1, "As the Black Knight rapidly approaches, you smash your " + "%weapon%" + " into the knight's head, dazing him. Upon doing this though, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. Your fall is more traumatic than the hit on the Black Knight, and the rest of the party eventually takes him out, but not before you succumb to the bleeding from your head"), 
                        option("Arm", "Just as the Black Knight seems to be recovering, you rush him and slice off his other arm in his weakend state. \"Aye, have at ye! It's just a flesh wound\" explains the armless knight. He meekly attempts to kick you, \
                        but a quick kick back knocks him over, and he is unable to get up quickly before you and the rest of the party are able to cross his tiny bridge and continue upon your quest, though calls of being a \
                        coward continue to come from the Black Knight for some time.", 8), 
                        option("Leg", "Just as the Black Knight seems to be recovering, you rush him and slice off his leg in his weakend state. \"Aye, have at ye! It's just a flesh wound\" explains the half-limbed knight. He meekly attempts to hop torwards you, \
                        but the entire party is easily able to outpace him over his own bridge, and you conintue upon your quest, despite the calls of being a coward that continue to come from the Black Knight in the distance. You also take a Red Herring from \
                        the knight's food stores - he shan't need them much longer", 8)],
                        "blackKnight.txt"))

    gameScenesMontyPython.append(scene("blackKnight2_leg_rt1", 7.3, "Where do you strike?",
                        #filler text
                        ["Now one legged, the Black Knight seems quite keen to continue fighting as he hops torwards you, with cries of \"Tis only a flesh wound! Continue!\""], 
                        #options
                        [option("Head", "As the Black Knight rapidly approaches, you smash your " + "%weapon%" + " into the knight's head, dazing him. Upon doing this though, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. Luckily, you recover quickly from this fall while the Black Knight is still dazed and confused, and the \
                        rest of the party is able to cross the small bridge and conintue the quest.", 8, 1, "As the Black Knight rapidly approaches, you smash your " + "%weapon%" + " into the knight's head, dazing him. Upon doing this though, the force of hitting the Knight's big metal helmet sends you flying back, \
                        and you collapse onto the ground, hitting your head on a rock. Your fall is more traumatic than the hit on the Black Knight, and the rest of the party eventually takes him out, but not before you succumb to the bleeding from your head"), 
                        option("Arm", "Just as the Black Knight seems to be recovering, you rush him and slice off his arm in his weakend state. \"Aye, have at ye! It's just a flesh wound\" explains the half-limbed knight. He meekly attempts to kick you, \
                        but a quick kick back knocks him over, and he is unable to get up quickly before you and the rest of the party are able to cross his tiny bridge and continue upon your quest, though calls of being a \
                        coward continue to come from the Black Knight for some time.", 8), 
                        option("Leg", "Just as the Black Knight seems to be recovering, you rush him and slice off his other leg in his weakend state. \"Aye, have at ye! It's just a flesh wound\" explains the leglesss knight. He meekly attempts to hop torwards you, \
                        but the entire party is easily able to outpace him over his own bridge, and you conintue upon your quest, despite the calls of being a coward that continue to come from the leglesss Black Knight in the distance.", 8)],
                        "blackKnight.txt"))

    gameScenesMontyPython.append(scene("swamp1", 8, "What do you bring to the Knights who say Ni?",
                        #filler text
                        ["Past the Forest and Plains, a great Swampland lays before you. Just after entering, what seems like a mass made of up twigs, leaves, a garden gnome, and some old armor pieces appears before you. You then notice more of the same appearing in the distance", 
                        "\"We are the Knights who say 'Ni'\"", 
                        "It is oddly irritating when the being says these words, and it sure would be annoying if they were some kind of group who repeatedly say 'Ni' over and over in some sort of repetitive tendency. Between \
                        their bouts of reciting the evil phrase, they demand a sacrifice from your party. You all begin to eye whom you begin to think is the weakest member, before they elaborate:",
                        "\"We woud like a shrubbery. A nice one, not too expensive, but \
                        would generally impress a vistor\". Will you return to the previous town to shop for a shrubbery for the Knight Who Say Ni Repeatedly, or take another action?"], 
                        #options
                        [option("Shrubbery", "The party returns to the last town to shop for a shrubbery. You also get some nice new shows and a haircut while out.", 9.1), 
                        option("Battle", "Instead of bending to the whim of these odd knights, you attempt to fight them - using your " + "%weapon%" + " to attack the leader. You get one hit in, but they cry out \"Ni!\" in such a shrieking tone, and \
                        repatedly at that, that you collapse to the ground in pain, hitting your head on a rock. The party, still standing but weakened, drag you away into town to go shopping. You do not buy new shoes while out, \
                        as they were sold out.", 9.2, 1, "Instead of bending to the whim of these odd knights, you attempt to fight them - using your " + "%weapon%" + " to attack the leader. You get one hit in, but they cry out \"Ni!\" in such a shrieking tone, and \
                        repatedly at that, that you collapse to the ground in pain, hitting your head on a rock. The party, still standing but weakened, drag you away into town to go shopping, but you bleed out and are placed onto the dead cart before you can \
                        even see if they have any shoes in stock."), 
                        option("Fish", "Thinking quick, you remember that you caught a nice fish earlier that week, and maybe these Knights Who Say Ni won't know the difference between a fish and a shrubbery. To your dismay, as it's presented, they explain \
                        \"That's no shrubbery, that's a fish! ... wait, a Herring. You aren't supposed to mention a Herring until scene 9 when we become the Knights Who Say 'Ecky-ecky-ecky-ecky-pikang-zoop-boing-goodem-zu-owly-zhiv'. Well, no matter, \
                        you can skip a chapter and go ahead.", 10)],
                        "ni.txt"))

    gameScenesMontyPython.append(scene("swamp2_shopped", 9.1, "What do you do?",
                        #filler text
                        ["After much heated debate, you return with what the party believes to be a suitable shrubbery. Upon presenting it to the leader of the Knights who say Ni, he replies \"I'm sure the Knights who say Ni would have loved it, but \
                        we are no longer the Knights who say Ni, but instead say 'Ecky-ecky-ecky-ecky-pikang-zoop-boing-goodem-zu-owly-zhiv', and thus must give you a new test!\"", 
                        "\"This is ridiculous!\", explains King Arthur", 
                        "\"Ni!, I mean, eecky-ecky-ecky-pizang-bong oh whatever just shutup and find us another shrubbery. Slightly bigger, so that it makes a nice two-level effect.\""], 
                        #options
                        [option("Shopping", "You and the party return yet again to town to shop for another, slightly larger shrubbery. Fortunately, the Knights who say 'Ecky-ecky-ecky-ecky-pikang-zoop-boing-goodem-zu-owly-zhiv' were satisfied, and let you pass. \
                        Unfortunately, you had to sell your nice new shoes you had just bought to afford it.", 10), 
                        option("Battle", "Instead of bending to the whim of these odd knights again, you attempt to fight them - using your " + "%weapon%" + " to attack the leader. You get one hit in, but they cry out 'Ecky-ecky-ecky-ecky-pikang-zoop-boing-goodem-zu-owly-zhiv' in such a shrieking tone, and \
                        repatedly at that, that you collapse to the ground in pain, hitting your head on a rock. The party, still standing but weakened, drag you away into town to go shopping. You do not buy new shoes while out, \
                        as they were sold out, but the party does satisfy the Knights of the Swamp and are able to continue on.", 10, 1, "Instead of bending to the whim of these odd knights, you attempt to fight them - using your " + "%weapon%" + " to attack the leader. You get one hit in, but they cry out \"Ni!\" in such a shrieking tone, and \
                        repatedly at that, that you collapse to the ground in pain, hitting your head on a rock. The party, still standing but weakened, drag you away into town to go shopping, but you bleed out and are placed onto the dead cart before you can \
                        even see if they have any shoes in stock."), 
                        option("Shoes", "You instead try to barter your shoes to the Knights - \"Check out these fresh kicks, would you take them instead? I still have my old shoes, so I can part with these, the old ones just got real muddy while I was fishing. I didn't \
                        even catch anything, but did get a Herring fr--\" \"AHHH!\", Shrieks the Knight!, \"Not that word, don't say it!\" \"What did I say, shoes? fish?\" \"...\" \"Herrin-\" \"AHHH! DON'T SAY IT! WE'LL LET YOU THROUGH, JUST STOP SPEAKING\"", 10)],
                        "ni.txt"))      

    gameScenesMontyPython.append(scene("swamp2_fought", 9.2, "What will you take?",
                        #filler text
                        ["After much heated debate, without any of your input, the party returns with what they believe to be a suitable shrubbery. Upon presenting it to the leader of the Knights who say Ni, he replies \"I'm sure the Knights who say Ni would have loved it, but \
                        we are no longer the Knights who say Ni, but instead say 'Ecky-ecky-ecky-ecky-pikang-zoop-boing-goodem-zu-owly-zhiv', and thus must give you a new test!\"", 
                        "\"This is ridiculous!\", explains King Arthur", 
                        "\"Ni!, I mean, eecky-ecky-ecky-pizang-bong oh whatever just shutup and find us another shrubbery. Slightly bigger, so that it makes a nice two-level effect.\""], 
                        #options
                        [option("Shopping", "You and the party return yet again to town to shop for another, slightly larger shrubbery. Fortunately, the Knights who say 'Ecky-ecky-ecky-ecky-pikang-zoop-boing-goodem-zu-owly-zhiv' were satisfied, and let you pass. \
                        Unfortunately, you had to sell your shoes to afford it.", 10), 
                        option("Battle", "Still refusing to bend to the whim of these odd knights, you again attempt to fight them - using your " + "%weapon%" + " to attack the leader. You get one hit in, but they cry out 'Ecky-ecky-ecky-ecky-pikang-zoop-boing-goodem-zu-owly-zhiv' in such a shrieking tone, and \
                        repatedly at that, that you collapse to the ground in pain, hitting your head on a rock. The party, still standing but weakened, drag you away into town to go shopping. You do not buy new shoes while out, \
                        as they were sold out, but the party does satisfy the Knights of the Swamp and are able to continue on.", 10, 1, "Still refusing to bend to the whim of these odd knights, you again attempt to fight them - using your " + "%weapon%" + " to attack the leader. You get one hit in, but they cry out \"Ni!\" in such a shrieking tone, and \
                        repatedly at that, that you collapse to the ground in pain, hitting your head on a rock. The party, still standing but weakened, drag you away into town to go shopping, but you bleed out and are placed onto the dead cart before you can \
                        even see if they have any shoes in stock."), 
                        option("Shoes", "You instead try to barter your shoes to the Knights - \"Check out these fresh kicks, would you take them instead? I still have my old shoes, so I can part with these, the old ones just got real muddy while I was fishing. I didn't \
                        even catch anything, but did get a Herring fr--\" \"AHHH!\", Shrieks the Knight!, \"Not that word, don't say it!\" \"What did I say, shoes? fish?\" \"...\" \"Herrin-\" \"AHHH! DON'T SAY IT! WE'LL LET YOU THROUGH, JUST STOP SPEAKING\"", 10)],
                        "ni.txt"))    

    gameScenesMontyPython.append(scene("bridge1", 10, "How do you answer?",
                        #filler text
                        ["You feel as though you are nearing the end of the journey, as if only one or two final perils await you. The first, or maybe last, of these perils is a rickety old bridge. An old man stands, blocking the way.", 
                        "\"Answer my questions three, and pass may thee\", the old man says. You feel a sense of great magic from these man.", 
                        "He begins, \"WHAT is your name?\""], 
                        #options
                        [option("Truth", "My name is \"" + "%name%" + "\" you confidently reply. The old man nods, and begins to speak again...", 11), 
                        option("Lie", "My name is \"" + os.getlogin() + "\" you shakily reply. \"Well, that's not quite a true but not a lie either, is it?\" says the old man, as you both break the 4th wall. \"Yes\", you reply, \"and did that count \
                        as asking me a second question that I answered?\". \"Drat! Guess you get to skip a scene\" explains the old man.", 12), 
                        option("Fight", "You quicky rush the old man, and knock him over as you rush onto the rickety old bridge. As you make the halfway point, the old man is getting up and begins to cackle. Magical energy wells up around him and his staff - surely \
                        this is your end. Miraculously, as the old man takes a step to cast his spell, he trips over his extremely long beard and falls into the abyss, allowing you and the rest of the party to traverse the bridge safely.", 13)],
                        "bridge1.txt"))

    gameScenesMontyPython.append(scene("bridge2", 11, "How do you answer?",
                        #filler text
                        ["The second question, is THUS, answer wisely, o knight...", 
                        "\"What is your favorite colour?\""], 
                        #options
                        [option("Blue", "\"#6A5ACD\", you confidently, reply. \"The heck is #6A5ACD, I don't know that!\" the wizard exclaims, turning a shade of bright #FF5733, angry that he cannot dechiper your answer, as he seeks to gain knowledge...", 12), 
                        option("Red", "\"Red\", you say. \"Ok sure, wow, way to be basic\" replies the old man, as he moves on...", 12), 
                        option("Color", "you take too much HP damange for this text to show", 12, Difficulty["EASY"].value, "\"I don't have a favourite COLOUR, just a favorite COLOR\" you explain, before being suddenly thrown off the mountain to your death, as you hear \
                        the wizard explain as you fall, \"You were wrong for being so pedantic, it's the same thing! And you claim to not use coloUr but said favoUrite, should have made up your mind on whether this was a British or American company, err, I mean \
                        story!\" are the last words you hear."),
                        option("Unsure", "Truthfully but timidly, you answer \"unsure\" - and the wizard accepts this? \"That's totally a valid answer\", he explains, \"it's never nessecary to pick favorites, you are allowed to enjoy many things equally. Except \
                        children, you always have a favorite child, just never tell them that.\"", 12)],
                        "bridge1.txt"))

    gameScenesMontyPython.append(scene("bridge3", 12, "How do you answer?",
                        #filler text
                        ["The air is still with tension as the wizard asks his 3rd and final question:", 
                        "\"What... is the air-speed velocity of an unladen swallow?\""], 
                        #options
                        [option("Object", "you take too much HP damange for this text to show", 13, Difficulty["EASY"].value, "\"African or European Swallows?\" you cleverly think to ask, having seen the movie before, or at least heard Ben \
                        reference it 100 times before, before being thrown off the mountain,. As you fall to your doom, you hear the wizard exclaim \"OBVIOUSLY we established this is a story taking place in Medevial Europe! I wouldn't except you to know \
                        anything about Africa, that's not for another 175 years!\""), 
                        option("11mph", "Unfortunately, you have converted your units poorly, silly knight! You are thrown into the sky, over the giant canyon the bridge traverses. Luckily, you manage to land ON the bridge, though you hit your head \
                        on the rock that was placed in the middle of the bridge dedicated to the 3 people who died during its construction 64 years ago in a freak bird attack. Dazed but alive, you are able to continue across \
                        the bridge without the wizard realizing \
                        he needs to improve his aim.", 13, 1, "Unfortunately, you have converted your units poorly, silly knight! You are thrown into the sky, over the giant canyon the bridge traverses. Luckily, you manage to land ON the bridge, \
                        though you hit your head \
                        on the rock that was placed in the middle of the bridge dedicated to the 3 people who died during its construction 64 years ago in a freak bird attack. Dazed, your limp body rolls off the bridge and into the abyss below."), 
                        option("24mts", "Unfortunately, you have converted your units poorly, silly knight! You are thrown into the sky, over the giant canyon the bridge traverses. Luckily, you manage to land ON the bridge, though you hit your head \
                        on the rock that was placed in the middle of the bridge dedicated to the 3 people who died during its construction 64 years ago in a freak bird attack. Dazed but alive, you are able to continue across the bridge without the wizard realizing \
                        he needs to improve his aim.", 13, 1, "Unfortunately, you have converted your units poorly, silly knight! You are thrown into the sky, over the giant canyon the bridge traverses. Luckily, you manage to land ON the bridge, though you hit your head \
                        on the rock that was placed in the middle of the bridge dedicated to the 3 people who died during its construction 64 years ago in a freak bird attack. Dazed, your limp body rolls off the bridge and into the abyss below."), 
                        option("24mph", "\"Well... thats... right...\" says the wizard, wondering if the delay in your response was because you were googling the answer. Nonetheless, you pass and are able to continue on your journey.", 13), 
                        option("11mts", "\"Well... thats... right...\" says the wizard, wondering if the delay in your response was because you were googling the answer. Nonetheless, you pass and are able to continue on your journey.", 13)],
                        "bridge1.txt"))

    gameScenesMontyPython.append(scene("coast", 13, "How will you proceed?",
                        #filler text
                        ["As you approach the coast, the castle where the Holy Grail is alleged to be comes into view - The quest is nearly at an end! But wait, you recognize someone on the battlements...", 
                        "\"Allo, dappy English k-niggets and Monsieur Arthur King, who has the brain of a duck, you know. So, we French fellows outwit you a second time!\"", 
                        "Drat! That group of Frenchman has beat you to the castle."], 
                        #options
                        [option("Siege", "You begin to make camp around the castle to prepare for extended battle.", 14), 
                        option("Attack", "After a heroic camera pan across the field of combatants that we could not afford to animate, you and the rest of the party start running torwards the castle, weapons drawn!", 14), 
                        option("Retreat", "You instantly break rank to run back home, and the party flees too, thinking you had a better reason than just being a coward.", 14)],
                        "coast.txt"))

    gameScenesMontyPython.append(scene("ending", 14, "ending",
                        #filler text
                        ["Crikey, its the Rozzers! Before you had a chance to enact your plan, the constables showed up and arrested the whole party. They've been on your tail since you felled that Black Knight in the forest, helped with the witch trials, and that one [DLC Scene not purcahsed] back in the wetlands.", 
                        "It was a silly quest, anyways.",
                        "No French people were harmed in the making of this game. Not sure about the original movie, though."], 
                        #options
                        [],
                        "police.txt"))

    return gameScenesMontyPython


gameScenes = {}
gameScenes["montyPython"] = loadMontyPython()



def getScene(name):
    return gameScenes[name]

def main():
    print(len(gameScenes))
    print(gameScenes["montyPython"])

if __name__ == "__main__":
    main()