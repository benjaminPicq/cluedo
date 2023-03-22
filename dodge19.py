import pyxel, random
#www.pyxelstudio.net/qwklx584

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
transparent_colour_2 = 2
niveau = 0
coins_liste = []
hearts_liste = []
clouds_liste = []
bomb_liste = []
obstacles_liste = []


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
    # sens 0 = left/up et sens 1 = right/down
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
def collisions_ennemis(ennemis_liste, vies, sens):#sens 1 = left; sens 2 = right; sens 3 = up; sens 4 = down
    for ennemi in ennemis_liste:
        if sens == 1:
            if ((personnage_x + w +(w/2)) >= (ennemi[0] + w +(w/2)) >= personnage_x +(w/2)) and ((personnage_y + h + (h/2) + (h/2)) >= (ennemi[1] + (h/2) + (h/2)) >= personnage_y + (h/2)):
                    ennemis_liste.remove(ennemi)
                    vies = vies -1
        elif sens == 2:
            if ((personnage_x + w +(w/2)) >= ennemi[0] +(w/2) >= personnage_x +(w/2)) and ((personnage_y + h + (h/2) + (h/2)) >= (ennemi[1] + (h/2) + (h/2)) >= personnage_y + (h/2)):
                    ennemis_liste.remove(ennemi)
                    vies = vies -1
        elif sens == 3:
            if ((personnage_x + w + (w/2) +(w/2)) >= ennemi[0] + (w/2) +(w/2) >= personnage_x +(w/2)) and ((personnage_y + h + (h/2)) >= (ennemi[1] + h + (h/2)) >= personnage_y + (h/2)):
                    ennemis_liste.remove(ennemi)
                    vies = vies -1
        elif sens == 4:
            if ((personnage_x + w + (w/2) +(w/2)) >= (ennemi[0] + (w/2) +(w/2)) >= personnage_x +(w/2)) and ((personnage_y + h + (h/2)) >= ennemi[1] + (h/2) >= personnage_y + (h/2)):
                    ennemis_liste.remove(ennemi)
                    vies = vies -1
              
              
        for obstacle in obstacles_liste:
            obst1 = obstacle[0] + w +(w/2)
            if sens == 1:
                if obst1 >= (ennemi[0] + w +(w/2)) >= (obst1-w) and ((obstacle[1] + h + (h/2) + (h/2)) >= (ennemi[1] + (h/2) + (h/2)) >= obstacle[1] + (h/2)):
                        ennemis_liste.remove(ennemi)
            elif sens == 2:
                if ((obstacle[0] + w +(w/2)) >= ennemi[0] +(w/2) >= obstacle[0] +(w/2)) and ((obstacle[1] + h + (h/2) + (h/2)) >= (ennemi[1] + (h/2) + (h/2)) >= obstacle[1] + (h/2)):
                        ennemis_liste.remove(ennemi)
            elif sens == 3:
                if ((obstacle[0] + w + (w/2) +(w/2)) >= ennemi[0] + (w/2) +(w/2) >= obstacle[0] +(w/2)) and ((obstacle[1] + h + (h/2)) >= (ennemi[1] + h + (h/2)) >= obstacle[1] + (h/2)):
                        ennemis_liste.remove(ennemi)
            elif sens == 4:
                if ((obstacle[0] + w + (w/2) +(w/2)) >= (ennemi[0] + (w/2) +(w/2)) >= obstacle[0] +(w/2)) and ((obstacle[1] + h + (h/2)) >= ennemi[1] + (h/2) >= obstacle[1] + (h/2)):
                        ennemis_liste.remove(ennemi)
                        
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
    
    
    
    
def obstacles_creation(obstacles_liste):
    if len(obstacles_liste) < 2 :
        if (pyxel.frame_count % 30 == 0):
            obstacles_liste.append([random.randint(40,200), random.randint(40,200)])
    return obstacles_liste



def bomb_creation(bomb_liste):
    if niveau >= 2:
        if len(bomb_liste) < 1 :
            if (pyxel.frame_count % 600 == 0):
                bomb_liste.append([random.randint(40,200), random.randint(40,200)])
    return bomb_liste

