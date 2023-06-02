#Emile Macabies 2023
#TP5

#Importations
import arcade
import random
import game_state
import arcade.gui

#Importations des classes
from attack_animation import AttackType, AttackAnimation

#Constantes
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Roche, papier, ciseaux"
DEFAULT_LINE_HEIGHT = 45

#Classe principale
class MyGame(arcade.Window):

    #Constantes
   PLAYER_IMAGE_X = (SCREEN_WIDTH / 2) - (SCREEN_WIDTH / 4)
   PLAYER_IMAGE_Y = SCREEN_HEIGHT - 300
   COMPUTER_IMAGE_X = (SCREEN_WIDTH / 2) * 1.5
   COMPUTER_IMAGE_Y = SCREEN_HEIGHT - 300
   ATTACK_FRAME_WIDTH = 154 / 2
   ATTACK_FRAME_HEIGHT = 154 / 2

   #Classe pour creer toutes les variables du jeu
   def __init__(self, width, height, title):
       super().__init__(width, height, title)

       arcade.set_background_color(arcade.color.BLACK)

       self.player = None
       self.computer = None
       self.players = None
       self.rock = None
       self.paper = None
       self.scissors = None
       self.player_score = 0
       self.computer_score = 0
       self.player_attack_type = {}
       self.computer_attack_type = None
       self.player_attack_chosen = False
       self.player_won_round = None
       self.computer_won_round = None
       self.draw_round = None
       self.game_state = game_state.GameState.NOT_STARTED

   #Fonction pour afficher les textes
   def setup(self):



       #Créer les sprites pour le joueur et l'ordinateur
       self.player = arcade.Sprite("assets/faceBeard.png", 0.5)
       self.player.center_x = self.PLAYER_IMAGE_X
       self.player.center_y = self.PLAYER_IMAGE_Y
       self.computer = arcade.Sprite("assets/compy.png", 0.5)
       self.computer.center_x = self.COMPUTER_IMAGE_X
       self.computer.center_y = self.COMPUTER_IMAGE_Y
       self.players = arcade.SpriteList()
       self.players.append(self.player)
       self.players.append(self.computer)

       # Créer les sprites pour les attaques du joueur
       self.rock = AttackAnimation('assets/srock.png', 0.5)
       self.rock.center_x = self.PLAYER_IMAGE_X
       self.rock.center_y = self.PLAYER_IMAGE_Y

       self.paper = AttackAnimation("assets/spaper.png", 0.5)
       self.paper.center_x = self.PLAYER_IMAGE_X
       self.paper.center_y = self.PLAYER_IMAGE_Y

       self.scissors = AttackAnimation("assets/scissors.png", 0.5)
       self.scissors.center_x = self.PLAYER_IMAGE_X
       self.scissors.center_y = self.PLAYER_IMAGE_Y

       # Créer les sprites pour les attaques de l'ordinateur
       self.computer.scissors = AttackAnimation("assets/scissors.png", 0.5)
       self.computer.scissors.center_x = self.COMPUTER_IMAGE_X
       self.computer.scissors.center_y = self.COMPUTER_IMAGE_Y

       self.computer.paper = AttackAnimation("assets/spaper.png", 0.5)
       self.computer.paper.center_x = self.COMPUTER_IMAGE_X
       self.computer.paper.center_y = self.COMPUTER_IMAGE_Y

       self.computer.rock = AttackAnimation('assets/srock.png', 0.5)
       self.computer.rock.center_x = self.COMPUTER_IMAGE_X
       self.computer.rock.center_y = self.COMPUTER_IMAGE_Y

       # Créer les dictionnaires pour les attaques
       self.player_attack_type = {AttackType.ROCK: self.rock,
                                          AttackType.PAPER: self.paper,
                                        AttackType.SCISSORS: self.scissors}
       self.computer_attack_type = random.randint(1, 3)

       # Créer les variables pour les scores
       self.player_score = 0
       self.computer_score = 0

       # Créer les variables pour les états de jeu
       self.player_attack_chosen = False
       self.player_won_round = None
       self.draw_round = False
       self.game_state = game_state.GameState.NOT_STARTED

