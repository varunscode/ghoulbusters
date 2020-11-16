import time
drunk = False 
wine_bottle = False
cellar_key = False
necklace = False
eviction_notice = False
items = 0
name = "user"
def startgame():
    print("""
███████ ██   ██  █████  ██████  ██████      ███████ ████████ ██    ██ ██████  ██  ██████  ███████ 
██      ██   ██ ██   ██ ██   ██ ██   ██     ██         ██    ██    ██ ██   ██ ██ ██    ██ ██      
███████ ███████ ███████ ██████  ██   ██     ███████    ██    ██    ██ ██   ██ ██ ██    ██ ███████ 
     ██ ██   ██ ██   ██ ██   ██ ██   ██          ██    ██    ██    ██ ██   ██ ██ ██    ██      ██ 
███████ ██   ██ ██   ██ ██   ██ ██████      ███████    ██     ██████  ██████  ██  ██████  ███████ 
                                                                                                  """)

    time.sleep(2.5)

    print(""" 
 _______  _______     ________   ______   ________  ____  _____  _________   ______   
|_   __ \|_   __ \   |_   __  |.' ____ \ |_   __  ||_   \|_   _||  _   _  |.' ____ \  
  | |__) | | |__) |    | |_ \_|| (___ \_|  | |_ \_|  |   \ | |  |_/ | | \_|| (___ \_| 
  |  ___/  |  __ /     |  _| _  _.____`.   |  _| _   | |\ \| |      | |     _.____`.  
 _| |_    _| |  \ \_  _| |__/ || \____) | _| |__/ | _| |_\   |_    _| |_   | \____) | 
|_____|  |____| |___||________| \______.'|________||_____|\____|  |_____|   \______.' 
                                                                                      
                                                                                      """)
    
    
    time.sleep(2.5)
    
    
    print("""  
 ▄████  ██░ ██  ▒█████   █    ██  ██▓        ▄▄▄▄    █    ██   ██████ ▄▄▄█████▓▓█████  ██▀███    ██████ 
 ██▒ ▀█▒▓██░ ██▒▒██▒  ██▒ ██  ▓██▒▓██▒       ▓█████▄  ██  ▓██▒▒██    ▒ ▓  ██▒ ▓▒▓█   ▀ ▓██ ▒ ██▒▒██    ▒ 
▒██░▄▄▄░▒██▀▀██░▒██░  ██▒▓██  ▒██░▒██░       ▒██▒ ▄██▓██  ▒██░░ ▓██▄   ▒ ▓██░ ▒░▒███   ▓██ ░▄█ ▒░ ▓██▄   
░▓█  ██▓░▓█ ░██ ▒██   ██░▓▓█  ░██░▒██░       ▒██░█▀  ▓▓█  ░██░  ▒   ██▒░ ▓██▓ ░ ▒▓█  ▄ ▒██▀▀█▄    ▒   ██▒
░▒▓███▀▒░▓█▒░██▓░ ████▓▒░▒▒█████▓ ░██████▒   ░▓█  ▀█▓▒▒█████▓ ▒██████▒▒  ▒██▒ ░ ░▒████▒░██▓ ▒██▒▒██████▒▒
 ░▒   ▒  ▒ ░░▒░▒░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ░ ▒░▓  ░   ░▒▓███▀▒░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░  ▒ ░░   ░░ ▒░ ░░ ▒▓ ░▒▓░▒ ▒▓▒ ▒ ░
  ░   ░  ▒ ░▒░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░ ▒  ░   ▒░▒   ░ ░░▒░ ░ ░ ░ ░▒  ░ ░    ░     ░ ░  ░  ░▒ ░ ▒░░ ░▒  ░ ░
░ ░   ░  ░  ░░ ░░ ░ ░ ▒   ░░░ ░ ░   ░ ░       ░    ░  ░░░ ░ ░ ░  ░  ░    ░         ░     ░░   ░ ░  ░  ░  
      ░  ░  ░  ░    ░ ░     ░         ░  ░    ░         ░           ░              ░  ░   ░           ░  """)

    time.sleep(2)
    print("""On all hallows eve, five friends gather at a remote location of an abandoned house looking for a spooky adventure.
Sally, Freddie, Jack and Annabelle look upon the decaying house and slowly make there way through the front entrance.""")
    time.sleep(1)
    global name
    time.sleep(2)
    name = input("What is your name? ")
    print("Hello {}, it's so great to meet you.".format(name)) 
    time.sleep(2)
    print("After the 5 of you settle in you decide what you want to do first")
    option1()