def bomb_collisions(bomb_liste, ennemis_liste_up, ennemis_liste_left, ennemis_liste_down, ennemis_liste_right):
    for bombs in bomb_liste:
        if ((personnage_x + w) >= bombs[0] >= personnage_x - w) and ((personnage_y + h) >= bombs[1] >= personnage_y - h):
            bomb_liste.remove(bombs)
            ennemis_liste_up = []
            ennemis_liste_left = []
            ennemis_liste_down = []
            ennemis_liste_right = []
            
    return bomb_liste, ennemis_liste_up, ennemis_liste_left, ennemis_liste_down, ennemis_liste_right

def clouds_creation(clouds_liste):
    if (pyxel.frame_count % 10 == 0):
        clouds_liste.append([-w, random.randint(0, 240)])
    return clouds_liste
    
def clouds_deplacement(clouds_liste):
    for cloud in clouds_liste:
        cloud[0] += 1
    return clouds_liste


# =========================================================
# == UPDATE
# =========================================================
def update():
# flèches interactives
    global personnage_x,personnage_y,ennemis_liste_up,ennemis_liste_left,ennemis_liste_down,ennemis_liste_right,score,game,vies,niveau, coins_liste, hearts_liste, clouds_liste, bomb_liste, obstacles_liste
    if niveau == 0:
        if pyxel.btn(pyxel.KEY_S):
            niveau = 1
        clouds_liste = clouds_creation(clouds_liste)
        clouds_liste = clouds_deplacement(clouds_liste)
    if niveau >= 0:
        personnage_x, personnage_y = personnage_deplacement(personnage_x, personnage_y)
    if niveau >= 1:
        ennemis_liste_up = ennemis_creation(ennemis_liste_up, 1, 0)
        ennemis_liste_left = ennemis_creation(ennemis_liste_left, 0, 0)
        ennemis_liste_up = ennemis_deplacement(ennemis_liste_up, 1, 0)
        ennemis_liste_left = ennemis_deplacement(ennemis_liste_left, 0, 0)
        score = score_timer(score)
        game = lose(game)
        ennemis_liste_left, vies = collisions_ennemis(ennemis_liste_left, vies, 1)
        ennemis_liste_up, vies = collisions_ennemis(ennemis_liste_up, vies, 3)
        ennemis_liste_right, vies = collisions_ennemis(ennemis_liste_right, vies, 2)
        ennemis_liste_down, vies = collisions_ennemis(ennemis_liste_down, vies, 4)
        niveau = niveau_compteur(niveau)
        coins_liste = coins_creation(coins_liste)
        coins_liste, score = coins_collisions(coins_liste, score)
        hearts_liste = hearts_creation(hearts_liste)
        hearts_liste, vies = hearts_collisions(hearts_liste, vies)
        bomb_liste = bomb_creation(bomb_liste)
        bomb_liste, ennemis_liste_up, ennemis_liste_left, ennemis_liste_down, ennemis_liste_right = bomb_collisions(bomb_liste, ennemis_liste_up, ennemis_liste_left, ennemis_liste_down, ennemis_liste_right)
        obstacles_liste = obstacles_creation(obstacles_liste)
        hearts_liste, vies = hearts_collisions(hearts_liste, vies)
        
        if niveau == 2:
            ennemis_liste_down = ennemis_creation(ennemis_liste_down, 1, 1)
            ennemis_liste_right = ennemis_creation(ennemis_liste_right, 0, 1)
            ennemis_liste_down = ennemis_deplacement(ennemis_liste_down, 1, 1)
            ennemis_liste_right = ennemis_deplacement(ennemis_liste_right, 0, 1)
            bomb_liste = bomb_creation(bomb_liste)
            bomb_liste, ennemis_liste_up, ennemis_liste_left, ennemis_liste_down, ennemis_liste_right = bomb_collisions(bomb_liste, ennemis_liste_up, ennemis_liste_left, ennemis_liste_down, ennemis_liste_right)
        if pyxel.btn(pyxel.KEY_SPACE):
            game = False
            vies = 0
            ennemis_liste_up = []
            ennemis_liste_left = []
            coins_liste = []
            hearts_liste = []
            obstacles_liste = []
            if niveau == 2:
                ennemis_liste_down = []
                ennemis_liste_right = []
                bomb_liste = []
        if pyxel.btn(pyxel.KEY_R):
            game = True
            vies = 3
            score = 0
            personnage_x = 120
            personnage_y = 120
            ennemis_liste_up = []
            ennemis_liste_left = []
            coins_liste = []
            hearts_liste = []
            obstacles_liste = []
            if niveau == 2:
                ennemis_liste_down = []
                ennemis_liste_right = []
                bomb_liste = []
            niveau = 0
