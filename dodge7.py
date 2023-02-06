import pyxel, random

# taille de la fenetre 256x256 pixels
# ne pas modifier
pyxel.init(256, 256)
"""pyxel.load("images,.pyxres")"""

x = 124
y = 200
w = 8
h = 16
ennemis_liste_up = []
ennemis_liste_left = []
score = 0
vie = 3
game = True

def personnage_deplacement(x, y):
    """déplacement avec les touches de directions"""
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 256-w):
            x = x+2
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0):
            x = x-2
    if pyxel.btn(pyxel.KEY_UP):
        if (y > 0):
            y = y-2
    if pyxel.btn(pyxel.KEY_DOWN):
        if (y < 256-h):
            y = y+2

    return x, y

def ennemis_creation(ennemis_liste, direction): #direction 0 = left et direction 1 = up
    """création aléatoire des ennemis"""
    # un ennemi par seconde
    if (pyxel.frame_count % 30 == 0):
        if direction == 1:
            ennemis_liste.append([random.randint(0, 240), 0])
        else:
            ennemis_liste.append([0, random.randint(0, 240)])
    return ennemis_liste

def ennemis_deplacement(ennemis_liste, direction):
    """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""
    for ennemi in ennemis_liste:
        ennemi[direction] += 3
        if  ennemi[direction]>256:
            ennemis_liste.remove(ennemi)
    return ennemis_liste

def score_timer(score):
    """augmente le score au fur et a mesure du temps"""
    if 127 < 128:
        score += 1
    return score

def lose(game):
    global vie
    if vie == 0:
        game = False
    return game
    
# =========================================================
# == UPDATE
# =========================================================
def update():
# flèches interactives
    global x,y,ennemis_liste_up,ennemis_liste_left,score,game,vie
    x, y = personnage_deplacement(x, y)
    ennemis_liste_up = ennemis_creation(ennemis_liste_up, 1)
    ennemis_liste_left = ennemis_creation(ennemis_liste_left, 0)
    ennemis_liste_up = ennemis_deplacement(ennemis_liste_up, 1)
    ennemis_liste_left = ennemis_deplacement(ennemis_liste_left, 0)
    score = score_timer(score)
    game = lose(game)
    
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    global x,y,ennemis_liste,ennemis_liste_left,score
    # vide la fenetre
    pyxel.cls(0)
    pyxel.rect(0,0,256,256,7)     

  
    # dessiner le reste:
    pyxel.text(175, 200, f"score: {score}", 6)
    # backgrounds

    pyxel.rect(x , y , w , h, 8)
    for ennemi in ennemis_liste_up:
        pyxel.blt(ennemi[0], ennemi[1], 0, 0, 16, 16, 16)
    for ennemi in ennemis_liste_left:
        pyxel.blt(ennemi[0], ennemi[1], 0, 0, 16, 16, 16)
    
    if game == False:
        pyxel.cls(7)
        pyxel.text(110, 128, "Game Over", 0)
pyxel.run(update,draw)