#Fonction pour detecter qui a gagné
   def validate_victory(self):
        if game_state == game_state.GameState.ROUND_ACTIVE:
            if self.player_attack_chosen == True and self.computer_attack_type != None:
                if self.player_attack_type == self.computer_attack_type:
                    pass
                elif self.player_attack_type == AttackType.ROCK and self.computer_attack_type == AttackType.SCISSORS:
                    self.player_score += 1
                elif self.player_attack_type == AttackType.PAPER and self.computer_attack_type == AttackType.ROCK:
                    self.player_score += 1
                elif self.player_attack_type == AttackType.SCISSORS and self.computer_attack_type == AttackType.PAPER:
                    self.player_score += 1
                else:
                    self.computer_score += 1



#Fonction pour ajuster les scores
        if self.player_won_round == True:
           self.player_score = + 1
           arcade.draw_text("Player wins the round", 111, 111, arcade.color.GREEN, 30, width=SCREEN_WIDTH, align="center")

        elif self.computer_won_round == True:
           self.computer_score = + 1
           arcade.draw_text("Computer wins the round", 111, 111, arcade.color.GREEN, 30, width=SCREEN_WIDTH, align="center")

        elif self.draw_round == True:
           pass
           arcade.draw_text("Draw!", 111, 111, arcade.color.GREEN, 30, width=SCREEN_WIDTH, align="center")

#Fonction pour dessiner les attaques possibles du joueur
   def draw_possible_attack(self):

#Dessiner les carres des attaques
       arcade.draw_rectangle_outline(self.PLAYER_IMAGE_X, self.PLAYER_IMAGE_Y - 150, self.ATTACK_FRAME_WIDTH, self.ATTACK_FRAME_HEIGHT, arcade.color.GREEN, 5)

       arcade.draw_rectangle_outline(self.PLAYER_IMAGE_X + 100, self.PLAYER_IMAGE_Y - 150, self.ATTACK_FRAME_WIDTH, self.ATTACK_FRAME_HEIGHT, arcade.color.GREEN, 5)

       arcade.draw_rectangle_outline(self.PLAYER_IMAGE_X - 100, self.PLAYER_IMAGE_Y - 150, self.ATTACK_FRAME_WIDTH, self.ATTACK_FRAME_HEIGHT, arcade.color.GREEN, 5)

#Dessiner les attaques
       if self.player_attack_chosen == False and self.game_state == game_state.GameState.ROUND_ACTIVE:
           self.rock.center_x = self.player.center_x - 100
           self.rock.center_y = 150
           self.rock.draw()

           self.paper.center_x = self.player.center_x
           self.paper.center_y = 150
           self.paper.draw()

           self.scissors.center_x = self.player.center_x + 100
           self.scissors.center_y = 150
           self.scissors.draw()

#Fonction pour dessiner l'attaques du joueur si il a choisi une attaque et que le jeu est en cours
       if self.player_attack_chosen == True and self.game_state == game_state.GameState.ROUND_ACTIVE:
           if self.player_attack_type == AttackType.ROCK and self.player_attack_chosen == True and self.game_state == game_state.GameState.ROUND_ACTIVE:
               self.rock.center_x = self.player.center_x - 100
               self.rock.center_y = 150
               self.rock.draw()

           elif self.player_attack_type == AttackType.PAPER and self.player_attack_chosen == True and self.game_state == game_state.GameState.ROUND_ACTIVE:
               self.paper.center_x = self.player.center_x
               self.paper.center_y = 150
               self.paper.draw()

           elif self.player_attack_type == AttackType.SCISSORS and self.player_attack_chosen == True and self.game_state == game_state.GameState.ROUND_ACTIVE:
               self.scissors.center_x = self.player.center_x + 100
               self.scissors.center_y = 150
               self.scissors.draw()


#Fonction pour dessiner l'attaque de l'ordinateur
   def draw_computer_attack(self):

#Dessiner le carre de l'attaque de l'ordinateur
       arcade.draw_rectangle_outline(self.COMPUTER_IMAGE_X, self.COMPUTER_IMAGE_Y - 150, self.ATTACK_FRAME_WIDTH, self.ATTACK_FRAME_HEIGHT, arcade.color.GREEN, 5)

#choisir au hasard une attaque de l'ordinateur
       self.computer_attack_type = random.randint(1, 3)

