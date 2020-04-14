from guizero import *
import random


#player names
player_name_list = []

#whos turn it is 
current_player = []

#stores piece positions of the players piece to compare for win check
player1_pieces= []
player2_pieces= []


#creates players 1 and 2
    #class
class player(object):
    def __init__(self, name, turn):
        self.name = name
        self.turn = turn
   #players    
player1 =player("Player1" ,1)
player2 = player("Player2",2)


#assigns names randomly to player 1 and 2
def _assign_names():
    current_player.clear()
    player_name_list.append(player_name1.value)
    player_name_list.append(player_name2.value)
    player1.name = random.choice(player_name_list)
    player_name_list.remove(player1.name)
    player2.name = player_name_list[0]
    

#Starts game displays board
def _start_game():
    if player_name1.value == "":
        error.visible = True
    elif player_name2.value == "":
        error.visible = True
    else:
        error.visible = False
        _assign_names()
        app.hide()
        current_player.append(player1)
        player_turn.value = player1.name + "\'s Turn "
        game.show()


#shows intructions
def _show_instruct():
    app.hide()
    instruct.show()

#closes the instructions
def _close_instruct():
    instruct.hide()
    app.show()


#ramtch button command
def _rematch():
    player_name_list.clear()
    player1_pieces.clear()
    player2_pieces.clear()
    _assign_names()
    current_player.append(player1)
    player_turn.value = player1.name + "\'s Turn "
    
    for i in range(9): 
        pieces = Game_button_list[int(i)]
        pieces.text = "X/O"
        pieces.enabled = True
        i=i+1
    

#returns to title screen and resets board
def _main_menu():
    player_name1.value = ""
    player_name2.value = ""
    player_name_list.clear()
    player1_pieces.clear()
    player2_pieces.clear()
    
    for i in range(9): 
        pieces = Game_button_list[int(i)]
        pieces.text = "X/O"
        pieces.enabled = True
        i=i+1
    
    game.hide()
    app.show()
 
 
#check for winner 
def _win_check():
    wins_list = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    new_list = wins_list
     
    for i,j,k, in wins_list:
        if  i in player1_pieces and j in player1_pieces and k in player1_pieces: 
            for i in range(9): 
                pieces = Game_button_list[int(i)]
                pieces.text = "X/O"
                pieces.enabled = False
                i=i+1
            player_turn.value = player1.name + " Wins!!"
            return
        elif i in player2_pieces and j in player2_pieces and k in player2_pieces:
            for i in range(9): 
                pieces = Game_button_list[int(i)]
                pieces.text = "X/O"
                pieces.enabled = False
                i=i+1
            player_turn.value = player2.name + " Wins!!"
        

#plays x or o on board
def _set_piece(z):
    i = int(z)
    piece_pos = i
    # piece_position
    piece = Game_button_list[int(z)]
    
    if player1 in current_player:
        piece.text = "X"
        player1_pieces.append(piece_pos)
        current_player.append(player2)
        current_player.remove(player1)
        player_turn.value = player2.name + "\'s Turn "
    elif player2 in current_player:
        piece.text = "O"
        player2_pieces.append(piece_pos)
        current_player.append(player1)
        current_player.remove(player2)
        player_turn.value = player1.name + "\'s Turn "
        
    piece.enabled = False
    _win_check()
       
    
#title screen window
app = App(title = "Tic Tac Toe", bg = "light blue", width = 600, height = 600, layout = "auto")
headline = Text(app, text= "Tic Tac Toe!!!", color = "red", size = 40, align = "top")
instructions_button = PushButton(app, text ="Instuctions", command = _show_instruct)
box_label1 = Text(app, text= "Player Names", color = "green", size = 35, align = "top")
player_name1 = TextBox(app, text = "")
player_name1.bg = "white"
box_label2 = Text(app, text= "VS.", color = "green", size = 40, align = "top")
player_name2 = TextBox(app, text = "")
player_name2.bg = "white"
start_game_button = PushButton(app, text ="Start Game", command = _start_game)
error = Text(app, text= "ENTER PLAYER NAMES!", color = "red", size = 35, align = "top", visible = False)


#instrutcions window
instruct = Window(app, title = "Tic Tac Toe", bg = "light blue", width = 600, height = 600)
headline = Text(instruct, text = "Instructions", color = "red", size = 40)
line1 = Text(instruct, text = "1) Enter player names and press start game.", color = "dark green", size = 20)
line2 = Text(instruct, text = "2) First player will be randomly selected.", color = "dark green", size = 20)
line3 = Text(instruct, text = "3) First player clicks on a chosen square.", color = "dark green", size = 20)
line4 = Text(instruct, text = "4) Repeat for player 2.", color = "dark green", size = 20)
line5 = Text(instruct, text = "5) First to get 3 matching squares wins.", color = "dark green", size = 20)
line6 = Text(instruct, text = "6) Wins are 3 in a column, row, or angle.", color = "dark green", size = 20)
line7 = Text(instruct, text = "7) Click \"Main Menu\" to return to title screen.", color = "dark green", size = 20)
line8 = Text(instruct, text = "8) Click \"Rematch\" to play again.", color = "dark green", size = 20)
close_window_button = PushButton(instruct, text ="Close", command = _close_instruct)
instruct.hide()


#game window
game = Window(app, title = "Tic Tac Toe", bg = "light blue", width = 600, height = 600)
headline = Text(game, text = "2 Players!!!", color = "dark green", size = 40)
main_menu_button = PushButton(game, text = "Main Menu", command = _main_menu)
play_area = Box(game, width = 300, height = 300, layout = "grid")
play_area.bg = "grey"
#generate board buttons
Game_button_list = [] 
z = 0
for x in range(3):
    for y in range (0,3):
        Game_button_list.append(PushButton(play_area, text = "X/O", grid = [x,y], args = str(z), width = 9, height = 5, enabled = True, command = _set_piece))
        z+=1
player_turn = Text(game, text = "", color = "dark green", size = 40)
rematch_button = PushButton(game, text = "Rematch", command = _rematch)
game.hide()


#start program
app.display()