movie = ["The Shining[1]","Nightmare on Elm street[2]","Halloween[3]"]
def option1():
    global drunk
    time.sleep(2)
    print("What do you want to do?")
    ouija_board = "use the Ouija board[2]"
    horror_movie = "watch a horror movie[3]"
    drink = "get drunk[1]"

    if drunk == False:
        activity = input("Would you like to {}, {} or {}?".format(drink,ouija_board,horror_movie))
    else:
        activity = input("Would you like to {} or {}?".format(ouija_board,horror_movie))
    
    if activity == "1":
        drunk = True
        time.sleep(1)
        print("10 shots in you're finally getting the courage to partake in the exciting activities")
        option1()

    elif activity == "2":

        print("Ouija board lets go")
        time.sleep(2)
        print("The five friends gather around the Ouija board and place a finger on the glass.")
        time.sleep(2)
        print("A few moments pass before the glass begins to move.")
        time.sleep(2)
        print("All of a sudden a ghost appears before them!")
        print("""
   .-.
   .'   `.
   :g g   :
   : o    `.
  :         ``.
 :             `.
:  :         .   `.
:   :          ` . `.
 `.. :            `. ``;
    `:;             `:'
       :              `.
        `.              `.     .
          `'`'`'`---..,___`;.-'""")
        time.sleep(2)
        print("""Friendly ghost – “Please, don’t be afraid. I am here to help you explore the old secrets of the house!
Once upon a time and old woman used to live here, living her days in lavish splendour.""")
        time.sleep(2)
        print("""Until one day her money was gone, and was to be forced onto the streets! Before the bailiffs could remove her""")
        time.sleep(2)
        print("""
She curses the house claiming it for herself and damned anyone who would enter!""")
        time.sleep(2)
        print("""
The lady then climbed into the loft and hung herself!""")
        time.sleep(2)
        print("""
Friendly ghost – “I fear you may have woken her spirit and she’s out looking for vengeance! """)
        time.sleep(2)
        print("""  
We must create a ceremony to free her spirit! 

This is what the Lady in Grey sings every night! Can you help me?
""")

        time.sleep(2)
        print("I have 5 things that soothe my soul")
        time.sleep(2)
        print("A glass of wine that I adore")
        time.sleep(2)
        print("A priceless heirloom I long for")
        time.sleep(2)
        print("A hairbrush needed to keep me neat")
        time.sleep(2)
        print("A necklace to wear for when we meet")
        time.sleep(2)
        print("the notice for my house is a must")
        time.sleep(2)
        print("for my death is the cause of this unjust!")
        time.sleep(2)
        
        casper()

    elif activity == "3":
        print("what horror movie do you want to watch?")
        time.sleep(2)
        movie_response = input(movie)
        if movie_response == "1":   
            print("You are now watching The Shining")
            time.sleep(2)
            print("After getting shit scared,you move on to your next activity")
            option1()
        elif movie_response == "2":   
            print("You are now watching Nightmare on Elm Street")
            time.sleep(2)
            print("After getting shit scared,you move on to your next activity")
            option1()
        elif movie_response == "3":   
            print("You are now watching Halloween")
            time.sleep(2)
            print("After getting shit scared,you move on to your next activity")
            option1()
        else:
            print("I dont understand")
            option1()


    else:
        print("Invalid input")
        option1()

def casper():
    time.sleep(1)
    print("Do you accept this mission and choose to help Casper?")
    time.sleep(1)
    explore = input("Yes[Y] No[N]")
    if explore.upper() == "Y" or explore == "1" or explore.upper() == "YES":
        print("Casper: Thank you so  much! We can get rid of her together!")
        time.sleep(1)
        print("We'll start in the hallway and from there you can get to every room in the house.")
        hallway()
    elif explore.upper() == "N" or explore == "2" or explore.upper() == "NO":
        print("Wow, I did not expect that from you, what a loser")
        time.sleep(2)
        print("Are you sure you dont want to carry on?")
        sure = input("Yes[Y] No[N]")
        if sure.upper() == "Y" or sure == "1":
            time.sleep(2)
            print("wow you gave up before you even started")
            time.sleep(2)
            print("GAMEOVER")
            gameover()
        elif sure.upper() == "N" or explore.upper() == "NO" or explore == "2":
            print("Good, we need you to be brave to get though this game!")
            time.sleep(1)
            print("We'll start in the hallway and from there you can get to every room in the house.")
            hallway()
        else:
            print("I didnt understand what you said")
            casper()
    else:
        print("I didnt get that")
        casper()
    