#Dessiner l'attaque de l'ordinateur
       if self.computer_attack_type == 1 and self.player_attack_chosen == True:
           self.computer.rock.center_x = self.computer.center_x
           self.computer.rock.center_y = 150
           self.computer_attack_type = self.computer.rock
           self.computer.rock.draw()

       elif self.computer_attack_type == 2 and self.player_attack_chosen == True:
           self.computer.paper.center_x = self.computer.center_x
           self.computer.paper.center_y = 150
           self.computer_attack_type = self.computer.paper
           self.computer.paper.draw()

       elif self.computer_attack_type == 3 and self.player_attack_chosen == True:
           self.computer.scissors.center_x = self.computer.center_x
           self.computer.scissors.center_y = 150
           self.computer_attack_type = self.computer.scissors
           self.computer.scissors.draw()

#Fonction pour dessiner les scores
   def draw_scores(self):

       arcade.draw_text("Player: " + str(self.player_score), -250, SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4.5, arcade.color.GREEN, 30, width=SCREEN_WIDTH, align="center")
       arcade.draw_text("Computer: " + str(self.computer_score), 250, SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 4.5, arcade.color.GREEN, 30, width=SCREEN_WIDTH, align="center")

#Fonction pour dessiner les instructions selon letat du jeu
   def draw_instructions(self):

       if self.game_state == game_state.GameState.NOT_STARTED:
           arcade.draw_text("Press 'SPACE' to start the game", 0, 40, arcade.color.GREEN, 30, width=SCREEN_WIDTH, align="center")

       elif self.game_state == game_state.GameState.ROUND_ACTIVE:

           arcade.draw_text("Use 'LEFT CLICK' on an attack to use it", 0, 40, arcade.color.GREEN, 30, width=SCREEN_WIDTH, align="center")

       elif self.game_state == game_state.GameState.ROUND_DONE:
           arcade.draw_text("Press 'SPACE' to continue the game", 0, 40, arcade.color.GREEN, 30,
                            width=SCREEN_WIDTH, align="center")

       elif self.game_state == game_state.GameState.GAME_OVER:
           arcade.draw_text("Press 'SPACE' to start a new game", 0, 40, arcade.color.GREEN, 30,
                            width=SCREEN_WIDTH, align="center")

#fonction pour dessiner le jeu
   def on_draw(self):

       arcade.start_render()

#Display title
       arcade.draw_text(SCREEN_TITLE,
                        0,
                        SCREEN_HEIGHT - DEFAULT_LINE_HEIGHT * 2,
                        arcade.color.GREEN,
                        60,
                        width=SCREEN_WIDTH,
                        align="center")

       self.draw_instructions()
       self.players.draw()
       self.draw_possible_attack()
       self.draw_scores()
       self.draw_computer_attack()

#Fonction valider la victoire
       self.validate_victory()

   def on_update(self, delta_time):

       #vérifier si le jeu est actif (ROUND_ACTIVE) et continuer l'animation des attaques



       #changer l'état de jeu si nécessaire (GAME_OVER)
       pass

#detecter si le joueur a cliqué sur espace changer l'état du jeu
   def on_key_press(self, key, modifiers):

       if (self.game_state == game_state.GameState.NOT_STARTED and key == arcade.key.SPACE):
           self.game_state = game_state.GameState.ROUND_ACTIVE

       elif (self.game_state == game_state.GameState.ROUND_DONE and key == arcade.key.SPACE):
           self.game_state = game_state.GameState.ROUND_ACTIVE

       elif (self.game_state == game_state.GameState.GAME_OVER and key == arcade.key.SPACE):
           self.game_state = game_state.GameState.ROUND_ACTIVE
           #pts a zero


   #reset la ronde
   def reset_round(self):

       #self.computer_attack_type = -1
       #self.player_attack_chosen = False
       #self.player_attack_type = {AttackType.ROCK: False, AttackType.PAPER: False, AttackType.SCISSORS: False}
       #self.player_won_round = False
       #self.draw_round = False

       pass

# detecter si le joueur a cliqué sur une attaque
   def on_mouse_press(self, x, y, button, key_modifiers):

       if self.game_state == game_state.GameState.ROUND_ACTIVE:
           if self.rock.collides_with_point((x, y)):
               self.player_attack_type = AttackType.ROCK
               self.player_attack_chosen = True
           elif self.paper.collides_with_point((x, y)):
               self.player_attack_type = AttackType.PAPER
               self.player_attack_chosen = True
           elif self.scissors.collides_with_point((x, y)):
               self.player_attack_type = AttackType.SCISSORS
               self.player_attack_chosen = True

#faire partir le jeu
def main():
   game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
   game.setup()
   arcade.run()

#lancer le jeu
if __name__ == "__main__":
   main()