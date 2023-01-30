import pyxel

pyxel.init(512, 512)


x = 256
y = 400

def update():
# flèches interactives
    global x,y
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()   
    elif pyxel.btnp(pyxel.KEY_F):
        if (x > 5) :
            x = x-10
    elif pyxel.btnp(pyxel.KEY_H):
        if (x < 494) :
            x = x+10
    elif pyxel.btnp(pyxel.KEY_T):
        if (y > 5) :
            y = y-10
    elif pyxel.btnp(pyxel.KEY_G):
        if (y < 460) :
            y = y+10
     
        
# draw
def draw():
    """création des objets (30 fois par seconde)"""
    global x,y
    # vide la fenetre
    pyxel.cls(0)
    
    pyxel.rect(x,y, 16,56, 6)
    
    
pyxel.run(update,draw)
