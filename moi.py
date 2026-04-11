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
        if self.Ytext == 10:
            pyxel.cls(0)
            self.Ytext = 0
        if pyxel.frame_count == 1:
            #mettre self.print_text(Le texte a afficher , le numéro correspondant a la couleur du texte)
            self.print_text("J'aime bouffer", 2)
            self.print_text("J'aime bouffer ton pere", 7)
            self.print_text("J'aime bouffer ta mere", 16)

    def draw(self):
        pyxel.cls(0)
        count = 0
        while count < len(self.logs):
            pyxel.text(0, count*6, self.logs[count], self.color_logs[count])
            count += 1
App()
