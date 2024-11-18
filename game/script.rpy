# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character. renpy.get_mouse_pos()

#attributions
#atmosphere.wav: 230109_2302_FR_KitchenAtmosphere.wav by kevp888 -- https://freesound.org/s/669154/ -- License: Attribution 4.0
#microwave.wav: microwave 03.wav by ShadowSilhouette -- https://freesound.org/s/489751/ -- License: Creative Commons 0
#leavehome.wav: FX SaSc Door 18 Old Wood Squeak Rattle Open Close 2 Versions Far.wav by Profispiesser -- https://freesound.org/s/583226/ -- License: Creative Commons 0
#trainarriving.wav: S-Bahn Berlin - Train arrives at station, waits, departs, perspective from the street below by Pfannkuchn -- https://freesound.org/s/560911/ -- License: Attribution 4.0
#office.wav: Office Ambience / Walla by sebearroyo -- https://freesound.org/s/483688/ -- License: Attribution 4.0
#platformnight.mp3: Interior City Apartment - Los Angeles on Ventura Blvd.wav by MJSoundDesign -- https://freesound.org/s/397889/ -- License: Creative Commons 0
#platformday.mp3: Railway Station Platform by mycompasstv -- https://freesound.org/s/474616/ -- License: Creative Commons 0
#apartment.mp3: room-tone apartment 622 PM 240215_0662 by klankbeeld -- https://freesound.org/s/736848/ -- License: Attribution 4.0
#closetcreak.wav: Door Creak by coosemek -- https://freesound.org/s/460542/ -- License: Attribution 3.0
#clothesrustle.wav: foley cloth rustle.wav by martian -- https://freesound.org/s/19291/ -- License: Creative Commons 0
#heartbeat.wav: Heartbeat, Regular, Single, 01-01, LOOP.wav by InspectorJ -- https://freesound.org/s/485076/ -- License: Attribution 4.0
#doorcreak.wav: Door_Creak_Short_01.wav by scholzi982 -- https://freesound.org/s/566174/ -- License: Attribution 3.0
#plastic.wav: Plastic-bag crackle by mboscolo -- https://freesound.org/s/212664/ -- License: Attribution 4.0
#kitchen.wav: 230109_2302_FR_KitchenAtmosphere.wav by kevp888 -- https://freesound.org/s/669154/ -- License: Attribution 4.0
#returnhome.wav: open door knob from outside, step in and close the door, lock the deadbolt by PostProdDog -- https://freesound.org/s/537821/ -- License: Creative Commons 0
#nightmarebreath.wav: Breath.ogg by egomassive -- https://freesound.org/s/536729/ -- License: Creative Commons 0
#trainride.wav: NYC Subway 4 by joliusnyren -- https://freesound.org/s/713917/ -- License: Creative Commons 0
#trainchime.wav: Prague Metro Line C Chime by chungus43A -- https://freesound.org/s/724060/ -- License: Creative Commons 0

init python:
    class Item:
        def __init__(self, name, cost):
            self.name = name
            self.cost = cost

    class Inventory:
        def __init__(self, money=10):
            self.money = money
            self.items = []

        def buy(self, item):
            if self.money >= item.cost:
                self.money -= item.cost
                self.items.append(item)
                return True
            else:
                return False

        def earn(self, amount):
            self.money += amount

        def has_item(self, item):
                if item in self.items:
                    return True
                else:
                    return False

#definitions

define gui.text_font = "Exo2.ttf"

define mc = Character("")
define mcs = Character("You", color="000000")
define d = Character("Diana", color="abcdef")
define k = Character("Kieth", color="063970")
define sm = Character("Stranger", color="F2F2F2")

define slowdissolve = Dissolve(1.0)
define blink = Fade(0.2, 0.0, 0.9)

define word_list = ["alligator", "blueberry", "957", "gooseberry", "illness", "basketball", "1395", "1296", "fifty-two"]

default outfit = ["none", "none", "none"]
default day = 1
#default workperformance = [0, 0, 0]
default workaverage = 0


