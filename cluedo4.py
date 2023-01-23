import pyxel
#https://kitao.github.io/pyxel/wasm/launcher/?run=benjaminPicq.cluedo.

# taille de la fenetre 512x512 pixels
# ne pas modifier
pyxel.init(512, 512, title="Cluedo")
mouse(visible) = True



# backgrounds


# flèches interactives
    
    
# draw
def draw():
    """création des objets (30 fois par seconde)"""

    # vide la fenetre
    pyxel.cls(0)
    
    pyxel.rect(256, 256, 256, 128, 13)
    
pyxel.run(draw)
