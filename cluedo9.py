import pyxel

# taille de la fenetre 512x512 pixels
# ne pas modifier
pyxel.init(512, 512)
pyxel.mouse(True)

x = 256
y = 128

# backgrounds

    
def update():
# flèches interactives
    global x,y
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()   
    elif pyxel.btnp(pyxel.KEY_T):
        y = y-10
    elif pyxel.btnp(pyxel.KEY_G):
        y = y+10
    elif pyxel.btnp(pyxel.KEY_F):
        x = x-10
    elif pyxel.btnp(pyxel.KEY_H):
        x = x+10
     
        
# draw
def draw():
    """création des objets (30 fois par seconde)"""
    global x,y
    # vide la fenetre
    pyxel.cls(0)
    
    pyxel.rect(x,y, 25,25, 6)
    
    pyxel.rect(256, 256, 128, 128, 13)
    
pyxel.run(update,draw)
