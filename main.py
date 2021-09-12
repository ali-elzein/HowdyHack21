from tkinter import *
import pygame as pyg
import math
import pygame.display
import random

#tkinter root stuff that allows us to make the window
root_object = Tk()
root_object.title("Aggie Yell Music Player")
root_object.geometry("1000x1000")
pyg.mixer.init()

#this is where the words are added for each yell
yell_box = Listbox(root_object, bg = "maroon",font = ("Arial",12), fg = "white", width = 50, height = 30 )
yell_box.pack(pady = 20)

#This will hold our control menu
player_frame = Frame(root_object)
player_frame.pack()

#play and pause functions for control menu functions
def pause():
        pyg.mixer.music.pause()

def play():
    active_song = yell_box.get(ACTIVE)
    pyg.mixer.music.unpause()

#These are our control menu buttons
play_image = PhotoImage(file = 'Play.png')
play_button = Button(player_frame, image =play_image, borderwidth = 10, command = play)
play_button.grid(row = 0, column = 0, padx = 10, pady =10)

pause_image = PhotoImage(file = "Pause.png")
pause_button = Button(player_frame, image =pause_image, borderwidth = 10, command = pause)
pause_button.grid(row = 0, column = 1, padx = 10, pady = 10)

# this is where all of the yells will be listed
yell_frame = Frame(root_object)
yell_frame.pack()


# This function plays the audio file and calls function to print text on the screen.
def file_get(filename):
    file_path = filename + ".mp3"
    pyg.mixer.music.load(file_path)
    pyg.mixer.music.play(loops=0)
    print_text(filename)

#this prints text on the screen.
def print_text(yell_name):
    SizeVal = yell_box.size()
    yell_box.delete(0, SizeVal)
    for yell in texts.keys():
        if yell == yell_name:
            values = texts[yell]
    for i in range(len(values)):
        (yell_box.insert(i, values[i]))


#this dictionary allows us to get the text screen.
texts = {"OldArmy" : ["Aaaa, Rrrr, Mmmm, Yyyy(Drop voice)",
                    "Tttt, Aaaa, Mmmm, Cccc(Drop voice)",
                    "Aaaaaaaa",
                    "Ol’ Army fight!"],

         "Locomotive" : ["(slow) Rah! Rah! Rah! Rah!", "T-A-M-C", " ",
                         "(faster) Rah! Rah! Rah! Rah!", "T-A-M-C", " ",
                         "(very fast) Rah! Rah! Rah! Rah!", "T-A-M-C"," ",
                         "(Seniors only: “Whoop!”", "Aaaaaaa", "Rah! Rah! Rah! Team!"],

         "Farmer" : ["Farmers fight!",
                     "Farmers fight!",
                     "Fight! Fight!",
                     "Farmers, farmers fight!"],

        "FifteenForTeam" : ["Rah! Rah! Rah! Team!"],

         "Military" : ["Squads left! squads right!",
                       "Farmers, farmers, we’re all right!",
                       "Load, ready, aim, fire, BOOM!",
                       "(Seniors only: “Reload!”)",
                       "A&M, give us room!",
                       ],

         "WarHymn" : ["Hullabaloo, Caneck! Caneck!",
                        "Hullabaloo, Caneck! Caneck!",
                      "Good bye to texas university",
                      "So long to the orange and the white",
                      "Good luck to dear old Texas Aggies",
                      "They are the boys who show the real old fight",
                      "'the eyes of Texas are upon you'",
                      "That is the song they sing so well",
                      "Sounds Like Hell",
                      "So good bye to texas university",
                      "We're gonna beat you all to Chig-gar-roo-gar-rem",
                      "Chig-gar-roo-gar-rem",
                      "Rough, Tough, real stuff Texas A&M",
                      "Good bye to texas university",
                      "So long to the orange and the white",
                      "Good luck to dear old Texas Aggies",
                      "They are the boys who show the real old fight",
                      "'the eyes of Texas are upon you'",
                      "That is the song they sing so well",
                      "Sounds Like Hell",
                      "So good bye to texas university",
                      "We're gonna beat you all to Chig-gar-roo-gar-rem",
                      "Chig-gar-roo-gar-rem",
                      "Rough, Tough, real stuff Texas A&M",
                      "Saw varsity's horns off (x3)",
                      "Short! A!",
                      "Varsity's horns are sawed off (x3)",
                      "Short! A!"]}