# =========================================================
# == DRAW
# =========================================================
def draw():
    """création des objets (30 fois par seconde)"""
    global personnage_x,personnage_y,ennemis_liste_up,ennemis_liste_left,ennemis_liste_down,ennemis_liste_right,score,vies,coins_liste, clouds_liste, transparent_colour, bomb_liste, obstacles_liste
    # vide la fenetre
    pyxel.cls(0)
    if niveau == 0:
        pyxel.bltm(0, 0, 0, 512, 0, 256, 256)
        for cloud in clouds_liste:
            pyxel.blt(cloud[0], cloud[1], 0, 0, 64, 16, 8, transparent_colour_2)
        pyxel.bltm(0, 0, 0, 256, 0, 256, 256, transparent_colour)
        pyxel.blt(personnage_x, personnage_y, 0, 32, 64, 16, 19, transparent_colour_2)
        pyxel.text(95, 210, "Press 'S' to Start", 0)
    if niveau >= 1:
        pyxel.rect(0, 0, 255, 255, 7)
    
        # backgrounds
        pyxel.bltm(0, 0, 0, 0, 0, 255, 255)
        pyxel.text(175, 190, f"Niveau: {niveau}", 0)
        
        # dessiner le reste:
        if niveau == 1:
            pyxel.text(175, 200, f"Score: {score}/100", 0)
        elif niveau == 2:
            pyxel.text(175, 200, f"Score: {score}", 0)
        
        pyxel.blt(personnage_x, personnage_y, 0, 0, 0, 16, 16, transparent_colour)
        
        for ennemi in ennemis_liste_up:
            pyxel.blt(ennemi[0], ennemi[1], 0, 16, 80, 8, -16, transparent_colour)
        for ennemi in ennemis_liste_left:
            pyxel.blt(ennemi[0], ennemi[1], 0, 0, 48 + 8, 16, 8, transparent_colour)
        for ennemi in ennemis_liste_down:
            pyxel.blt(ennemi[0], ennemi[1], 0, 16, 80, 8, 16, transparent_colour)
        for ennemi in ennemis_liste_right:
            pyxel.blt(ennemi[0], ennemi[1], 0, 0, 48 + 8, -16, 8, transparent_colour)
            
        for bombs in bomb_liste:
            pyxel.blt(bombs[0], bombs[1], 0, 0, 80, 16, 16, transparent_colour_2)
            
        for coin in coins_liste:
            pyxel.blt(coin[0], coin[1], 0, 0, 32, 16, 16, transparent_colour)
            
        for heart in hearts_liste:
            pyxel.blt(heart[0], heart[1], 0, 0, 16, 16, 16, transparent_colour_2)
            
        for obstacle in obstacles_liste:
            pyxel.blt(obstacle[0], obstacle[1], 0, 48, 64, 16, 16)
        
        if game == False:
            pyxel.cls(7)
            pyxel.bltm(0, 0, 0, 512, 0, 256, 256)
            pyxel.text(110, 100, "Game Over", 0)
            pyxel.text(90, 110, "Press 'R' to Restart", 0)
            pyxel.text(110, 120, f"Score: {score}", 0)
        
        if vies == 3:
            pyxel.blt(4, 4, 0, 0, 16, 16, 16, transparent_colour_2)
            pyxel.blt(24, 4, 0, 0, 16, 16, 16, transparent_colour_2)
            pyxel.blt(44, 4, 0, 0, 16, 16, 16, transparent_colour_2)
        elif vies == 2:
            pyxel.blt(4, 4, 0, 0, 16, 16, 16, transparent_colour_2)
            pyxel.blt(24, 4, 0, 0, 16, 16, 16, transparent_colour_2)
            pyxel.blt(44, 4, 0, 32, 48, 16, 16, transparent_colour_2)
        elif vies == 1:
            pyxel.blt(4, 4, 0, 0, 16, 16, 16, transparent_colour_2)
            pyxel.blt(24, 4, 0, 32, 48, 16, 16, transparent_colour_2)
            pyxel.blt(44, 4, 0, 32, 48, 16, 16, transparent_colour_2)

pyxel.run(update,draw)
