import pyxel, random
#Pour jouer: www.pyxelstudio.net/qwklx584
#Pour edit: https://www.pyxelstudio.net/studio/4mp2f96v/eyJpdiI6InkyS3BESnE1R0V3REU3RHd4cWFDbHc9PSIsInZhbHVlIjoieUxRZUNjS3A4eEd2a2QvZklwQUR3QT09IiwibWFjIjoiZGYzYzg1NjQzZWJiNjZmY2QxOWI4NmEzNTJkODMwMWQwMmM0OTFmMDUyN2VjY2U1NDU3ZWQ2YTg4N2IwYWQ2YSIsInRhZyI6IiJ9

# taille de la fenetre 256x256 pixels
# ne pas modifier
pyxel.init(256, 256)
pyxel.load("res.pyxres")

personnage_x = 120
personnage_y = 120
w = 16
h = 16
ennemis_vitesse_1 = 4
ennemis_vitesse_2 = 2
ennemis_liste_up = []
ennemis_liste_left = []
ennemis_liste_down = []
ennemis_liste_right = []
score = 0
vies = 3
game = True
transparent_colour = 7
transparent_colour_hearts = 2
niveau = 1
coins_liste = []
hearts_liste = []



def score_timer(score):
    """augmente le score au fur et a mesure du temps"""
    if vies>0:
        if (pyxel.frame_count % 30 == 0):
            score += 1
    return score

def lose(game):
    global vies
    if vies <= 0:
        game = False
    return game
    
def niveau_compteur(niveau):
    if game == True:
        if score >= 100 and niveau == 1:
            niveau = niveau + 1
    return niveau    
    
    
    
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



def ennemis_creation(ennemis_liste, direction, sens): #direction 0 = left/right et direction 1 = up/down
    """création aléatoire des ennemis"""
    # un ennemi par seconde
    if (pyxel.frame_count % 30 == 0):
        if sens == 0:
            if direction == 1:
                ennemis_liste.append([random.randint(0, 240), -h])
            else:
                ennemis_liste.append([-w, random.randint(0, 240)])
        elif sens == 1:
            if direction == 1:
                ennemis_liste.append([random.randint(0, 240) + h, (256)])
            else:
                ennemis_liste.append([(256), random.randint(0, 240) + w])
    return ennemis_liste
def ennemis_deplacement(ennemis_liste, direction, sens): # sens 0 = left/up et sens 1 = right/down
    """déplacement des ennemis vers le haut et suppression s'ils sortent du cadre"""
    for ennemi in ennemis_liste:
        if sens == 0:
            if niveau == 1:
                ennemi[direction] += ennemis_vitesse_1
            elif niveau == 2:
                ennemi[direction] += ennemis_vitesse_2
            if  ennemi[direction]>256:
                ennemis_liste.remove(ennemi)
        elif sens == 1:
            if niveau == 1:
                ennemi[direction] -= ennemis_vitesse_1
            elif niveau == 2:
                ennemi[direction] -= ennemis_vitesse_2
            if  ennemi[direction]<0:
                ennemis_liste.remove(ennemi)
    return ennemis_liste



def collisions_left(ennemis_liste, vies):
    for ennemi in ennemis_liste:
        if ((personnage_x + w) >= (ennemi[0] + w) >= personnage_x) and ((personnage_y + h + (w/2)) >= (ennemi[1] + (w/2)) >= personnage_y):
            ennemis_liste.remove(ennemi)
            vies = vies -1
    return ennemis_liste, vies
def collisions_right(ennemis_liste, vies):
    for ennemi in ennemis_liste:
        if ((personnage_x + w) >= ennemi[0] >= personnage_x) and ((personnage_y + h + (w/2)) >= (ennemi[1] + (w/2)) >= personnage_y):
            ennemis_liste.remove(ennemi)
            vies = vies -1
    return ennemis_liste, vies  
def collisions_up(ennemis_liste, vies):
    for ennemi in ennemis_liste:
        if ((personnage_x + w + (w/2)) >= ennemi[0] + (w/2) >= personnage_x) and ((personnage_y + h) >= (ennemi[1] + h) >= personnage_y):
            ennemis_liste.remove(ennemi)
            vies = vies -1
    return ennemis_liste, vies
def collisions_down(ennemis_liste, vies):
    for ennemi in ennemis_liste:
        if ((personnage_x + w + (w/2)) >= (ennemi[0] + (w/2)) >= personnage_x) and ((personnage_y + h) >= ennemi[1] >= personnage_y):
            ennemis_liste.remove(ennemi)
            vies = vies -1
    return ennemis_liste, vies
    
    
def coins_creation(coins_liste):
    if len(coins_liste) < 1 :
        if (pyxel.frame_count % 150 == 0):
            coins_liste.append([random.randint(40,200), random.randint(40,200)])
    return coins_liste
def coins_collisions(coins_liste, score):
    for coins in coins_liste:
        if ((personnage_x + w) >= coins[0] >= personnage_x - w) and ((personnage_y + h) >= coins[1] >= personnage_y - h):
            coins_liste.remove(coins)
            score += 10
    return coins_liste, score
    
    
    
def hearts_creation(hearts_liste):
    if len(hearts_liste) < 1 :
        if (pyxel.frame_count % 1500 == 0):
            hearts_liste.append([random.randint(40,200), random.randint(40,200)])
    return hearts_liste