default closet_sensitive = True
default bathroom_sensitive = True
default journal_sensitive = True

default keith_sensitive = True
default computer_sensitive = True

default textclicked = False

default tooltip_outfit_fun = "A favorite outfit of yours. You have to admit it looks pretty good on you."
default tooltip_outfit_stuffy = "Stuffy clothes, but very professional."
default tooltip_outfit_casual = "Loose pants, the hoodie you've had since your teen years... the epitome of comfort."

#define text_outfit_fun_list = ["You feel a little lighter in these clothes. A little more yourself.", "...Maybe these clothes attracted attention yesterday... You feel unsure."]

#inventory
#define date = ["January", "February"]
#$ date = ["January", "February"]

#python:
#   example_list = [0, 3, 2]
#   example_list.append(5)
#   example_list.append("string")

style pc_button_text is text:
    #outlines [ (absolute(3), "#ffffff", absolute(3), absolute(3)) ]
    size 45
    hover_color "#FF00FF"             # Pink
    outlines [ (0, "#0000FF", 1, 1) ] # Blue
    color "#FF0000"                   # Red


transform slightright:
    xalign 0.95
    yalign 1.0

screen bedroom_day_choices():
    vbox:
        imagebutton:    
            xpos 1208
            ypos 213
            idle "empty.png"
            hover "empty.png"
            activate_sound "closetcreak.wav"
            action Jump("closet_day" + str(day))
            tooltip "The closet."
        imagebutton:
            xpos 782
            ypos 172
            idle "empty.png"
            hover "empty.png"
            action NullAction()
            tooltip "Your journal... maybe after work."

        imagebutton:
            xpos 1600
            ypos -400
            idle "empty.png"
            hover "empty.png"
            activate_sound "doorcreak.wav"
            action Jump("kitchen_day" + str(day))
            tooltip "The door to the kitchen and the entrance."

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]"

screen closet_choices():
    vbox:
        imagebutton:
            xpos 0
            ypos 250
            idle "empty.png"
            hover "empty.png"
            action [SetDict(outfit, day, "fun"), Return]
            #tooltip "An outfit you quite like. You have to admit it looks pretty good on you."
            tooltip tooltip_outfit_fun

        imagebutton:
            xpos 390
            ypos -120
            idle "empty.png"
            hover "empty.png"
            action [SetDict(outfit, day, "stuffy"), Return]
            #tooltip "Stuffy clothes, but very professional."
            tooltip tooltip_outfit_stuffy

        imagebutton:
            xpos 800
            ypos -600
            idle "empty.png"
            hover "empty.png"
            action [SetDict(outfit, day, "casual"), Return]
            #tooltip "Loose pants, your favorite hoodie... the epitome of comfort."
            tooltip tooltip_outfit_casual

    $ tooltip = GetTooltip()

    if tooltip:
        text "[tooltip]"   

screen office_day_choices:
    vbox:
        imagebutton:
            xpos 200
            ypos 400
            idle "empty.png"
            hover "empty.png"
            action [Jump("keith_day" + str(day))]
            tooltip "Your coworker, Keith. He's playing some kind of game on his computer."

        imagebutton:
            xpos 800
            ypos -300
            idle "empty.png"
            hover "empty.png"
            action [Jump("bathroom_day" + str(day))]
            tooltip "The bathroom. Your favorite hiding place."

        imagebutton:
            xpos 1260
            ypos -700
            idle "empty.png"
            hover "empty.png"
            action NullAction()
            tooltip "The boss's office. You don't want to go in unless you have to."

        imagebutton:
            xpos 1560
            ypos -600
            idle "empty.png"
            hover "empty.png"
            action [Jump("computer_day" + str(day))]
            tooltip "Your cubicle, your computer... your work. A lot of work."

    $ tooltip = GetTooltip()

    if tooltip:
        text "[tooltip]"   

