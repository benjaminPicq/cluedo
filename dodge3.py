import pyxel, random

# taille de la fenetre 512x512 pixels
# ne pas modifier
pyxel.init(512, 512)
"""pyxel.load("images,.pyxres")"""

x = 249
y = 400
w = 16
h = 32
ennemis_liste_up = []
ennemis_liste_left = []
score = 0

def personnage_deplacement(x, y):
    """déplacement avec les touches de directions"""
    if pyxel.btn(pyxel.KEY_RIGHT):
        if (x < 512-w):
            x = x+4
    if pyxel.btn(pyxel.KEY_LEFT):
        if (x > 0):
            x = x-4
    if pyxel.btn(pyxel.KEY_UP):
        if (y > 0):
            y = y-4
    if pyxel.btn(pyxel.KEY_DOWN):
        if (y < 512-h):
            y = y+4

    return x, y

def ennemis_creation(ennemis_liste, direction): #direction 0 = left et direction 1 = up
    """création aléatoire des ennemis"""
    # un ennemi par seconde
    if (pyxel.frame_count % 30 == 0):
        if direction == 1:
            ennemis_liste.append([random.randint(0, 480), 0])
        else:
            ennemis_liste.append([0, random.randint(0, 480)])
    return ennemis_liste

def ennemis_deplacement(ennemis_liste, direction):
    """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""
    for ennemi in ennemis_liste:
        ennemi[direction] += 6
        if  ennemi[direction]>512:
            ennemis_liste.remove(ennemi)
    return ennemis_liste
    
def score_timer(score):
    """augmente le score au fur et a mesure du temps"""
    if 127 < 128:
        score += 1
    return score
    
# =========================================================
# == UPDATE
# =========================================================
def update():
# flèches interactives
    global x,y,ennemis_liste_up,ennemis_liste_left,score
    x, y = personnage_deplacement(x, y)
    ennemis_liste_up = ennemis_creation(ennemis_liste_up, 1)
    ennemis_liste_left = ennemis_creation(ennemis_liste_left, 0)
    ennemis_liste_up = ennemis_deplacement(ennemis_liste_up, 1)
    ennemis_liste_left = ennemis_deplacement(ennemis_liste_left, 0)
    score = score_timer(score)
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    global x,y,ennemis_liste,ennemis_liste_left,score
    # vide la fenetre
    pyxel.cls(0)
    pyxel.rect(0,0,512,512,7)     

  
    # dessiner le reste:
    pyxel.text(350, 400, f"score: {score}", 6)
    # backgrounds

    pyxel.rect(x , y , w , h, 8)
    for ennemi in ennemis_liste_up:
        pyxel.blt(ennemi[0], ennemi[1], 0, 0, 32, 32, 32)
    for ennemi in ennemis_liste_left:
        pyxel.blt(ennemi[0], ennemi[1], 0, 0, 32, 32, 32)
    
pyxel.run(update,draw)