def hallway():
    global items
    time.sleep(2)
    print("Casper: Which room do you want to go to?")
    time.sleep(1)
    room = input("Bedroom[1],Cellar[2],Kitchen[3],Living Room[4],Study[5],Dining Room[6],Loft[7]")
    if room == "1":
        time.sleep(2)
        print("""You enter the bedroom with your friends.
Everything seems to be intact, although somewhat full of dust and cobwebs! """)
        time.sleep(2)
        print("""You feel a bad energy in this room, like somebody is watching you…
        """)
        bedroom()
    elif room == "5":
        print("The group enter the study, filled with musty old books and newspapers.")
        time.sleep(2)
        print('Annabelle “Look at these things! they seem somewhat peculiar"')
        study() 
    elif room == "3":
        time.sleep(1)
        print("""You are now entering the Kitchen
The group enter the Kitchen. Nothing seems to be out of place, except for the usual signs of decay and lack of upkeep.""")
        time.sleep(2)
        print("""
You see an old cooking stove, various food cabinets with a crumbling dining table and chairs”
Jack – “Whoever lived here seemed to enjoy their wine!" """)
        time.sleep(1)
        kitchen() 
    elif room == "4":
        print("""
You enter the living room. It's a comfortable looking space, with a couch and arm chairs surrounding. 
Although the materials were worn down, you feel it was once had a homely feel. 
    """)
        time.sleep(2)
        print("""
To the back of the living room you see a large dusty fireplace. An unused candle stick sits next to it. The
fireplace looks like it's still burning. Has someone been here?
    """)
        living_room()
    elif room == "2" and cellar_key == True:
        print("You turn the rusty door knob and are met with a long stair well.")
        time.sleep(2)
        print("You make your way down, down, down until you finally reach the bottom.")
        time.sleep(2)
        print("It's cold and damp, you don't feel like you want to stay in here too long.")
        time.sleep(2)
        print("As you quickly explore the cellar you notice a piece of paper stapled to a notice board along with various other newspaper clippings.")
        time.sleep(2)
        print("It's an eviction notice which reads that the property is to be repossessed by the bank.")
        time.sleep(2)
        print("What do you want to do?")
        cellar()
    elif room == "2" and cellar_key == False:
        print("You try and open the door, it is locked. There must be a key somewhere in this house")
        hallway()
    elif room == "6":
        time.sleep(2)
        print("A large spacious area filled with taxidermy and a grand chandelier")
        time.sleep(2)
        print("Among the peeled wallpaper you see a huge painting. It's the old lady sitting ready and poised.")
        time.sleep(2)
        print("Her stare is bone chilling!")
        time.sleep(2)
        print("The table has been set as if ready to serve food! But look at this spoon?")
        time.sleep(2)
        print("It appears to have a family crest engraved on it.")
        time.sleep(2)
        print("It must be a family heirloom!")
        dining_room()
    elif room == "7":
        if items >=6:
            print("You are entering the loft")
            loft()
        elif items <= 4:
            print("You dont have everything you need yet to face the Lady in Grey! She will kill you!")
            hallway()
        else:
            print("Casper: You havent got everything you need yet! The lady in grey will kill you!")
            hallway()
    else:
        print("Thats not a valid room choice!")
        hallway()

def bedroom(): 
    global items
    time.sleep(1) 
    response = input("Do you continue to explore the bedroom? Y/N ")
    if response.upper() == "Y" or response == "1" or response.upper() == "YES":
        print("You and your friends explore the eerie bedroom.")
        bedroom_1()
    elif response.upper() == "N" or response.upper() == "NO" or response == "2":
        print("You exit the room and go back to the hallway.")
        hallway()
    else:
        print("Sorry, that choice is not recognised, please try again.")
        bedroom()
