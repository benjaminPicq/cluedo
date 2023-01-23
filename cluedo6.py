import pyxel

# taille de la fenetre 512x512 pixels
# ne pas modifier
pyxel.init(512, 512)
mouse(True)



# backgrounds


# flèches interactives
    
    
# draw
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)
    
    pyxel.rect(256, 256, 256, 128, 13)
    
pyxel.run(draw)
