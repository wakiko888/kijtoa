import pyxel


class App():
    def __init__(self):
        self.classe = ""
        pyxel.init(320,240, title="Marion")
        pyxel.run(self.update,self.draw)
    def update(self):
        if pyxel.btnp(pyxel.KEY_1):
            self.classe = "Warrior"
        if pyxel.btnp(pyxel.KEY_2):
            self.classe = "Rogue"


    def draw(self):
        phrase_classe = ""
        if self.classe != "":

            phrase_classe = "So you choose to became a " + self.classe
        pyxel.cls(0)
        pyxel.text(20, 40, phrase_classe , 7)

App()