screen bedroom_night_choices():
    vbox:
        imagebutton:    
            xpos 400
            ypos 300
            idle "empty.png"
            hover "empty.png"
            action Jump("bed_night" + str(day))
            tooltip "Your bed..."

        imagebutton:
            xpos 782
            ypos 12
            idle "empty.png"
            hover "empty.png"
            action Jump("journal_night" + str(day))
            tooltip "Your journal."

        imagebutton:    
            xpos 1208
            ypos -600
            idle "empty.png"
            hover "empty.png"
            action Jump("closet_night" + str(day))
            tooltip "The closet."


        imagebutton:
            xpos 1600
            ypos -600
            idle "empty.png"
            hover "empty.png"
            action NullAction()
            tooltip "...You'd rather stay holed up in here for now."

    $ tooltip = GetTooltip()
    if tooltip:
        text "[tooltip]"

screen simple_screen():
    frame:
        xalign 0.5 ypos 50
        vbox:
            text "This is a screen."
            textbutton "Okay":
                action Return(True)

screen buttonExample:
    imagebutton:
        focus_mask True
        auto "closet.png"
        hovered (SetVariable("whom", "The Choose Button"))
        unhovered (SetVariable("whom", ""))
        action [SetVariable("whom", ""), Hide("buttonExample"), Jump ("bedroom_day")]

screen generatetext(word_list):
    grid 3 3:
        align (.5,.3)
        spacing 100
        for word in word_list:
            textbutton "[word]" action If(textclicked == False, true = SetVariable("textclicked",True), false = SetVariable("textclicked",False))#NullAction() #text_style "pc_button" left_margin 1
    textbutton "done" action Return()
# The game starts here.

