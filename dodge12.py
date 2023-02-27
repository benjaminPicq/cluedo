import pyxel, random
#www.pyxelstudio.net/qwklx584

# taille de la fenetre 256x256 pixels
# ne pas modifier
pyxel.init(256, 256)
pyxel.load("res.pyxres")

personnage_x = 124
personnage_y = 200
w = 16
h = 16
ennemis_liste_up = []
ennemis_liste_left = []
score = 0
vies = 3
game = True
transparent_colour = 7

def personnage_deplacement(x, y):
    """déplacement avec les touches de directions"""
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 256-w+2):
            x = x+2
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > -2):
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
    if vies>0:
        score += 1
    return score

def lose(game):
    global vies
    if vies == 0:
        game = False
    return game
    
def collisions_left(ennemis_liste, vies):
    for ennemi in ennemis_liste:
        if ((personnage_x + w) >= (ennemi[0] + w) >= personnage_x) and ((personnage_y + h) >= (ennemi[1] + (w/2)) >= personnage_y):
            ennemis_liste.remove(ennemi)
            vies = vies -1
    return ennemis_liste, vies
    
# =========================================================
# == UPDATE
# =========================================================
def update():
# flèches interactives
    global personnage_x,personnage_y,ennemis_liste_up,ennemis_liste_left,score,game,vies
    personnage_x, personnage_y = personnage_deplacement(personnage_x, personnage_y)
    ennemis_liste_up = ennemis_creation(ennemis_liste_up, 1)
    ennemis_liste_left = ennemis_creation(ennemis_liste_left, 0)
    ennemis_liste_up = ennemis_deplacement(ennemis_liste_up, 1)
    ennemis_liste_left = ennemis_deplacement(ennemis_liste_left, 0)
    score = score_timer(score)
    game = lose(game)
    ennemis_liste_left, vies = collisions_left(ennemis_liste_left, vies)
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    global personnage_x,personnage_y,ennemis_liste,ennemis_liste_left,score,vies
    # vide la fenetre
    pyxel.cls(0)     
    # backgrounds
    pyxel.bltm(0,0,0,0,0,255,255)

    pyxel.text(175, 200, f"score: {score}", 6)
  
    # dessiner le reste:
    pyxel.blt(personnage_x, personnage_y, 0, 0, 0, 16, 16, transparent_colour)
    
    for ennemi in ennemis_liste_up:
        pyxel.blt(ennemi[0], ennemi[1], 0, 0, 48, 8, 16, 7)
    for ennemi in ennemis_liste_left:
        pyxel.blt(ennemi[0], ennemi[1], 0, 0, 48, 16, 8, 7)
    
    if game == False:
        pyxel.cls(7)
        pyxel.text(110, 128, "Game Over", 0)
pyxel.run(update,draw)
