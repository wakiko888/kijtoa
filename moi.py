import pyxel
import math
from console_class import console

taille_ecran_x = 320
taille_ecran_y = 240

class App:
    def __init__(self):
        self.console = console(100, 100, 160, 120, taille_ecran_x, taille_ecran_y)
        pyxel.init(taille_ecran_x, taille_ecran_y, title="Hello Pyxel")
        pyxel.mouse(True)
        pyxel.run(self.update, self.draw)



    def update(self):
        self.console.Xpos = pyxel.mouse_x
        self.console.Ypos = pyxel.mouse_y
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_T):
            #mettre self.print_text(Le texte a afficher , le numéro correspondant a la couleur du texte)
            self.console.print_text("j'aime manger du caca", 2)


        if pyxel.btnp(pyxel.KEY_R):
            #mettre self.print_text(Le texte a afficher , le numéro correspondant a la couleur du texte)
            self.console.print_text("j'aime faire caca", 7)

    def draw(self):
        pyxel.cls(0)
        self.console.print_logs()
App()