def gamer():
    pyg.init()
    screen = pyg.display.set_mode((800,800))
    still_running = True
    pyg.display.set_caption("Yell Leaders Walk")
    icon = pyg.image.load('Play.png')
    pygame.display.set_icon(icon)

    def player(player_x, player_y):
        screen.blit(leader, (player_x, player_y))
        for i in range(3):
            screen.blit(t_u_icon, (icon_x[i], icon_y[i]))

    #kyleField
    kyleField = pyg.image.load("KyleField.png")

    #Yell Leader image
    leader = pyg.image.load("Yell.png")
    leader_x = 400
    leader_y = 700
    x_change = 0
    y_change = 0
    icon_x = []
    icon_y = []
    icon_change_x = []
    score = 0
    font = pyg.font.Font("freesansbold.ttf", 32)
    font2 = pyg.font.Font("freesansbold.ttf", 12)
    text_X = 10
    text_Y = 10

    def scorer(x, y):
        score_text = font.render("Score:" + str(score), True, (255, 255, 255))
        screen.blit(score_text, (x, y))

    for i in range(3):
        # texas university (hisssssssss) icon
        t_u_icon = pyg.image.load("tu.png")
        icon_x.append(random.randint(100, 400))
        icon_y.append(random.randint(10, 400))
        icon_change_x.append(random.randint(3, 10))

    #this checks for collision in the) game
    def is_Collision(leader_x, leader_y):
        for i in range(3):
            dist = math.sqrt(math.pow((icon_x[i] - leader_x), 2) + math.pow((icon_y[i] - leader_y), 2))
            if dist < 100:
                return True
            else:
                return False

    def win_Collision(leader_y):
        if leader_y < 60:
            return True
        else:
            return False

    while still_running:
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                    pygame.display.quit()
                    running = False

            if event.type == pyg.KEYDOWN:
                if event.key == pyg.K_LEFT:
                    x_change = -4
                if event.key == pyg.K_RIGHT:
                    x_change = 4
                if event.key == pyg.K_UP:
                    y_change = -4
                if event.key == pyg.K_DOWN:
                    y_change = 4
            if event.type == pyg.KEYUP:
                if (event.key == pyg.K_RIGHT):
                    x_change += -4
                if (event.key == pyg.K_LEFT):
                    x_change += 4
                if (event.key == pyg.K_UP) or (event.key == pyg.K_DOWN):
                    y_change = 0


        leader_x += x_change
        leader_y += y_change
        if leader_x <= 0:
            leader_x = 0
        if leader_x >= 700:
            leader_x = 700
        if leader_y <= 0:
            leader_y = 0
        if leader_y >= 700:
            leader_y = 700

        for i in range(3):
            icon_x[i] += icon_change_x[i]
            if icon_x[i] <= 0:
                icon_x[i] = 0
                icon_change_x[i]= random.randint(3, 10)
                icon_y[i] += 10
            if icon_x[i] >= 700:
                icon_x[i] = 700
                icon_y[i] += 10
                icon_change_x[i] = -random.randint(3, 10)

            if icon_y[i] >= 700:
                icon_y[i] = 700
        collision = is_Collision(leader_x, leader_y)
        if collision:
            for i in range(3):
                icon_x[i] = random.randint(10, 800)
                icon_y[i] = random.randint(50, 400)
            leader_y = 699
            leader_x = 10
        winner = win_Collision(leader_y)
        if winner:
            score += 1
            leader_y = 699
            leader_x = 300

        endgame = font2.render("Go Here To End Game", True, (255, 255, 255))


        screen.fill((80, 0, 0))
        screen.blit(kyleField, (0,0))
        player(leader_x, leader_y)
        scorer(text_X, text_Y)
        screen.blit(endgame, (670, 750))
        if math.sqrt(math.pow((700 - leader_x), 2) + math.pow((700 - leader_y), 2)) < 50:
            screen.blit(kyleField, (0, 0))
            failure = font.render("GAME OVER!!", True, (60, 0, 0))
            failure2 = font.render("Your final score is " + str(score), True, (60, 0, 0))
            failure3 = font.render("Hit X to Exit", True, (60, 0, 0))
            x_change = 10
            y_change = 10
            screen.blit(failure, (250, 400))
            screen.blit(failure2, (250, 450))
            screen.blit(failure3, (250, 500))

        pygame.display.update()



#Song Buttons, these are the buttons the user will use to play the music.
#this one doesn't have a song yet

old_army_button = Button(yell_frame, text= "Old Army", font = ("Arial"), command=lambda: file_get("OldArmy"))
old_army_button.grid(row = 0, column = 0, padx=10)

locomotive_button = Button(yell_frame, text= "Locomotive", font = ("Arial"), command=lambda: file_get("Locomotive"))
locomotive_button.grid(row = 0, column = 2, padx=10)

farmers_button = Button(yell_frame, text= "Farmer Fight", font = ("Arial"), command=lambda: file_get("Farmer"))
farmers_button.grid(row=1, column = 0, padx =10)

fifteen_for_team_button = Button(yell_frame, text= "Fifteen for Team", font = ("Arial"), command=lambda: file_get("FifteenForTeam"))
fifteen_for_team_button.grid(row = 1, column = 2, padx=10)

military_button = Button(yell_frame, text= "Military", font = ("Arial"), command=lambda: file_get("Military"))
military_button.grid(row=2, column = 0, padx =10)

war_hymn_button = Button(yell_frame, text= "War Hymn", font = ("Arial"), command=lambda: file_get("WarHymn"))
war_hymn_button.grid(row=2, column = 2, padx =10)

war_hymn_button = Button(yell_frame, text= "Yell Leader Game", font = ("Arial"), command=lambda: gamer())
war_hymn_button.grid(row=3, column = 1, padx =10)

# Create Menu
yell_menu = Menu(root_object)
root_object.config(menu = yell_menu)

root_object.mainloop()