label start:
    mc "..."

    play music "apartment.mp3" fadein 0.2 loop

    scene wakeup with fade

    mc "...ah..."
    mc "Another day."
    mc "....."

    mcs "Up, girl."
     
    scene bedroom_day with fade

    mc "You need clothes."
    mc "And... ...ah... to eat something."
    mc "...Today is a big day."

    label bedroom_day1:
        scene bedroom_day with dissolve
        call screen bedroom_day_choices()

    label closet_day1:
        $ menu_flag = True
        if outfit[day] != "none":
            mc "You already put on some clothes... do you want to change?"
            menu:
                "Yeah.":
                    mc "You take another look at your options."
                "No, these clothes are fine.":
                    jump expression "bedroom_day" + str(day)
        #play sound "closetcreak.wav"
        scene closet_inside with fade
        mc "..."
        call screen closet_choices
        scene blackscreen with fade
        play sound "clothesrustle.wav"
        pause 2.0
        jump expression "bedroom_day" + str(day)

    label kitchen_day1:
        $ menu_flag = True
        scene kitchen with fade
        play music "kitchen.wav" loop
        mc "..."
        if (outfit[day] == "None"):
            mc "Can't just go to work in your PJs, though you wish you could..."
            jump expression "bedroom_day" + str(day)
        if day == 1:
            mc "...It's nasty in here..."
            mc "...But whose fault is that?"
            mc "..."
            mc "...Well, better eat something."
        else:
            mc "...You should eat something."
        scene blackscreen with fade
        play sound "closetcreak.wav" volume 0.7
        scene hotpocket with fade
        mc "..."
        mc "Nothing like a nutritious breakfast."
        scene blackscreen with fade
        play sound "plastic.wav"
        queue sound "microwaveshort.wav"
        pause 8
        scene kitchen with fade
        mc "...Time to go."
        scene blackscreen with fade
        play sound "leavehome.wav"
        queue sound "footsteps.wav" volume 0.4
        pause 4
        jump expression "subway_day" + str(day)
    
    label subway_day1:
        play music "platformday.mp3" fadein 0.5 loop volume 0.7
        scene subway_day with fade
        mc "...Ah. It's pretty nice out today, actually..."
        mc "The train should be here in a few minutes."
        mc "..."
        mc "...?"
        mc "...There's a man further down the platform who seems to be looking at you."
        mc "..."
        mc "...You keep your head down and pretend to be interested in something else."
        mc "..."
        show strangeman at slightright with moveinright
        mc "...!" #man moves closer in image
        play sound "trainarriving.wav"
        mc "..."
        mc "Ah -- the train is coming."
        scene blackscreen with fade
        pause 2.0
        mc "...He stayed behind on the platform..."
        mc "The rest of the ride passes uneventfully."
    
    label arrive_office_day1:
        play music "office.mp3" fadein 0.5 loop volume 0.5
        scene office with fade
        "..."
        show keith with moveinleft
        k "Ah!"
        k "Look who it is. Just who I was hoping to run into."
        mc "..."
        mc "You work in cubicles directly across from each other. The chances of *not* running into each other are incredibly slim."
        mcs "...Good morning."
        if outfit[1] == 'fun':
            k "I gotta say you're looking... fantastic... today. Really improving the morale of the guys around here, if you know what I'm saying!"
            mc "..."
            mcs "...Thanks."
        if outfit[1] == 'casual':
            k "Come to think, uh, you feeling alright today? You're looking a little under-the-weather..."
            mc "...!"
            mcs "Uh... I feel fine. Just... didn't feel like jumping through any hoops today. Need to get to work."
        hide keith
        show keithannoyed
        k "..."
        k "What, that's all? C'mon, I've got nothing to do. Tell me how your weekend was."
        mc "..."
        mcs "...My weekend was fine. I just have a lot to do today, that's all."
        k "..."
        k "Sure, sure, suit yourself." 
        k "Honestly I don't know why you bother anyways, they never seem to give a shit. But don't let me stop you. I'll talk to you later."
        hide keithannoyed with moveoutleft
        mc "..."
        mc "Well, you're here. Better get to work."
        
        
    label office_day1:
        scene office with dissolve
        if computer_sensitive == False:
            mc "...You've worked about as much as you can for today. Are you ready to go?"
            menu:
                "..."

                "...Yeah. Let's head home.":
                    jump expression "subway_night" + str(day)
                "...No, not yet.":
                    mc "..."
        call screen office_day_choices

    label keith_day1:
        if keith_sensitive == False:
            mc "You try to get keith's attention, but he's glued to his computer."
        else:
            mcs "...Hey, uh, Keith?"
            mc "Keith spins around in his chair."
            k "...Oh? I thought you didn't have time to talk to little old me today."
            if outfit[1] == 'fun':
                k "Consider me graced by your presence."
            mcs "...Well, uh... I was just wondering if you finished your portion of the project yet. It's just got some info I'll need soon."
            k "Yeah, yeah, don't worry about it..."
            mc "You see that his focus has already drifted back to the game."
            $ keith_sensitive = False
        jump expression "office_day" + str(day)

    label computer_day1:
        $ menu_flag = True
        if computer_sensitive == False:
            mc "You're too tired to work on this more, for now... you're simply out of juice."
            jump expression "office_day" + str(day)
        scene computer with fade
        mc "Alright. Let's get started."
        $ computer_sensitive = False
        call screen generatetext(word_list)
        #mc "You play an astoundingly fun and captivating minigame that truly knocks your socks off."
        mc "..."
        mc "You finish up what you were doing. That should be enough."
        menu:
            "How did you do?"

            "Well":
                #action[SetDict(workperformance, day, 1)]
                mc "You feel like you did well today."
                $ workaverage += 1
            "Alright":
                mc "You caught some snags, but managed to finish what you needed to do."
                #action[SetDict(workperformance, day, 0)]
            "Poorly":
                #action[SetDict(workperformance, day, -1)]
                mc "...There's always tomorrow."
                $ workaverage -=1
        jump expression "office_day" + str(day)

    #label boss_office_day2:
    #    show boss_office with fade

    label bathroom_day1:
        if bathroom_sensitive == False:
            mc "Already went. You don't have to go *that* often."
            jump expression "office_day" + str(day)
        scene bathroom with fade
        mc "...You breathe a sigh of relief. You always feel a little more alone in here."
        mc "...Probably helps that there are only a few women at the company... You never have to wait for your favorite stall."
        mc "...Second from the left."
        scene blackscreen with fade
        #play rummage sound and flush
        pause 2
        scene mirror with fade
        #play water sound
        mc "..."
        mc "Well... Time to get back out there."
        $ bathroom_sensitive = False
        scene blackscreen with fade
        jump expression "office_day" + str(day)

    label subway_night1:
        scene subway_night with fade
        play music "platformnight.mp3" loop
        mc "Geez... how is it so dark already?"
        mc "Must've been working longer than you thought..."
        mc "..."
        mc "You take a moment to breathe."
        mc "Today you've just felt... wired."
        mc "..."
        show strangeman at slightright with moveinright
        mc "...!"
        mc "The same man from this morning is here."
        mc "He's not even bothering to be subtle. He's staring you up and down."
        play sound "heartbeat.wav" loop
        mc "..."
        mc "His eyes are boring straight into you."
        mc "You look over your shoulder. Nobody else is around."
        mc "..."
        mc "You quickly check your phone to see when the train will be arriving."
        mc "It's still a few minutes away."
        mc "..."
        show strangeman at center with move
        mc "...He's getting closer..."
        mc "..."
        mc "You feel like you need to get away. You decide to move further down the platform."
        play sound "footsteps.wav"
        queue sound "heartbeat.wav" loop
        hide strangeman with moveoutright
        mc "...He doesn't follow you. But he doesn't stop staring, either."
        mc "You wait like that for another minute or so, praying he won't decide to come near you again."
        play sound "trainarriving.wav"
        pause 5
        scene blackscreen with fade
        mc "...Thank god. The train is arriving."
        mc "You find a car with plenty of people on it and quickly step inside."
        mc "The doors slide shut. You spare a glance out the window..."
        mc "The man is standing right where you had been just a moment ago."
        mc "..."
        mc "...The rest of the ride passes uneventfully."
    
    label returnhome_night1:
        play sound "returnhome.wav"
        scene kitchen with fade
        queue music "kitchen.wav" loop
        mc "..."
        mc "It feels good to be alone."
        mc "...You can't say you feel like having anything to eat."
        $ closet_sensitive = True
        scene blackscreen with fade
        play sound "doorcreak.wav"

    label bedroom_night1:
        scene bedroom_night with dissolve
        play music "apartment.mp3" loop
        call screen bedroom_night_choices
        
    label closet_night1:
        $ menu_flag = True
        if closet_sensitive == False:
            mc "You're already in your pajamas."
            jump bedroom_night1
        scene blackscreen with fade
        play sound "clothesrustle.wav"
        mc "You change out of your clothes and hang up what isn't too dirty..."
        $ closet_sensitive = False
        jump bedroom_night1
        
    label journal_night1:
        $ menu_flag = True
        if journal_sensitive == False:
            "You wrote already today. You're feeling too tired to make another entry."
            jump bedroom_night1
        scene journal with fade
        mc "Your journal. Might as well use this thing."
        mc "What do you want to write about?"
        menu:
            "..."
            
            "Work.":
                #scene blackscreen with fade
                #scene journal with fade
                show journal_entry_1a with fade
            "The man on the platform.":
                #scene blackscreen with fade
                #scene journal with fade
                show journal_entry_1b with fade

        mc "..."
        mc "You wish there wasn't so much on your mind."
        $ journal_sensitive = False
        jump bedroom_night1

    label bed_night1:
        $ menu_flag = True
        mc "...Are you ready for bed?"
        menu:
            "..."

            "Yeah.":
                jump end_night1
            "Not yet.":
                jump bedroom_night1

    label end_night1:
        scene blackscreen with fade
        mc "...It's been a long day. You're exhausted."
        mc "Falling into the soft covers, you find yourself drifting off almost immediately."
        mc "..."
        mc "You dream of being chased through a dark hallway by some unknown pursuer."
        mc "Rows upon rows of doors line the walls -- but each time you try to duck into one, you find it locked."
        mc "The only thing left to do is run."
        mc "...You run until you find yourself at the end of the hallway in front of one last door."
        mc "You reach out desperately, against all hope, to try and open it..."
        mc "It's stuck."
        play sound "nightmarebreath.wav"
        pause 3
    
    label wakeup_day2:
        scene wakeup with fade
        mc "...!"
        mc "..."
        mc "...Ah..."
        $ day = 2
        scene bedroom_day with fade
        
    label bedroom_day2:
        scene bedroom_day with dissolve
        play music "apartment.mp3" loop
        call screen bedroom_day_choices

    label closet_day2:
        $ menu_flag = True
        if outfit[day] != "none":
            mc "You already put on some clothes... do you want to change?"
            menu:
                "Yeah.":
                    mc "You take another look at your options."
                "No, these clothes are fine.":
                    jump expression "bedroom_day" + str(day)
        #play sound "closetcreak.wav"
        scene closet_inside with fade
        mc "..."
        call screen closet_choices
        scene blackscreen with fade
        if outfit[2] == "fun" and outfit[1] == "fun":
            mc "You normally love these clothes."
            mc "A colorful v-neck shirt... you got it on vacation with your mom... and a pair of nicely-cut pants you've practically loved to death."
            mc "...But..."
            mc "Maybe it's all a little ... much?"
            mc "Maybe that's why you attracted so much... attention, yesterday...?"
            mc "...Wear them anyway...?"
            menu:
                "..."
                "Yeah.":
                    mc "...Regardless of what anyone else thinks, you feel good in this outfit."
                "...No...":
                    mc "...You decide to err on the side of caution."
                    mc "...But then... with that logic..."
                    mc "Will you ever actually wear these again?"
                    mc "The thought makes you a little sad."
                    mc "Maybe just... not today..."
                    $ outfit[day] = "none"
                    jump expression "closet_day" + str(day)
        if outfit[2] == "casual" and outfit[1] != "casual":
            mc "...Wearing these clothes is akin to hiding for you. Maybe you'll be left alone in them."
        play sound "clothesrustle.wav"
        pause 2.0
        jump expression "bedroom_day" + str(day)
    
    label kitchen_day2:
        $ menu_flag = True
        scene kitchen with fade
        play music "kitchen.wav" loop
        mc "..."
        if (outfit[day] == "None"):
            mc "...Really ought to put on some clothes first."
            jump expression "bedroom_day" + str(day)
        else:
            mc "...Well, better eat something."
        scene blackscreen with fade
        play sound "closetcreak.wav" volume 0.7
        scene hotpocket with fade
        mc "..."
        mc "What would the regal queen like in her breakfast today? The finest of ground animal-parts in discs, or in chunks?"
        menu:
            "..."
            "...Pepperoni.":
                mc "Ahh, exquisite choice."
            "...Sausage.":
                 mc "Only the finest."
        scene blackscreen with fade
        play sound "plastic.wav"
        queue sound "microwaveshort.wav"
        pause 8
        scene kitchen with fade
        mc "...Time to go."
        scene blackscreen with fade
        play sound "leavehome.wav"
        queue sound "footsteps.wav" volume 0.4
        pause 4
        jump expression "subway_day" + str(day)

    label subway_day2:
        scene subway_day
        mc "..."
        mc "You look around, but the strange man from last night doesn't seem to be here today."
        play sound "trainarriving.wav"
        mc "...And the train is already arriving. Lucky."
        scene blackscreen with fade
        pause 4

    label arrive_office_day2:
        play music "office.mp3" fadein 0.5 loop volume 0.5
        scene office with fade
        "..."
        if outfit[day] == 'fun' and outfit[1] != 'fun':
            show keithhorny with moveinleft
            k "Hey, hey. Welcome back..."
            k "Looking great today... I love it. That shirt looks fantastic on you."
            mc "..."
            mcs "...Thanks."
        if outfit[day] == 'fun' and outfit[1] == 'fun':
            show keithhorny with moveinleft
            k "Hey, hey. Welcome back..."
            k "...Didn't you wear that yesterday? Not that I'm complaining. You oughta know that's all extremely flattering on you. Keep it up and I might not be able to focus on my work anymore, haha."
            mc "Your face flushes a little bit."
            mcs "...Thanks."
            hide keithhorny with moveoutleft
        if outfit[day] == 'casual' and outfit[1] != 'casual':
            show keith with moveinleft
            k "Hey hey hey... look who it is!"
            mc "..."
            k "Uh... you feeling sick today or something? Geez, girl, it looks like you just rolled out of bed."
            mc "..."
            mc "Your face flushes with embarrasment."
            mc "Does he not realize most of your department wears pretty much the same thing every day?"
            mcs "Well, uh... I just felt like taking it easy today, I guess. It gets cold in here, y'know?"
            k "..."
            k "Ha, sure. See you later."
            hide keith with moveoutleft
        if outfit[day] == 'casual' and outfit[1] == 'casual':
            show keithannoyed with moveinleft
            k "Hey, morning."
            mcs "...Morning."
            k "Not feeling so well again today? You should honestly just go home if you need to, you know that, right?"
            mc "..."
            mcs "...Like I said yesterday, I'm feeling fine."
            k "Wooah, hey, no need to crucify me for being worried about you. Guess I'll just shove it if that's what you want."
            mc "..."
            mc "...Jesus."
            hide keith with moveoutleft
        mc "..."
        mc "...Well, you're here. Better get to work."
        $ computer_sensitive = True
        $ bathroom_sensitive = True

    label office_day2:
        scene office with dissolve
        if computer_sensitive == False:
            mc "...You've worked about as much as you can for today. Are you ready to go?"
            menu:
                "..."

                "...Yeah. Let's head home.":
                    jump expression "subway_night" + str(day)
                "...No, not yet.":
                    mc "..."
        call screen office_day_choices

    label keith_day2:
        mc "...Keith is messing with his phone. He either doesn't realize you're there or is actively ignoring you."
        jump expression "office_day" + str(day)

    label bathroom_day1:
        if bathroom_sensitive == False:
            mc "...If you go in there again so soon surely somebody will notice."
            jump expression "office_day" + str(day)
        scene bathroom with fade
        mc "..."
        mc "...Second from the left."
        scene blackscreen with fade
        #play rummage sound and flush
        pause 2
        scene mirror with fade
        #play water sound
        mc "..."
        mc "Well... Time to get back out there."
        $ bathroom_sensitive = False
        scene blackscreen with fade
        jump expression "office_day" + str(day)

    label computer_day2:
        $ menu_flag = True
        if computer_sensitive == False:
            mc "...You really can't bring yourself to look at that any longer."
            jump expression "office_day" + str(day)
        scene computer with fade
        mc "Alright. Let's get started."
        $ computer_sensitive = False
        call screen generatetext(word_list)
        #mc "You play an astoundingly fun and captivating minigame that truly knocks your socks off."
        mc "..."
        mc "That should be enough."
        menu:
            "How did you do?"

            "Well":
                #action[SetDict(workperformance, day, 1)]
                mc "Thankfully, you feel pretty confident in your work today. That eases your mind a bit."
                $ workaverage += 1
            "Alright":
                mc "You hope that was enough."
                #action[SetDict(workperformance, day, 0)]
            "Poorly":
                #action[SetDict(workperformance, day, -1)]
                mc "...Maybe tomorrow will be better."
                $ workaverage -=1
        jump expression "office_day" + str(day)

    label subway_night2:
        scene subway_night with fade
        mc "..."
        mc "...You look over your left shoulder... then your right."
        mc "..."
        mc "...Nothing seems out of the ordinary today..."
        play sound "trainarriving.wav"
        mc "...And the train is already coming. Good timing."
        scene blackscreen with fade
        pause 3
        scene on_subway with fade
        play music "trainride.wav" loop fadein 0.5
        mc "..."
        mc "...It feels nice to just zone out for a while."
        mc "..."
        mc "Ah!"
        mc "A tap on your shoulder..."
        show diana with moveinleft
        mc "...!"
        d "No way! I thought that might be you!"
        mc "You can't believe it. It's Diana. You haven't seen her in years."
        d "I hope I didn't scare you. It's... it's really good to see you again... how are you?"
        mcs "I'm --"
        mcs "I'm good."
        mcs "..."
        mcs "It's really good to see you too... I mean it."
        show dianahappy with dissolve
        mc "..."
        mc "Wow. You missed seeing her smile like that."
        show diana with dissolve
        d "...Well, um... while we're here..."
        d "...I really just wanted to say I'm sorry I haven't... kept in touch."
        d "Things just... "
        show dianasad with dissolve
        d "Started moving a little fast for me. Life, I mean..."
        d "...I just had a hard time keeping up with it all. So... I just kind of... disappeared. It wasn't with just you, I promise."
        d "..."
        d "I, uh... I understand if that's a pretty terrible excuse. I'm sorry."
        mcs "No!"
        show dianasurprised with dissolve
        d "...!"
        mcs "-- Sorry, uh --"
        mcs "You just... don't need to apologize."
        mcs "...I..."
        mcs "...I understand."
        d "..."
        show dianahappy with dissolve
        d "...Thank you."
        mc "..."
        play sound "trainchime.wav" volume 0.2
        d "...ah!"
        d "..."
        d "That's my stop..."
        d "Um... I hope we can talk again sometime soon... ok?"
        scene blackscreen with fade
        mc "..."
        mc "With that, Diana turned and stepped through the door."
        mc "..."
        mc "...Will that be the last time you see her?"
        mc "Last time... you parted the same way."
        mc "..."

    label returnhome_night2:
        play sound "returnhome.wav"
        scene kitchen with fade
        play music "kitchen.wav" loop
        mc "..."
        $ closet_sensitive = True
        scene blackscreen with fade
        play sound "doorcreak.wav"

    label bedroom_night2:
        scene bedroom_night with dissolve
        play music "apartment.mp3" loop
        $ journal_sensitive = True
        call screen bedroom_night_choices
        
    label closet_night2:
        $ menu_flag = True
        if closet_sensitive == False:
            mc "You're already in your pajamas."
            jump bedroom_night1
        scene blackscreen with fade
        play sound "clothesrustle.wav"
        mc "You change out of your clothes and hang up what isn't too dirty..."
        $ closet_sensitive = False
        jump bedroom_night1
        
    label journal_night2:
        $ menu_flag = True
        if journal_sensitive == False: 
            "You wrote already today. You're feeling too tired to make another entry."
            jump bedroom_night1
        scene journal with fade
        mc "..."
        mc "What do you want to write about tonight?"
        menu:
            "..."
            
            "Diana.":
                #scene blackscreen with fade
                #scene journal with fade
                show journal_entry_2a with fade
            "Time.":
                #scene blackscreen with fade
                #scene journal with fade
                show journal_entry_2b with fade

        mc "..."
        mc "You wish there wasn't so much on your mind."
        $ journal_sensitive = False
        jump bedroom_night2

    label bed_night2:
        $ menu_flag = True
        mc "...ready to sleep?"
        menu:
            "..."

            "Yeah.":
                jump end_night2
            "Not yet.":
                jump bedroom_night2

    label end_night2:
        scene blackscreen with fade
        mc "..."
        mc "You don't really want to think anymore."
        mc "..."
        mc "You spend some time staring into space and trying not to worry, until you fight your way to sleep."
        mc "..."    
        mc "You dream of nothing."
        mc "...Nothing at all."
        pause 3






        















    mc "gabaghoul you have finished"
        

    #show person with moveinright
    #I want you to check in with Gary, alright?

    #e "You've created a new Ren'Py game."

    #e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.jj

    

    return