choices = [
    "Inspect Old Hair Brush[1]",
    "Inspect Old Photograph[2]", 
    "Exit room[3]"
    ] 
N = len(choices)
def bedroom_1():
    global items
    time.sleep(1)
    if choices[0] == "Inspect Old Hair Brush[1]":
        time.sleep(1)
        print("In the bedroom you can see an old hair brush and an old photograph." )
        time.sleep(1)
        print("What would you like to do?" )
    elif choices[0] == "Inspect Old Photograph[2]": 
        time.sleep(1)
        print("In the bedroom you can see the outline of the hair brush left in the dust and an old photograph." )
        time.sleep(1)
        print("What would you like to do?" ) 
    
    for i in range(N):
        print(choices[i])
        time.sleep(1)
        print(choices[i+1])
        response = input("What do you do?")
        if response == "1": 
            time.sleep(1)
            print("The hair brush definitely looks old. It is discoloured and covered in dust")
            time.sleep(2)
            print("""
            
                                                                        .,,,    
                                                                .,,,.,,,#*,**** 
                            (# &  %                        ,.,.,,.,./,,,,***//, 
               (.% %#/@.&&@ *# &&&#.@(%@              .,,,,,,,,,,,***////*(,.   
          %/#/#& %&&&(&*%&&.@@.& @.*& @ %%#     .,,.....,****/*////**,..        
     ,# #&/#&&#&&@@@%@@%@*&,@@&@@&@@*@,&%@%@,,,,.,,,**/*///*,...                
    ,&.&@(&%@@@@#@%&&#@&@@&,@*%*@/@@@&#&*@%,*,*****,.                           
  /.&%&@@%@@%&@@@@&@*@*&,@*@*%@@@@@/&@#@@(/****,.                               
  %%&@&&@@#&%#@@%*@@/@/%*@#@*@/&@%&&##&#(///(.                                  
  &&&%&&@@%&@&@@&*@/@%(%&(/&(&/&##&%%(#///*.                                    
   #&(%@@%&&/&#(#/&(#(&#&(%#%#%@&((/(//*.                                       
   ((&%%%#%&(%(#%#%#%(%&%%//((////**.                                           
   .((((#((%(%((((#/(////////(*..                                               
     .,(/(///////////(/,,.                                                      """)
            response = input("Would you like to take the hair brush? Y/N ")
            if response.upper() == "Y" or response.upper() == "YES": 
                items += 1
                time.sleep(1)
                print("You take the old hair brush")
                
                choices.remove("Inspect Old Hair Brush[1]")
                bedroom_1() 
            elif response.upper() == "N" or response.upper() == "NO" or response == 2: 
                bedroom_1()
            else: 
                print("Sorry, that choice is not recognised, please try again.")
        elif response == "2": 
            time.sleep(1)
            print("The photo shows a middle aged woman in a victorian style dress.")
            print("She is looking at you with a seemingly angry expression.")
            if drunk == True:  
                time.sleep(2)
                print("You are so intoxicated, it's as if the photograph is drawing you in.")
                print("The anger of the lady in grey, in the photograph, attacks your soul.")
                print("The anger is so intense it puts you into immense shock, forcing you to be paralysed with fear")
                time.sleep(2)
                print("GAMEOVER")
                gameover() 
            else:
                response = input("Would you like to look more? Y/N ")
                if response.upper() == "Y" or response.upper() == "YES" or response == 1:
                    time.sleep(2)
                    print("You feel the anger of the lady in grey attack your soul.")
                    print("The anger is so intense it puts you into immense shock, forcing you to be paralysed with fear")
                    gameover() 
                elif response.upper() == "N" or response.upper() == "NO" or response == 2:
                    time.sleep(2)
                    print("You stop looking at the picture. Probably for the best.")
                    bedroom_1()
                else: 
                    print("Sorry, that choice is not recognised, please try again.")
                    bedroom_1()
        elif response == "3":
            print("You leave the bedroom") 
            hallway()
        else:
            print("I dont understand")
            bedroom_1()
    
        
        
         
        

study_options = ["Pick up key[1]", "pick up the locket [2]", "return to hallway[3]"]

