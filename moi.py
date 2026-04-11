import pyxel
import math

class App:
    def __init__(self):
        self.Ytext = 0
        self.logs = []
        self.color_logs = []
        pyxel.init(320, 240, title="Hello Pyxel")
        pyxel.run(self.update, self.draw)

    def print_text(self, text, col):
        self.logs.append(text)
        self.color_logs.append(col)

    def update(self):
        if pyxel.btnp(pyxel.KEY_Q):
            pyxel.quit()

        if pyxel.btnp(pyxel.KEY_T):
            #mettre self.print_text(Le texte a afficher , le numéro correspondant a la couleur du texte)
            self.print_text("J'aime bouffer", 2)


        if pyxel.btnp(pyxel.KEY_R):
            #mettre self.print_text(Le texte a afficher , le numéro correspondant a la couleur du texte)
            self.print_text("J'aime bouffer ton pere", 7)

    def draw(self):
        pyxel.cls(0)
        count = 0
        while count < len(self.logs):
            if count >= 39:
                self.logs.pop(0)
                self.color_logs.pop(0)
                count += -1
            pyxel.text(0, count*6, self.logs[count], self.color_logs[count])
            count += 1
App()
