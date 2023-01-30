import pyxel, random

# taille de la fenetre 512x512 pixels
# ne pas modifier
pyxel.init(512, 512)

x = 249
y = 400
w = 16
h = 32
ennemis_liste_up = []
ennemis_liste_left = []

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

def ennemis_creation_up(ennemis_liste_up):
    """création aléatoire des ennemis"""
    # un ennemi par seconde
    if (pyxel.frame_count % 30 == 0):
        ennemis_liste_up.append([random.randint(0, 480), 0])
    return ennemis_liste_up

def ennemis_creation_left(ennemis_liste_left):
    """création aléatoire des ennemis"""
    # un ennemi par seconde
    if (pyxel.frame_count % 30 == 0):
        ennemis_liste_left.append([0, random.randint(0, 480)])
    return ennemis_liste_left

def ennemis_deplacement_up(ennemis_liste_up):
    """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""
    for ennemi in ennemis_liste_up:
        ennemi[1] += 6
        if  ennemi[1]>512:
            ennemis_liste_up.remove(ennemi)
    return ennemis_liste_up
    
def ennemis_deplacement_left(ennemis_liste_left):
    """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""
    for ennemi in ennemis_liste_left:
        ennemi[0] += 6
        if  ennemi[0]>512:
            ennemis_liste_left.remove(ennemi)
    return ennemis_liste_left
    
# =========================================================
# == UPDATE
# =========================================================
def update():
# flèches interactives
    global x,y,ennemis_liste_up,ennemis_liste_left
    x, y = personnage_deplacement(x, y)
    ennemis_liste_up = ennemis_creation_up(ennemis_liste_up)
    ennemis_liste_left = ennemis_creation_left(ennemis_liste_left)
    ennemis_liste_up = ennemis_deplacement_up(ennemis_liste_up)
    ennemis_liste_left = ennemis_deplacement_left(ennemis_liste_left)    
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    global x,y,ennemis_liste,ennemis_liste_left
    
    # vide la fenetre
    pyxel.cls(0)
    
    # dessiner le reste:
    # backgrounds
    pyxel.rect(0,0,512,512,7)
    pyxel.rect(x , y , w , h, 8)
    for ennemi in ennemis_liste_up:
        pyxel.blt(ennemi[0], ennemi[1], 0, 0, 32, 32, 6)
    for ennemi in ennemis_liste_left:
        pyxel.blt(ennemi[0], ennemi[1], 0, 0, 32, 32, 6)
    
pyxel.run(update,draw)