def study():
    global cellar_key
    global items
    global study_options
    print("What do you want to do?")

    study_choice = input(study_options)
    if study_choice == "1":
        study_options.pop(0)
        print("You have picked up the key to the cellar!")
        print("""
  ooo,    .---.
 o`  o   /    |\________________
o`   'oooo()  | ________   _   _)
`oo   o` \    |/        | | | |
  `ooo'   `---'         "-" |_|
  """)
        items += 1
        cellar_key = True
        
        study()
        
    elif study_choice == "2":
        if drunk == True:
            print("You open the locket, theres a photo of a lady who you assume to be the Lady in Grey")
            time.sleep(2)
            print("You couldnt keep your intoxicated gaze off the photo inside the locket of the Lady in Grey.")
            time.sleep(2)
            print("she jumps out of the photo and takes your soul")
            gameover()
        elif drunk == False:
            print("You open the locket, theres a photo of a lady who you assume to be the Lady in Grey")
            time.sleep(2)
            print("Do you want to keep staring?")
            time.sleep(2)
            death_stare = input("Yes[1] No[2]")
            if death_stare == "1" or death_stare.upper() == "Y" or death_stare.upper() == "YES":
                print("She jumps out of the photo and takes your soul")
                gameover()
            else:
                study()
    
    elif study_choice == "3":
        hallway()
    else:
        print("I didnt get that")
        study()

kitchen_options = ["Pick up a bottle of wine[1]","pick up the photo[2]","back to the hallway[3]"]
def kitchen():
    global items
    global wine_bottle
    global kitchen_options
    time.sleep(2)
    print("""What do you want to do?""")
    kitchen_choice = input(kitchen_options)
    if kitchen_choice == "1":
        if wine_bottle == False:
            time.sleep(2)
            print("You have picked up the bottle")
            time.sleep(2)
            print("""             __
           )==(
           )==(
           |H |
           |H |
           |H |
          /====|
         / Dr S |
        /========|
       :HHHHHHHH H:
       |HHHHHHHH H|
       |HHHHHHHH H|
       |HHHHHHHH H|
       |=/========|
       |oO/       |
       | oOOO  Le |
       | OOO Grape|  
       |  O       |   
       |==========| 
       |HHHHHHHH H|   
       |HHHHHHHH H|   
       |HHHHHHHH H|
       """)
            items += 1
            time.sleep(2)
            kitchen_options.pop(0)
            wine_bottle = True
            kitchen()
        elif wine_bottle == True:
            time.sleep(2)
            print("You already have a bottle, don't be greedy!")
            kitchen()
        else:
            print("error")
            kitchen()
    elif kitchen_choice == "2":
        if drunk == True:
            print("It’s a picture of the family who lived here. But the lady in this photo…I feel like she’s looking at me")
            time.sleep(2)
            print("As you are still drunk you cannot shift your eyes off the photo")
            time.sleep(2)
            print("The lady in grey comes out from the photo and paralyses you! GAMEOVER!")
            gameover()
        elif drunk == False:
            print("It’s a picture of the family who lived here. But the lady in this photo…I feel like she’s looking at me")
            time.sleep(2)
            print("Do you want to keep staring?")
            stare = input("Keep staring? [Y/N]")
            if stare.lower() == "y" or stare == "1":
                time.sleep(2)
                print("The lady comes out and possesses your soul GAMEOVER")
                gameover()
            else:
                print("That was a wise choice")
                kitchen()
    elif kitchen_choice == "3":
        print("You are now in the hallway")
        time.sleep(1)
        hallway()
    else:
        print("Casper: I dont understand what you want to do")
        kitchen()


def dining_room():
    global items
    global drunk
    
    time.sleep(2)
    print("What do you want to do?")
    paint_heirloom = input("look at painting[1], take the heirloom[2], go back to the hallway[3]")
    if paint_heirloom == "1":
        look_painting()
    elif paint_heirloom == "2":
        take_heirloom()
    elif paint_heirloom == "3":
        hallway()
    else:
        print("I don't understand that")
        dining_room()
