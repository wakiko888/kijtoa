import pyxel
def Rogue():
    return "Rogue"
def Warrior():
    return "Warrior"

class App():
    def __init__(self):
        pyxel.__init__(320,240, title="Marion")
        pyxel.run(self.update,self.draw)
    def update(self):
        if pyxel.btnp(pyxel.KEY_1):
            Warrior()
        if pyxel.btnp(pyxel.KEY_2):
            Rogue()
        

    def draw(self):
        pyxel.cls(7)
        pyxel.text(40, 70, self.update, 7)