def hearts_collisions(hearts_liste, vies):
    for heart in hearts_liste:
        if ((personnage_x + w) >= heart[0] >= personnage_x - w) and ((personnage_y + h) >= heart[1] >= personnage_y - h):
            hearts_liste.remove(heart)
            if vies < 3:
                vies += 1
    return hearts_liste, vies



# =========================================================
# == UPDATE
# =========================================================
def update():
# flèches interactives
    global personnage_x,personnage_y,ennemis_liste_up,ennemis_liste_left,ennemis_liste_down,ennemis_liste_right,score,game,vies,niveau, coins_liste, hearts_liste
    
    personnage_x, personnage_y = personnage_deplacement(personnage_x, personnage_y)
    ennemis_liste_up = ennemis_creation(ennemis_liste_up, 1, 0)
    ennemis_liste_left = ennemis_creation(ennemis_liste_left, 0, 0)
    ennemis_liste_up = ennemis_deplacement(ennemis_liste_up, 1, 0)
    ennemis_liste_left = ennemis_deplacement(ennemis_liste_left, 0, 0)
    score = score_timer(score)
    game = lose(game)
    ennemis_liste_left, vies = collisions_left(ennemis_liste_left, vies)
    ennemis_liste_up, vies = collisions_up(ennemis_liste_up, vies)
    niveau = niveau_compteur(niveau)
    ennemis_liste_right, vies = collisions_right(ennemis_liste_right, vies)
    ennemis_liste_down, vies = collisions_down(ennemis_liste_down, vies)
    coins_liste = coins_creation(coins_liste)
    coins_liste, score = coins_collisions(coins_liste, score)
    hearts_liste = hearts_creation(hearts_liste)
    hearts_liste, vies = hearts_collisions(hearts_liste, vies)
    if niveau == 2:
        ennemis_liste_down = ennemis_creation(ennemis_liste_down, 1, 1)
        ennemis_liste_right = ennemis_creation(ennemis_liste_right, 0, 1)
        ennemis_liste_down = ennemis_deplacement(ennemis_liste_down, 1, 1)
        ennemis_liste_right = ennemis_deplacement(ennemis_liste_right, 0, 1)
    if pyxel.btn(pyxel.KEY_SPACE):
        game = False
        vies = 0
        ennemis_liste_up = []
        ennemis_liste_left = []
        if niveau == 2:
            ennemis_liste_down = []
            ennemis_liste_right = []
    if pyxel.btn(pyxel.KEY_R):
        game = True
        vies = 3
        score = 0
        personnage_x = 120
        personnage_y = 120
        ennemis_liste_up = []
        ennemis_liste_left = []
        if niveau == 2:
            ennemis_liste_down = []
            ennemis_liste_right = []
        niveau = 1
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    global personnage_x,personnage_y,ennemis_liste_up,ennemis_liste_left,ennemis_liste_down,ennemis_liste_right,score,vies,coins_liste
    # vide la fenetre
    pyxel.cls(0)     

    # backgrounds
    pyxel.bltm(0,0,0,0,0,255,255)
    
    pyxel.text(175, 190, f"Niveau: {niveau}", 0)
    
    if niveau == 1:
        pyxel.text(175, 200, f"Score: {score}/100", 0)
    elif niveau == 2:
        pyxel.text(175, 200, f"Score: {score}", 0)
  
    # dessiner le reste:
    pyxel.blt(personnage_x, personnage_y, 0, 0, 0, 16, 16, transparent_colour)
    
    for ennemi in ennemis_liste_up:
        pyxel.blt(ennemi[0], ennemi[1], 0, 0, 48, 8, 16, transparent_colour)
    for ennemi in ennemis_liste_left:
        pyxel.blt(ennemi[0], ennemi[1], 0, 0, 48, 16, 8, transparent_colour)
    for ennemi in ennemis_liste_down:
        pyxel.blt(ennemi[0], ennemi[1], 0, 0, 48, 8, 16, transparent_colour)
    for ennemi in ennemis_liste_right:
        pyxel.blt(ennemi[0], ennemi[1], 0, 0, 48, 16, 8, transparent_colour)
        
    for coin in coins_liste:
        pyxel.blt(coin[0], coin[1], 0, 0, 32, 16, 16, transparent_colour)
        
    for heart in hearts_liste:
        pyxel.blt(heart[0], heart[1], 0, 0, 16, 16, 16, transparent_colour_hearts)
    
    if game == False:
        pyxel.cls(7)
        pyxel.text(110, 100, "Game Over", 0)
        pyxel.text(90, 110, "Press 'R' to Restart", 0)
        pyxel.text(110, 120, f"Score: {score}", 0)
    
    if vies == 3:
        pyxel.blt(4, 4, 0, 0, 16, 16, 16, transparent_colour_hearts)
        pyxel.blt(24, 4, 0, 0, 16, 16, 16, transparent_colour_hearts)
        pyxel.blt(44, 4, 0, 0, 16, 16, 16, transparent_colour_hearts)
    elif vies == 2:
        pyxel.blt(4, 4, 0, 0, 16, 16, 16, transparent_colour_hearts)
        pyxel.blt(24, 4, 0, 0, 16, 16, 16, transparent_colour_hearts)
        pyxel.blt(44, 4, 0, 32, 48, 16, 16, transparent_colour_hearts)
    elif vies == 1:
        pyxel.blt(4, 4, 0, 0, 16, 16, 16, transparent_colour_hearts)
        pyxel.blt(24, 4, 0, 32, 48, 16, 16, transparent_colour_hearts)
        pyxel.blt(44, 4, 0, 32, 48, 16, 16, transparent_colour_hearts)

pyxel.run(update,draw)