def look_painting():
    global drunk
    print("You take a close look at the painting. It fills you with dread")
    time.sleep(2)
    if drunk == True:
        print("""You can't shift your intoxicated gaze from the painting.
The grey lady looks deep into your eyes. The fear builds up and you suffer a heart attack! YOU LOSE""")
        time.sleep(2)
        gameover()
    else:
        keep_looking = input ("Do you want to keep looking at the painting? [Y/N] ")
        if keep_looking.upper() == "Y" or keep_looking.upper() == "YES":
            print("The grey lady looks deep into your eyes. The fear builds up and you suffer a heart attack! YOU LOSE")
            gameover()
        elif keep_looking.upper() == "N" or keep_looking.upper() == "NO":
            dining_room()
        else:
            print("I don't understand that")
            look_painting()
def take_heirloom():
    global drunk
    global items
    print("You have collected the family heirloom!")
    time.sleep(2)
    print("""
                                                              (%%%((  *&&&      
                                                          %%%###(*    #&@&&     
                                                       &&&%%#(/,     ,%%%**,    
                                                    .#&&%##/*        /#****     
                                                   ,.   (((*       ,*,***,/.    
                                                 (%%#*,,*((*     *.,,**,,/...   
                                                .###((((((#( *,..,,,*.  ....    
                                                ,****,,,,,,....,,** ,,/,...     
                                                 *///****,,,,***,.,./,,..       
                                                 ***/////*****,,*#*,,..         
                                             **/////***,,,,,//**,..             
                                          ,,,*/*,,.                             
                                       ,,,,/,,,.                                
                                    ,,,,(,,,.                                   
                                 ,,,*(**,.                                      
                              .,./*/*,                                          
                           .,.(,**,                                             
                        ,,.(.(*,.                                               
                    ,,..,/(/*                                                   
                 .*...(./*.                                                     
             .,,...(***,                                                        
          .,,...,(.#*                                                           
      ,,,,...,(,*/                                                              
   ,,,,,,,,**,/.                                                                
 ,,...,,,(,#*                                                                   
   *.,/,(*                                                                      
""")
    items += 1
    hallway()
        


def cellar():
    global drunk
    global items
    if eviction_notice == False:
        eviction_notice = input("Do you want to take the eviction notice? [Y/N] ")
        if eviction_notice.upper() == "Y" or eviction_notice.upper() =="YES" or eviction_notice == "1":
            print("You have collected the eviction notice!")
            time.sleep(2)
            print("""
             _______________________
           =(__    ___      __     _)=
             |                     |
             |                     |
             |      EVICTION       |
             |       NOTICE        |
             |                     |
             |                     |
             |                     |
             |                     |
             |__    ___   __    ___|
           =(_______________________)=
           """)
            items += 1
            time.sleep(2)
            eviciton_notice = True
            hallway()

        elif eviction_notice.upper() == "N" or eviction_notice.upper == "NO" or eviction_notice == "2":
            hallway()
        else:
            print("I don't understand that")
            cellar()
    else:
        print("You already have what you need from the cellar! Why would you want to go back there?")
        hallway()

living_choice = ["Inspect the candlestick[1]", "Gaze into the fire[2]", "Exit room and return to the hallway[3]"]
def living_room(): 
    time.sleep(1) 
    global necklace 
    global items
    global living_choice
    
    print("What would you like to do?")
    response = input(living_choice)
    if response == "1":
        if necklace == False: 
            print("You check the candlestick out. It's placement seems quite suspicious")
            time.sleep(2)
            print(""" 

         __,---.__
      ,-'         `-.
    ,'               `.
   /                   .
  /         .           .
 ;           )           :
 |          ((           |
 |          ) \          |
 :         ( , )         ;
  \       _ `|'__       /
   \     ( ...._ )     /
    `.    )/(/( \|   ,'
      `- ()  )()|| -'
          | ()  ||
          |     ||
          |     ()
          |     |
          |     |
          |     |
          |     |
      ____|_____|____
     (________    ___)
        \___     _/
        (_____  __)
         \       /
          )__   (
         (____  _)
           |   |
           |   |
           |   |
           |   |
           |   |
           |   |
           |   |
         _/     \_
     .--'_________`--.

     """)
            time.sleep(2)
            print("What would you like to do?")
            time.sleep(2)
            response = input("Touch candlestick![1], Leave it alone[2] ")
            if response == "1": 
                print("A panel in the wall, above the candlestick, opens to reveal a necklace!")
                time.sleep(2)
                print("""

                o--o--=g=--o--o     
               /      .'       |
               o      '.       o
                \             /
                 o           o
                  \         /
                   o       o
                    \     /
                     o   o
                      \_/
                       =
                      .^.
                     '   '
                     '. .'
                       !   
                       """)
                print("You decide to take the necklace with you and the panel in the wall shuts shortly after")
                necklace = True 
                items +=1
                living_choice.pop(0)
                living_room()
            elif response == "2": 
                print("You ignore the candlestick and look elsewhere.")
                living_room() 
            else: 
                print("Sorry, that choice is not recognised, please try again.")
                living_room()
            
        elif necklace == True:

            print("You already done this")
            living_room()
        
        else:
            print("Sorry, that choice is not recognised, please try again.")
            living_room() 
    elif response == "2":
        if drunk == True:
            print("You gaze into the fire...on first look it looks like a regular fire but then you notice there is no fuel source.")
            time.sleep(2)
            print("""        ,   ."".   ,
      , #   |()|   # ,
     _#_#___|__|___#_#__
    [__________________]
     |-_ -=__=-_ -==_-|
     |_.------------.=|
     |=| o        o |=|
    _|-| !   `(   ! |-|_
   /==_| ! _(_.)_ ! |=_-|
   |   |/^\^=^^=^/^\| _=|
   """)
            time.sleep(2)
            print("The fire is burning out of thin air!")
            time.sleep(2)
            print("You look further into the fire...suddenly a woman's face appears from the fire laughing")
            time.sleep(2)
            print("The fire explodes! causing severe burning that you can never recover from.")
            gameover()
        else:
            print("You gaze into the fire...on first look it looks like a regular fire but then you notice there is no fuel source.")
            time.sleep(2)
            print("The fire is burning out of thin air!")
            time.sleep(2)
            print("""       
         ,   ."".   ,
      , #   |()|   # ,
     _#_#___|__|___#_#__
    [__________________]
     |-_ -=__=-_ -==_-|
     |_.------------.=|
     |=| o        o |=|
    _|-| !   `(   ! |-|_
   /==_| ! _(_.)_ ! |=_-|
   |   |/^\^=^^=^/^\| _=|
   """)
            time.sleep(2)
            print("How do you wish to proceed?")
            time.sleep(1)
            response = input("Look More![1], Stop Looking[2] ")
            if response == "1": 
                print("You look further into the fire...suddenly a woman's face appears from the fire laughing")
                time.sleep(2)
                print("The fire explodes! causing severe burning that you can never recover from.")
                gameover() 
            elif response == "2": 
                print("You decide to ignore the seduction of the flames.")
                living_room() 
            else: 
                print("Sorry, that choice is not recognised, please try again.")
                living_room() 
    elif response == "3": 
        print("You exit the room and go back to the hallway.")
        hallway()
    else:
        print("Sorry, that choice is not recognised, please try again.")
        living_room()     
    

def loft():
    print("""You enter the loft.
It’s a derelict space, chopped wooden flooring and a single
window where the moon light pierces through. """)
    time.sleep(2)
    print("""
Hanging from the ceiling you see a
noose limping left to right.""")
    time.sleep(2)
    print("""
All of a sudden a ghastly woman appears before
you! Wailing and moaning for you to leave!""")
    time.sleep(2)
    print("""Casper: Quickly give her the items you've picked up from the house!""")
    time.sleep(2)
    print("""The ghost lady stops in her tracks and observes the items laid before her.""")
    time.sleep(2)
    print("She feels at peace...and her soul slowly vanishes….""")
    time.sleep(2)
    print("""  

(`\ .-') /` ('-. .-.                                                                                               
`.( OO ),'( OO )  /                                                                                               
,--./  .--.  ,--. ,--. .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----.     
|      |  |  |  | |  |( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '    
|  |   |  |, |   .|  |/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |    
|  |.'.|  |_)|       |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |    
|         |  |  .-.  |  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |    
|   ,'.   |  |  | |  |   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '    
'--'   '--'  `--' `--'     `-----'      `-----'      `-----'      `-----'      `-----'      `-----'      `-----'     
""")
    time.sleep(1)
    print("""
 .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----. 
( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '
/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |
\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |
  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |
   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '
     `-----'      `-----'      `-----'      `-----'      `-----'      `-----'      `-----'      `-----'      `-----' 
     """)
    time.sleep(1)
    print("""
 .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----.  .-'),-----. 
( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '( OO'  .-.  '
/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |/   |  | |  |
\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |\_) |  |\|  |
  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |  \ |  | |  |
   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '   `'  '-'  '
     `-----'      `-----'      `-----'      `-----'      `-----'      `-----'      `-----'      `-----'      `-----' 
     """)
    time.sleep(2)
    print("""
  .-')    ('-. .-. ('-. .-. ('-. .-. ('-. .-. ('-. .-. ('-. .-. ('-. .-. ('-. .-.                                    
 ( OO ). ( OO )  /( OO )  /( OO )  /( OO )  /( OO )  /( OO )  /( OO )  /( OO )  /                                    
(_)---\_),--. ,--.,--. ,--.,--. ,--.,--. ,--.,--. ,--.,--. ,--.,--. ,--.,--. ,--.                                    
/    _ | |  | |  ||  | |  ||  | |  ||  | |  ||  | |  ||  | |  ||  | |  ||  | |  |                                    
\  :` `. |   .|  ||   .|  ||   .|  ||   .|  ||   .|  ||   .|  ||   .|  ||   .|  |                                    
 '..`''.)|       ||       ||       ||       ||       ||       ||       ||       |                                    
.-._)   \|  .-.  ||  .-.  ||  .-.  ||  .-.  ||  .-.  ||  .-.  ||  .-.  ||  .-.  |                                    
\       /|  | |  ||  | |  ||  | |  ||  | |  ||  | |  ||  | |  ||  | |  ||  | |  |                                    
 `-----' `--' `--'`--' `--'`--' `--'`--' `--'`--' `--'`--' `--'`--' `--'`--' `--'     """)
    time.sleep(2)
    print("""She is making her way to the afterlife! You did
it! She’s gone!""")
    time.sleep(2)

    print("Congrats! you've done it")
    winner()

    

def gameover():
    global drunk
    global wine_bottle
    global cellar_key
    global Necklace
    global items
    global kitchen_options
    global living_choice
    global eviction_notice
    eviction_notice = False
    living_choice = ["Inspect candlestick[1]", "Gaze into the fire[2]", "Exit room [3]"]
    kitchen_options = ["Pick up a bottle of wine[1]","pick up the photo[2]","back to the hallway[3]"]
    drunk = False 
    wine_bottle = False
    cellar_key = False
    Necklace = False
    items = 0 
    print("""
                 
                 uuuuuuu
             uu$$$$$$$$$$$uu
          uu$$$$$$$$$$$$$$$$$uu
         u$$$$$$$$$$$$$$$$$$$$$u
        u$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$$$$$$$$$$$$$$$$$$$$u
       u$$$$$$"   "$$$"   "$$$$$$u
       "$$$$"      u$u       $$$$"
        $$$u       u$u       u$$$
        $$$u      u$$$u      u$$$
         "$$$$uu$$$   $$$uu$$$$"
          "$$$$$$$"   "$$$$$$$"
            u$$$$$$$u$$$$$$$u
             u$"$"$"$"$"$"$u
             $$u$ $ $ $ $u$$      
              $$$$$u$u$u$$$      
               "$$$$$$$$$"          
                  ......                      
     
     """)
    print("Would you like to play again?")
    play_again = input("Yes[y],No[n]")
    if play_again.lower() == "y":
        startgame()

    elif play_again.lower() == "n":
        print("Thank you for playing")
        
    else:
        print("invalid input")
        gameover()
      
def winner():
    global drunk
    global wine_bottle
    global cellar_key
    global Necklace
    global items
    global kitchen_options
    global living_choice 
    global eviction_notice
    eviction_notice = False
    living_choice = ["Inspect candlestick[1]", "Gaze into the fire[2]", "Exit room [3]"]
    kitchen_options = ["Pick up a bottle of wine[1]","pick up the photo[2]","back to the hallway[3]"]
    drunk = False 
    wine_bottle = False
    cellar_key = False
    Necklace = False
    items = 0 
    
    print("Would you like to play again?")
    play_again = input("Yes[y],No[n]")
    if play_again.lower() == "y":
        startgame()

    elif play_again.lower() == "n":
        print("Thank you for playing")
        pass
        
    else:
        print("invalid input")
        winner()
  
  
hallway()